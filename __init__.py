from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler


class ThemeChangeSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder().require('ThemeChange'))
    def handle_theme_change(self, message):
        self.speak_dialog('theme.change')


def create_skill():
    return ThemeChangeSkill()

