from deeppavlov.core.models.component import Component
from bpr.biencoder import BiEncoder
from transformers import AutoTokenizer
from torch.nn.parallel import DataParallel
import numpy as np
from deeppavlov.core.common.registry import register

@register('biembedder')
class PretrainedBiEncoder(Component):
    def __init__(self, pretrained_bpr_path: str, device, parallel=True, *args, **kwargs) -> None:
        super().__init__()
        self.biencoder = BiEncoder.load_from_checkpoint(pretrained_bpr_path, map_location=device)
        self.biencoder.to(device)
        self.biencoder.eval()
        self.biencoder.freeze()

        self.tokenizer = AutoTokenizer.from_pretrained(self.biencoder.hparams.base_pretrained_model, use_fast=True)
        self.passage_encoder = self.biencoder.passage_encoder
        if parallel:
            self.passage_encoder = DataParallel(self.passage_encoder)
        self.device = device


    def __call__(self, passages, query=False, *args, **kwargs):
        tokenizer = self.tokenizer
        biencoder = self.biencoder

        passage_inputs = tokenizer.batch_encode_plus(
                [("", passage) for passage in passages],
                return_tensors="pt",
                max_length=biencoder.hparams.max_passage_length,
                pad_to_max_length=True,
        )

        passage_inputs = {k: v.to(self.device) for k, v in passage_inputs.items()}
        emb = self.passage_encoder(**passage_inputs) if not query else self.biencoder.query_encoder(**passage_inputs)
        emb = biencoder.convert_to_binary_code(emb).cpu().numpy()
        emb = np.where(emb == -1, 0, emb).astype(np.bool)
        return emb

