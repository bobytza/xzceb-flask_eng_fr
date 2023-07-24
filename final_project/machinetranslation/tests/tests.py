import unittest
import sys
sys.path.append("/home/project/xzceb-flask_eng_fr/final_project/")
from machinetranslation.translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french("Hello"), "Bonjour") # test Hello = Bonjour
        
class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english("Bonjour"), "Hello") # test Bonjour = Hello
        
unittest.main()