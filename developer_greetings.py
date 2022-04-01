#!/usr/bin/env python3
"""
This module creates and manages an interface for developer, who's trying to change the parameters of the program.
This module can create, edit or remove questions that the program is supposed to ask
It works through terminal
"""
import json
import uuid
from functions import load_json_file, separate_line


class Interface:
    """
    class Interface creates an interactive interface in the terminal for developer to work with
    """
    def __init__(self, qs_obj) -> None:
        """
        dev_interface: developer interface in json format
        qs_obj: Question object
        """
        self.dev_interface: dict = {}
        self.qs_obj = qs_obj

    def greet_dev(self) -> str:
        """
        Prints out greeting to a developer
        Returns the same greeting in string format
        """
        output: str = self.dev_interface["msg"]
        print(output)
        return output

    def load_dev_interface(self, json_path: str) -> None:
        """
        returns nothing, loads developer interface from json file
        json_path: path to a json file
        """
        self.dev_interface = load_json_file(json_path)["developer"]

    def see_options(self) -> str:
        """
        Prints out different options the developer may use for changing or retrieving data
        for greetings.py module
        returns str
        """
        options: list = self.dev_interface["options"]
        output: str = ''.join(["\n    \"" + str(_i) + "\" --> " + options[_i] for _i in range(len(options))])[1:]
        output += "\n    \"quit()\" --> to end the session"
        print(output)
        return output

    def interact(self) -> None:
        """
        returns nothing, interacts with the developer through the terminal window
        """
        while True:
            separate_line()
            self.see_options()
            cmd: str = input(">>> ")

            if cmd == "1":
                par: str = input("Enter user_parameter: \n>>> ")
                val: str = input("Enter question: \n>>> ")
                audio: str = input("Enter audio path: \n>>> ")
                self.qs_obj.add_q(Question(par, val, audio))
                print("Object is added")

            elif cmd == "2":
                print(self.qs_obj)

            elif cmd == "3":
                _id: str = input("Enter id of the question you want to delete: \n>>> ")
                self.qs_obj.remove_q(_id)
                print("The question is deleted!!!")

            elif cmd == "0":
                json_data = load_json_file("json files/greetings.json")
                print(json_data)

            elif cmd == "4":
                _id: str = input("Enter id of the question you want to edit: \n>>> ")
                par: str = input("Enter attribute: \n>>> ")
                val: str = input("Enter val: \n>>> ")
                self.qs_obj.edit_q(_id, par, val)
                print("Question edited!!!")

            elif cmd == "quit()":
                print("Session is over")
                break

            else:
                msg: str = "There's no such option. Choose something from the available options!"
                print(msg)


class Questions:
    """
    class Questions allows the developer to add, edit or remove question(s) if needed
    It updates and takes data from json files
    """
    def __init__(self) -> None:
        """
        qs: a list of Question objects
        """
        self.qs: list = []

    def get_qs(self) -> list:
        """
        returns a list of Question objects
        """
        return self.qs

    def add_q(self, obj, f_path: str = "json files/greetings.json") -> None:
        """
        Adds a new Question object to Questions
        returns nothing
        obj: Question object
        f_path: path to json file that keeps questions in json format
        """
        self.qs = self.qs + [obj]
        self.update_json_db(f_path)

    def remove_q(self, _id: str, f_path: str = "json files/greetings.json") -> None:
        """
        Removes a Question object from Questions
        returns nothing
        _id: Question object's id
        f_path: path to json file that keeps questions in json format
        """
        self.qs = [obj for obj in self.qs if obj.id != _id]
        self.update_json_db(f_path)

    def edit_q(self, _id: str, attr: str, val: str, f_path: str = "json files/greetings.json") -> None:
        """
        Edits a Question object in Questions
        returns nothing
        _id: Question object's id
        attr: any key in Question object's json format
        val: a new value to any key in Question object's json format
        f_path: path to json file that keeps questions in json format
        """
        obj = [el for el in self.qs if el.id == _id][0]
        obj.edit_value(attr, val)
        self.update_json_db(f_path)

    def update_json_db(self, f_path: str = "json files/greetings.json") -> None:
        """
        Updates data in json file
        returns nothing
        f_path: path to json file that keeps questions in json format
        """
        json_qs: list[json] = [q.convert_to_json() for q in self.qs]
        obj: dict = load_json_file(f_path)
        obj["setup"]["questions"] = json_qs
        with open(f_path, "w") as js_f:
            json.dump(obj, js_f, indent=2)

    def get_qs_from_json_db(self, f_path: str = "json files/greetings.json") -> None:
        """
        Retrieves data from json file and creates a Questions object
        returns nothing
        """
        json_qs: list[json] = load_json_file(f_path)["setup"]["questions"]
        questions: list[dict] = [json.loads(q) for q in json_qs]
        for q in questions:
            new_question = Question(q["user_parameter"], q["q_text"], q["audio_f"], q["id"])
            self.add_q(new_question)

    def __str__(self):
        resp = '[\n'
        for _i in range(len(self.qs)):
            q = self.qs[_i]
            resp += '\n  '.join(str(q).split('\n'))
            if _i != len(self.qs) - 1:
                resp += ',\n  '
        resp += '\n]'
        return resp


class Question:
    """
    class Question creates a question object. Its methods can get all object parameters,
    edit any of the object parameters or
    convert itself into json data
    """
    def __init__(self, user_parameter: str, value: str, audio_f: str = "None", _id: str = str(uuid.uuid1())) -> None:
        """
        user_parameter: a descriptive word for the question that user will be later asked
        value: the question users are asked
        audio_f: it's a path to the audio file(needed for playing the question)
        _id: it's a private unique value assigned to every question
        """
        self.user_parameter = user_parameter
        self.value = value
        self.audio_f = audio_f
        self.id = _id

    def get_user_parameter(self) -> str:
        """
        returns user_parameter
        """
        return self.user_parameter

    def get_q_text(self) -> str:
        """
        returns question text
        """
        return self.value

    def get_audio_f(self) -> str:
        """
        returns path to an audio file
        """
        return self.audio_f

    def get_id(self) -> str:
        """
        returns Question object's id
        """
        return self.id

    def edit_value(self, attr: str, val: str) -> None:
        """
        Sets a certain Question object's attribute to a different value
        returns nothing
        """
        setattr(self, attr, val)

    def __str__(self):
        output = "{\n  \"user_parameter\": \"" + self.user_parameter
        output += "\",\n  \"q_text\": \"" + self.value
        output += "\",\n  \"audio_f\": \"" + self.audio_f
        output += "\",\n  \"id\": \"" + self.id + "\"\n}"
        return output

    def convert_to_json(self):
        """
        Converts Question object's data into a json format
        Returns json data
        """
        obj = {
            "user_parameter": self.user_parameter,
            "q_text": self.value,
            "audio_f": self.audio_f,
            "id": self.id,
        }
        return json.dumps(obj)


if __name__ == "__main__":
    qs = Questions()
    qs.get_qs_from_json_db()
    interface = Interface(qs)

    interface.load_dev_interface("json files/greetings.json")
    interface.greet_dev()
    interface.interact()
