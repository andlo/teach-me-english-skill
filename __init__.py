from mycroft import MycroftSkill, intent_file_handler


class TeachMeEnglish(MycroftSkill):
    def initialize(self):
        self.add_event("speak", self.capture_speaks)
        self.last_speech = ""
        self.capture = False

    def capture_speaks(self, message):
        if self.capture == True:
            self.last_speech = message.data.get("utterance", "")

    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('teaching.intent')
    def handle_teaching(self, message):
        user_said = None
        
        while (user_said != "stop"):   
            self.speak_dialog('repeat_after_me', expect_response=False)
            self.capture = True
            user_said = self.get_response("lesson",num_retries=0)    
            self.capture = False
            lesson = self.last_speech
            retries = 3
            while lesson != None and user_said != "stop" and retries != 0:          
                if user_said and user_said == self.last_speech:
                    self.speak_dialog("perfect", expect_response=False)
                    lesson = None
                elif user_said == None:
                    retries = retries - 1
                    if retries == 0:
                        user_said = "stop"
                    else:
                        self.speak_dialog("repeat_after_me", expect_response=False)
                        self.capture = True
                        user_said = self.get_response(lesson,num_retries=0)
                        self.capture = False    
                else:
                    retries = retries - 1
                    self.speak_dialog("notperfect", expect_response=False)
                    self.speak_dialog("repeat_after_me", expect_response=False)
                    self.capture = True
                    user_said = self.get_response(lesson,num_retries=0)    
                    self.capture = False
                    
            self.speak_dialog("lets_try_another_one", expect_response=False)

        self.speak_dialog('teaching_stop', expect_response=False)
        self.capture = False

def create_skill():
    return TeachMeEnglish()

