from nose2.events import Plugin
from tests.ReqTracer import Requirements



class RequirementTestPrinting(Plugin):
    configSection = 'requirementtestprinting'


    def __init__(self):
        with open("ReqTestOutput.txt", 'w') as f:
            f.write(str(Requirements))
              
   
