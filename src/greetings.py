#!/usr/bin/env python3
import json
import os
from playsound import playsound


class UserInterface:
    def __init__(self, f_path, js_f_path):
        # f_path is a file from where you'll receive the json data
        self.f_path = f_path
        self.json_data = ""
        self.processed_data = []
        # js_f_path is a file where the processed answered will be saved
        self.js_f_path = js_f_path

    def load_json_data(self, f_path=""):
        if f_path == "":
            f_path = self.f_path
        if os.path.isfile(f_path):
            with open(f_path, "r") as f:
                js_dt = json.load(f)
                self.json_data = js_dt
                return js_dt
        else:
            return {}

    def process_json_data(self, *keys):
        res = self.json_data
        for key in keys:
            res = res[key]
        proc_data = [self.convert_json_to_dict(el) for el in res]
        return proc_data
        # self.processed_data = [self.convert_json_to_dict(el) for el in res]

    def set_processed_data(self, obj):
        self.processed_data = obj

    def convert_json_to_dict(self, obj):
        return json.loads(obj)

    def ask_question(self, q, audio_f=None):
        print(q)
        if audio_f is not None and audio_f != "None":
            playsound(audio_f)

    def warning_msg(self):
        with open("json files/audio.json", "r") as json_f_2:
            warning_msg = json.load(json_f_2)["warning_msgs"][0]

        q = warning_msg["value"]
        audio = warning_msg["audio_path"]
        self.ask_question(q, audio)

    def answer_question(self, msg=">>> "):
        inp = input(msg)
        return inp

    def check_answer(self, ans) -> bool:
        return len(ans) != 0

    def process_answer(self, ans, q):
        obj = {
            "user_parameter": q["user_parameter"],
            "value": ans
        }
        return obj

    def save_answer(self, obj_ans):
        obj_dict = self.load_json_data(self.js_f_path)
        obj_dict[obj_ans["user_parameter"]] = obj_ans["value"]
        self.update_js_db(obj_dict)

    def update_js_db(self, obj):
        with open(self.js_f_path, 'w') as json_file:
            json.dump(obj, json_file, indent=2)

    def interact(self):
        for el in self.processed_data:
            while True:
                self.ask_question(el["q_text"], el["audio_f"])
                ans = self.answer_question()
                if self.check_answer(ans):
                    proc_ans = self.process_answer(ans, el)
                    if el["user_parameter"] != 'None':
                        self.save_answer(proc_ans)
                    break
                self.warning_msg()

    def get_processed_data(self):
        print(self.processed_data)
        return self.processed_data


class Greetings:

    def __init__(self):
        self.name: str = "Kevin"
        self.description: str = "I'm your personal assistant. You can think of me as a friend."
        self.greet = greet


def greet_new_user():
    greetings = UserInterface("json files/greetings.json", "json files/user.json")
    greetings.load_json_data()
    proc_data = greetings.process_json_data("setup", "questions")
    greetings.set_processed_data(proc_data)
    greetings.interact()
