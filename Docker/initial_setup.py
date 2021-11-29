from pathlib import Path
from shutil import copytree

from deeppavlov.core.commands.utils import parse_config


def initial_setup():
    config = parse_config('ner_rus_vx_distil.json')
    model_path = config['metadata']['variables']['NER_PATH']
    init_path = next(
        i for i in config['metadata']['download'] if 'ner_rus_distilbert_torch.tar.gz' in i['url']
    )['subdir']
    if not Path(model_path).exists():
        copytree(init_path, model_path)
