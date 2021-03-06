

class RequirementTrace(object):
    req_text = ""
    def __init__(self, text):
        self.req_text = text
        self.func_name = []

Requirements = {}

def requirements(req_list):
    def wrapper(func):
        def add_req_and_call(*args, **kwargs):
            for req in req_list:
                if req not in Requirements.keys():
                    raise Exception('Requirement {0} not defined'.format(req))
                Requirements[req].func_name.append(func.__name__)
            return func(*args, **kwargs)

        return add_req_and_call

    return wrapper

with open('pyTonaRequirements.txt') as f:
    for line in f.readlines():
        if '#00' in line:
            req_id, desc = line.split(' ', 1)
            Requirements[req_id] = RequirementTrace(desc)



class StoryTrace(object):
    req_text = ""
    def __init__(self, text):
        self.req_text = text
        self.func_name = []

Stories = {}

def stories(story_list):
    def wrapper(func):
        def add_story_and_call(*args, **kwargs):
            for story in story_list:
                if story not in Stories.keys():
                    raise Exception('Story {0} not defined'.format(story))
                Stories[story].func_name.append(func.__name__)
            return func(*args, **kwargs)

        return add_story_and_call

    return wrapper

with open('pyTonaRequirements.txt') as f:
    for line in f.readlines():
        if '*00' in line:
            story_id, desc = line.split(' ', 1)
            Stories[story_id] = StoryTrace(desc)
