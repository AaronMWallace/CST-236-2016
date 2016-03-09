from ReqTracer import requirements, stories
from source.main import Interface
import git_utils
import unittest, getpass, datetime
import mock
from mock import Mock, patch


class pyTona_testing(unittest.TestCase):
    def setUp(self):
        self.obj = Interface()

    def test_exceptions(self):
        self.assertRaises(Exception, self.obj.ask, 7)
        self.assertRaises(Exception, self.obj.ask, "Who are 17 you?")

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

#-------------------------------------------------------------------------------------------------
    @stories(['*0005'])
    def test_job_story_hal(self):
        ret = self.obj.ask("Open the door hal?")
        self.assertEqual(ret, "I'm afraid I can't do that {0}".format(getpass.getuser()))

    @stories(['*0001'])
    def test_job_story_time(self):
        ret = self.obj.ask("What time is it?")
        self.assertEqual(ret, datetime.datetime.now())

    @stories(['*0002'])
    def test_job_story_fibonacci(self):
        ret = self.obj.ask("What is 15 the digit of fibonacci?")
        self.assertEqual(ret, 610)

    @stories(['*0006','*0007'])
    def test_job_story_unit_conversions(self):
        ret = self.obj.ask("Convert 13 megameters to kilometers?")
        self.assertEqual(ret, 13000.0)
        ret = self.obj.ask("Convert 24 hectometers to decameters?")
        self.assertEqual(ret, 240.0)
        ret = self.obj.ask("Convert 1 meters to decimeters?")
        self.assertEqual(ret, 10)
        ret = self.obj.ask("Convert 54 centimeters to millimeters?")
        self.assertEqual(ret, 540.0)
        ret = self.obj.ask("Convert 62 micrometers to nanometers?")
        self.assertEqual(ret, 61999.99999999999)

    @stories(['*0004'])
    def test_job_story_clear(self):

        self.obj.ask("What is my name?")
        self.obj.teach("Jack")
        ret = self.obj.ask("What is my name?")
        self.assertEqual(ret, "Jack")
        self.obj.ask("Please clear memory?")

        ret = self.obj.ask("What is my name?")
        self.assertEqual(ret, "I don't know, please provide the answer")


    @stories(['*0008','*0009','*0010','*0011','*0012'])
    def test_more_job_stories(self):
        ret = self.obj.ask("Where is my car?")
        self.assertEqual(ret, "In the driveway {0}".format(getpass.getuser()))

        ret = self.obj.ask("What is the answer to everything?")
        self.assertEqual(ret, "42")

        ret = self.obj.ask("How are you?")
        self.assertEqual(ret, "I am doing well {0}".format(getpass.getuser()))

        ret = self.obj.ask("Who are you?")
        self.assertEqual(ret, "My name is PyTona")

        ret = self.obj.ask("Please shut down hal?")
        self.assertEqual(ret, "I am afraid I cannot do that right now {0}".format(getpass.getuser()))
#------------------------------------------------------------------------------------------

    @requirements(['#0022']) 
    def test_factorial(self):
        ret = self.obj.ask("What is 6 factorial?")
        self.assertEqual(ret, 720)
        
    @requirements(['#0023']) 
    def test_power(self):
        ret = self.obj.ask("What is 2 to the 3 power?")
        self.assertEqual(ret, 8)
        
    @requirements(['#0024']) 
    def test_root(self):
        ret = self.obj.ask("What is the square root of 256?")
        self.assertEqual(ret, 16)
        
    @requirements(['#0025']) 
    def test_degress_to_radians(self):
        ret = self.obj.ask("What is 78 degrees in radians?")
        self.assertEqual(ret, 1)
        
    @requirements(['#0026']) 
    def test_radians_to_degrees(self):
        ret = self.obj.ask("What is 2 radians in degrees?")
        self.assertEqual(ret, 114)

#--------------------------------------------------------------------------------------------------------

    @patch('git_utils.subprocess.Popen')
    def test_if_file_is_in_repo(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('stdout', 'stderr')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock 
        ret = self.obj.ask("Is the <C:\Python27\Scripts> in the repo?")
        self.assertTrue(mock_subproc_popen.called)
        self.assertEqual(ret, "Yes")


    @patch('git_utils.subprocess.Popen')
    def test_get_branch(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('stdout', 'stderr')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock 
        ret = self.obj.ask("What branch is <C:\Python27\Scripts>?")
        self.assertTrue(mock_subproc_popen.called)
        self.assertEqual(ret, "Yes")

    


    
























        
        
        

        
        



