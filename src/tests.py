#!/usr/bin/env python3
"""
This module runs tests on developer_greetings.py module classes and
functions of functions.py module
"""
import unittest
from developer_greetings import Question
from developer_greetings import Questions
import functions
import os


class ModuleTests(unittest.TestCase):
    def test_01(self):
        """
        Testing methods of a class "Question"
        """
        new_obj = Question("pet", "What is your pet?")

        # get_initial_attributes method
        self.assertEqual(new_obj.user_parameter, "pet")
        self.assertEqual(new_obj.get_user_parameter(), "pet")
        self.assertEqual(new_obj.value, "What is your pet?")
        self.assertEqual(new_obj.get_q_text(), "What is your pet?")
        self.assertEqual(new_obj.audio_f, "None")
        self.assertEqual(new_obj.get_audio_f(), "None")

        # edit_value method
        # change id of the Question object
        new_obj.edit_value("id", "3906d2c6-gf55-11ec-b826-a947e702f53d")
        self.assertEqual(new_obj.id, "3906d2c6-gf55-11ec-b826-a947e702f53d")
        self.assertEqual(new_obj.get_id(), "3906d2c6-gf55-11ec-b826-a947e702f53d")

        # change user_parameter of the Question object
        new_obj.edit_value("user_parameter", "animals")
        self.assertEqual(new_obj.user_parameter, "animals")
        self.assertEqual(new_obj.get_user_parameter(), "animals")

        # change question text of the Question object
        new_obj.edit_value("value", "What is your fav animal?")
        self.assertEqual(new_obj.value, "What is your fav animal?")
        self.assertEqual(new_obj.get_q_text(), "What is your fav animal?")

        # change path to the audio file of the Question object
        new_obj.edit_value("audio_f", "./audio/setup qs/Audio 2.m4a")
        self.assertEqual(new_obj.audio_f, "./audio/setup qs/Audio 2.m4a")
        self.assertEqual(new_obj.get_audio_f(), "./audio/setup qs/Audio 2.m4a")

        # __str__() method
        expected_output = "{\n  \"user_parameter\": \"animals\","
        expected_output += "\n  \"q_text\": \"What is your fav animal?\","
        expected_output += "\n  \"audio_f\": \"./audio/setup qs/Audio 2.m4a\","
        expected_output += "\n  \"id\": \"3906d2c6-gf55-11ec-b826-a947e702f53d\"\n}"
        self.assertEqual(str(new_obj), expected_output)

        # convert_to_json() method
        expected_output = "{\"user_parameter\": \"animals\", \"q_text\": \"What is your fav animal?\", \"audio_f\""
        expected_output += ": \"./audio/setup qs/Audio 2.m4a\", \"id\": \"3906d2c6-gf55-11ec-b826-a947e702f53d\"}"
        self.assertEqual(new_obj.convert_to_json(), expected_output)

    def test_02(self):
        """
        Testing methods of a class "Questions"
        """

        questions = Questions()

        # get_initial methods
        self.assertEqual(questions.qs, [])
        self.assertEqual(questions.get_qs(), [])

        # get_qs_from_json_db
        questions.get_qs_from_json_db("./json files/tests/test_01_2.json")
        self.assertEqual([q.get_user_parameter() for q in questions.get_qs()], [
            "None",
            "f_name",
            "nickname",
            "age",
            "location",
            "eyes' "
            "color",
            "self-esteem",
            "emotion",
        ])

        first_question = "Hi, so, I'm gonna ask you a couple of questions for my set up. "
        first_question += "It'll only take a few minutes. Is it ok if I do that?"
        self.assertEqual([q.get_q_text() for q in questions.get_qs()], [
            first_question,
            "What is your name?",
            "What would you like me to call you?",
            "How old are you?", "Where do you live?",
            "What is the color of your eyes?",
            "On a scale of one to ten, what do you think you are?",
            "Are you capable of empathy",
        ])
        self.assertEqual([q.get_audio_f() for q in questions.get_qs()], [
            "./audio/setup qs/Audio 1.m4a",
            "./audio/setup qs/Audio 2.m4a",
            "./audio/setup qs/Audio 3.m4a",
            "./audio/setup qs/Audio 4.m4a",
            "./audio/setup qs/Audio 5.m4a",
            "./audio/setup qs/Audio 6.m4a",
            "./audio/setup qs/Self Esteem.m4a",
            "None",
        ])
        self.assertEqual([q.get_id() for q in questions.get_qs()], [
            "3906cc9a-ac55-11ec-b826-a483e702f53d",
            "3906d06e-ac55-11ec-b826-a483e702f53d",
            "3906d1b8-ac55-11ec-b826-a483e702f53d",
            "3906d2c6-ac55-11ec-b826-a483e702f53d",
            "3906d3c0-ac55-11ec-b826-a483e702f53d",
            "d48ae116-ac54-11ec-9e60-a483e702f53d",
            "34edddcc-ac6b-11ec-93cf-a483e702f53d",
            "b724e52a-ac97-11ec-a387-a483e702f53d",
        ])

        # __str__() method
        # rendered_values is a list containing various question objects in json format
        # later when add_q() method will be tested, __str__() method will be used for the test
        # so rendered_values will be used as a template for creating expected output of __str__() method after running
        # add_q() method
        rendered_values: list[str] = list("[")
        rendered_values.append("{\n    \"user_parameter\": \"None\",\n    "
                               "\"q_text\": \"Hi, so, I'm gonna ask you a couple of questions for my set up. "
                               "It'll only take a few minutes. Is it ok if I do that?\",\n    "
                               "\"audio_f\": \"./audio/setup qs/Audio 1.m4a\",\n    "
                               "\"id\": \"3906cc9a-ac55-11ec-b826-a483e702f53d\"\n  },")
        rendered_values.append("  {\n    \"user_parameter\": \"f_name\",\n    "
                               "\"q_text\": \"What is your name?\",\n    "
                               "\"audio_f\": \"./audio/setup qs/Audio 2.m4a\",\n    "
                               "\"id\": \"3906d06e-ac55-11ec-b826-a483e702f53d\"\n  },")
        rendered_values.append("  {\n    \"user_parameter\": \"nickname\",\n    "
                               "\"q_text\": \"What would you like me to call you?\",\n    "
                               "\"audio_f\": \"./audio/setup qs/Audio 3.m4a\",\n    "
                               "\"id\": \"3906d1b8-ac55-11ec-b826-a483e702f53d\"\n  },")
        rendered_values.append("  {\n    \"user_parameter\": \"age\",\n    "
                               "\"q_text\": \"How old are you?\",\n    "
                               "\"audio_f\": \"./audio/setup qs/Audio 4.m4a\",\n    "
                               "\"id\": \"3906d2c6-ac55-11ec-b826-a483e702f53d\"\n  },")
        rendered_values.append("  {\n    \"user_parameter\": \"location\",\n    "
                               "\"q_text\": \"Where do you live?\",\n    "
                               "\"audio_f\": \"./audio/setup qs/Audio 5.m4a\",\n    "
                               "\"id\": \"3906d3c0-ac55-11ec-b826-a483e702f53d\"\n  },")
        rendered_values.append("  {\n    \"user_parameter\": \"eyes' color\",\n    "
                               "\"q_text\": \"What is the color of your eyes?\",\n    "
                               "\"audio_f\": \"./audio/setup qs/Audio 6.m4a\",\n    "
                               "\"id\": \"d48ae116-ac54-11ec-9e60-a483e702f53d\"\n  },")
        rendered_values.append("  {\n    \"user_parameter\": \"self-esteem\",\n    "
                               "\"q_text\": \"On a scale of one to ten, what do you think you are?\",\n    "
                               "\"audio_f\": \"./audio/setup qs/Self Esteem.m4a\",\n    "
                               "\"id\": \"34edddcc-ac6b-11ec-93cf-a483e702f53d\"\n  },")
        rendered_values.append("  {\n    \"user_parameter\": \"emotion\",\n    "
                               "\"q_text\": \"Are you capable of empathy\",\n    "
                               "\"audio_f\": \"None\",\n    "
                               "\"id\": \"b724e52a-ac97-11ec-a387-a483e702f53d\"\n  }")
        rendered_values.append("]")

        msg = "\n".join(rendered_values)

        self.assertEqual(str(questions), msg)

        # add_q() method: adding a new Question object to Questions object
        obj_2 = Question("love", "Do you have a significant other?", "None", "b726o22a-ac97-11ec-a387-a473e702f53d")
        questions.add_q(obj_2, os.getcwd() + "/json files/tests/test_01_2.json")

        rendered_values_2 = rendered_values.copy()
        rendered_values_2[8] = rendered_values[8] + ","
        rendered_values_2[9] = "  {\n    \"user_parameter\": \"love\",\n    " \
                               "\"q_text\": \"Do you have a significant other?\",\n    " \
                               "\"audio_f\": \"None\",\n    " \
                               "\"id\": \"b726o22a-ac97-11ec-a387-a473e702f53d\"\n  }"
        rendered_values_2.append(']')

        msg = "\n".join(rendered_values_2)
        self.assertEqual(str(questions), msg)

        # remove_q() method
        questions.remove_q("b726o22a-ac97-11ec-a387-a473e702f53d", "./json files/tests/test_01_2.json")
        msg = "\n".join(rendered_values)
        self.assertEqual(str(questions), msg)

        # edit_q() method
        questions.edit_q("b724e52a-ac97-11ec-a387-a483e702f53d",
                         "user_parameter",
                         "Ability to be empathetic",
                         "./json files/tests/test_01_2.json")
        rendered_values_3 = rendered_values.copy()
        rendered_values_3[8] = "  {\n    \"user_parameter\": \"Ability to be empathetic\",\n    " \
                               "\"q_text\": \"Are you capable of empathy\",\n    " \
                               "\"audio_f\": \"None\",\n    " \
                               "\"id\": \"b724e52a-ac97-11ec-a387-a483e702f53d\"\n  }"
        msg = "\n".join(rendered_values_3)
        self.assertEqual(str(questions), msg)
        questions.edit_q("b724e52a-ac97-11ec-a387-a483e702f53d",
                         "user_parameter",
                         "emotion",
                         "./json files/tests/test_01_2.json")

    def test_03(self):
        """
        Testing functions from functions.py module
        """
        # load_json_file() function
        self.assertEqual(functions.load_json_file("./json files/tests/test_01.json"), {
            'names': [
                {'name': 'andrei', 'audio_path': './audio/names/andrei.m4a'}
            ],
            'warning_msgs': [
                {
                    'value': "I didn't quite get that. Could you please tell me again: ",
                    'audio_path': './audio/warning msgs/wrms71851.m4a'
                }
            ]
        })


if __name__ == "__main__":
    unittest.main()
