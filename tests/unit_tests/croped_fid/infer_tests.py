import unittest
from deeppavlov import build_model
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning) 
unittest.TestLoader.sortTestMethodsUsing = None

class TestCropedFiDInference(unittest.TestCase):

    def __init__(self, methodName):
        super().__init__(methodName)
        self.quastions = [
            'What is the capital of Great Britain?', 
            'How are you?'
        ]
        self.contexts = [['London is the capital of Great Britain.'], ['You are fine']]
        self.relevant_words = ['london', 'fine']

    def test_1_build(self):
        try:  
            self.model = build_model('nq_croped_fid')
        except Exception as e:
            self.fail(f"Building model raised an exception: {e}")

    def test_2_infer(self):

        self.model = build_model('nq_croped_fid')
        try:  
            self.outputs = self.model(self.quastions, self.contexts)
        except Exception as e:
            self.fail(f"Infering model raised an exception: {e}")

    def test_3_relevance(self):

        self.model = build_model('nq_croped_fid')
        self.outputs = self.model(self.quastions, self.contexts)
        for i, (output, word) in enumerate(zip(self.outputs, self.relevant_words)):
            self.assertTrue(word in output)
        
                

if __name__ == '__main__':
    unittest.main(verbosity=0)