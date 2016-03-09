from source.question_answer import QA
from source.shape_checker import get_triangle_type, get_quadrilateral_type
from source.answer_funcs import (hal_20, current_time, get_fib, unit_convert, find_car, omnianswer,
how_r_u, who_r_u, shut_down, get_factorial, get_power, get_root, d_to_r, r_to_d)
from source.git_utils import (is_file_in_repo, get_repo_branch, get_repo_url, get_git_file_info, get_file_info)

import difflib
NOT_A_QUESTION_RETURN = "Was that a question?"
UNKNOWN_QUESTION = "I don't know, please provide the answer"
NO_QUESTION = 'Please ask a question first'
NO_TEACH = 'I don\'t know about that. I was taught differently'


class Interface(object):
    def __init__(self):
        self.how_ict = {}
        self.what_dict = {}
        self.where_dict = {}
        self.who_dict = {}

        self.keywords = ['How', 'What', 'Where', 'Who', "Why", 'Convert', 'Please', 'Open', 'Is']
        self.units = ['megameters','kilometers', 'hectometers', 'decameters', 'meters', 'decimeters', 'centimeters', 'millimeters', 'micrometers', 'nanometers']
        self.question_mark = chr(0x3F)

        self.question_answers = {
            'What type of triangle is ': QA('What type of triangle is ', get_triangle_type),
            'What type of quadrilateral is ': QA('What type of quadrilateral is ', get_quadrilateral_type),
            'Open the door hal': QA('Open the door hal', hal_20),
            'What time is it': QA('What time is it', current_time),
            'What is the digit of fibonacci ': QA('What is the digit of fibonacci ', get_fib),
            'Convert to ': QA('Convert to ', unit_convert),
            'Please clear memory': QA('Please clear memory', self.clear),
            'Where is my car': QA('Where is my car', find_car),
            'What is the answer to everything': QA('What is the answer to everything', omnianswer),
            'How are you': QA('How are you', how_r_u),
            'Who are you': QA('Who are you', who_r_u),
            'Please shut down hal': QA('Please shut down hal', shut_down),
            'What is factorial': QA('What is factorial', get_factorial),
            'What is to the power': QA('What is to the power', get_power),
            'What is the square root of ': QA('What is the square root of ', get_root),
            'What is degrees in radians': QA('What is degrees in radians', d_to_r),
            'What is radians in degrees': QA('What is radians in degrees', r_to_d),
            'Is the in the repo': QA('Is the in the repo', is_file_in_repo),
            'What is the status of': QA('What is the status of', get_git_file_info),
            'What is the deal with': QA('What is the deal with', get_file_info),
            'What branch is': QA('What branch is', get_repo_branch),
            'Where did come from': QA('Where did come from',get_repo_url),
        }
        self.last_question = None

    def ask(self, question=""):
        if not isinstance(question, str):
            self.last_question = None
            raise Exception('Not A String!')
        if question[-1] != self.question_mark or question.split(' ')[0] not in self.keywords:
            self.last_question = None
            return NOT_A_QUESTION_RETURN
        else:
            parsed_question = ""
            args = []
           
            for keyword in (question[:-1].split(' ')):
              
                try:
                    if keyword in self.units:
                        args.append(keyword)
                    elif (keyword[0] == '<'):
                        
                        keyword =(keyword[1:-1])
                        args.append(str(keyword))
                    else:
                        args.append(float(keyword))
                    
                      
                except:
                    parsed_question += "{0} ".format(keyword)

                

                
            parsed_question = parsed_question[0:-1]

            self.last_question = parsed_question
            for answer in self.question_answers.values():
                if difflib.SequenceMatcher(a=answer.question, b=parsed_question).ratio() >= .90:
                    if answer.function is None:
                        return answer.value
                    else:
                        try:
                            return answer.function(*args)
                        except Exception as ex:
                            print ex
                            raise Exception("Too many extra parameters")
            else:
                return UNKNOWN_QUESTION

    def teach(self, answer=""):
        if self.last_question is None:
            return NO_QUESTION
        elif self.last_question in self.question_answers.keys():
            return NO_TEACH
        else:
            self.__add_answer(answer)

    def correct(self, answer=""):
        if self.last_question is None:
            return NO_QUESTION
        else:
            self.__add_answer(answer)

    def clear(self):
        
        self.question_answers = []
        self.question_answers = {
            'What type of triangle is ': QA('What type of triangle is ', get_triangle_type),
            'What type of quadrilateral is ': QA('What type of quadrilateral is ', get_quadrilateral_type),
            'Open the door hal': QA('Open the door hal', hal_20),
            'What time is it': QA('What time is it', current_time),
            'What is the digit of fibonacci ': QA('What is the digit of fibonacci ', get_fib),
            'Convert to ': QA('Convert to ', unit_convert),
            'Please clear memory': QA('Please clear memory', self.clear),
            'Where is my car': QA('Where is my car', find_car),
            'What is the answer to everything': QA('What is the answer to everything', omnianswer),
            'How are you': QA('How are you', how_r_u),
            'Who are you': QA('Who are you', who_r_u),
            'Please shut down hal': QA('Please shut down hal', shut_down),
            'What is factorial': QA('What is factorial', get_factorial),
            'What is to the power': QA('What is to the power', get_power),
            'What is the square root of ': QA('What is the square root of ', get_root),
            'What is degrees in radians': QA('What is degrees in radians', d_to_r),
            'What is radians in degrees': QA('What is radians in degrees', r_to_d),
            'Is the in the repo': QA('Is the in the repo', is_file_in_repo),
            'What is the status of': QA('What is the status of', get_git_file_info),
            'What is the deal with': QA('What is the deal with', get_file_info),
            'What branch is': QA('What branch is', get_repo_branch),
            'Where did come from': QA('Where did come from',get_repo_url),
        }


    def __add_answer(self, answer):
        self.question_answers[self.last_question] = QA(self.last_question, answer)
