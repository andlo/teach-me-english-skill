from mycroft import MycroftSkill, intent_file_handler


class TeachMeEnglish(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('english.me.teach.intent')
    def handle_english_me_teach(self, message):
        self.speak_dialog('english.me.teach')


def create_skill():
    return TeachMeEnglish()

