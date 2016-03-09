from ReqTracer import requirements
from source.main import Interface
import unittest

class pyTona_testing(unittest.TestCase):
    def setUp(self):
        self.obj = Interface()

    @requirements(['#0017'])    
    def test_teach(self):
        ret = self.obj.teach()
        self.assertEqual(ret, "Please ask a question first")

    @requirements(['#0021'])
    def test_correct(self):
        ret = self.obj.correct()
        self.assertEqual(ret, "Please ask a question first")

    @requirements(['#0016', '#0018'])    
    def test_teach_2(self):
        self.obj.ask("What is my name?")
        self.obj.teach("Bubba")
        ret = self.obj.ask("What is my name?")
        self.assertEqual(ret, "Bubba")
        
        ret = self.obj.teach("Fred")
        self.assertEqual(ret, "I don\'t know about that. I was taught differently")
        ret = self.obj.ask("What is my name?")
        self.assertEqual(ret, "Bubba")
               
    @requirements(['#0006', '#0007', '#0014'])
    def test_ask(self):
        ret = self.obj.ask("What is 8 feet in miles?")
        self.assertEqual(ret, "I don't know, please provide the answer")
        ret = self.obj.ask("How many seconds since?")
        self.assertEqual(ret, "I don't know, please provide the answer")
        ret = self.obj.ask("Who invented Python?")
        self.assertEqual(ret, "I don't know, please provide the answer")
        ret = self.obj.ask("Why don\'t you understand me?")
        self.assertEqual(ret, "I don't know, please provide the answer")
        ret = self.obj.ask("Why don\'t you shutdown?")
        self.assertEqual(ret, "I don't know, please provide the answer")
        ret = self.obj.ask("Where am I?")
        self.assertEqual(ret, "I don't know, please provide the answer")


    @requirements(['#0008'])
    def test_ask_again(self):
        ret = self.obj.ask("Half Life 3 confirmed?")
        self.assertEqual(ret, "Was that a question?")
        
    @requirements(['#0009'])
    def test_ask_no_question_mark(self):
        ret = self.obj.ask("Half Life 3 confirmed")
        self.assertEqual(ret, "Was that a question?")
                   
    @requirements(['#0010','#0011','#0012','#0013','#0016'])
    def test_ask_more_questions(self):
        ret = self.obj.ask("What type tf triangle is 5 5 5?")#swapped 'of' with 'tf'
        self.assertEqual(ret, "equilateral")

        ret = self.obj.ask("What typ tf trIange iz 5 5 5?")#really messed up the grammar
        self.assertEqual(ret, "I don't know, please provide the answer")


    @requirements(['#0019','#0020'])            
    def test_correct_2(self):
        self.obj.ask("What type of quadrilateral is 5 5 5 5 90 90 90 90?")
        self.obj.correct("circle")

        ret = self.obj.ask("What type of quadrilateral is 5 5 5 5 90 90 90 90?")
        self.assertEqual(ret, "circle")

        

    
