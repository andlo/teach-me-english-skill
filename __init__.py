from mycroft import MycroftSkill, intent_file_handler


class TeachMeEnglish(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('english.me.teach.intent')
    def handle_english_me_teach(self, message):
        self.speak_dialog('english.me.teach')
        lesson = self.get_response("repeat")

 
 
    @intent_file_handler('teaching.intent')
    def  teaching_intent(self, message):
        # response = {'name': message.data.get("name")}
        if message == lesson:
            self.speak_dialog("perfect")
        else:
            self.speak_dialog("notperfect")
            self.speak(lesson)

def create_skill():
    return TeachMeEnglish()

