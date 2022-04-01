#!/usr/bin/env python3
from greetings import greet_new_user


class PersonalAssistant:
    def __init__(self):
        self.name: str = "Kevin"

    def sign_up_new_user(self):
        greet_new_user()


if __name__ == "__main__":
    assistant = PersonalAssistant()
    assistant.sign_up_new_user()
