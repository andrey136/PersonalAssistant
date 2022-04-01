"""
This module contains reusable functions in various parts of the program
"""
import os
import json


def get_file_address(dir_and_f_names: list[str]) -> str:
    """
    returns absolute address to a file
    dir_and_f_names is a list of directories' and file's names we need to get the absolute address to
    """
    # loop goes through indexes of dir_and_f_names
    for _i in range(len(dir_and_f_names)):
        # checks whether there are spaces in directories' or file's name
        # if there are, they get replaced with "\\ ", so the terminal would see the complete address
        if len(dir_and_f_names[_i].split(' ')) > 1:
            dir_and_f_names[_i] = '\\ '.join(dir_and_f_names[_i].split(' '))
    # finds the absolute path to the current dir and joins it with a local file address
    f_address: str = os.path.join(os.getcwd(), os.path.join(*dir_and_f_names))
    return f_address


def execute_sh_cmd(obj: dict) -> None:
    """
    returns nothing, executes a shell command in the terminal
    obj is a dictionary that contains shell command
    """
    # obj template looks like:
    # {
    #     "cmd": "cat",
    #     "local_file_path" ["json files", "audio.json"]
    # }
    shell_cmd: str = obj["cmd"]
    # checking if there's an address to a file the shell command will interact with
    if obj.get("local_file_path", 0) != 0:
        address: str = get_file_address(obj["local_file_path"])
        shell_cmd = ' '.join([obj["cmd"], address])
    # executing the command
    os.system(shell_cmd)


def load_json_file(f_path: str) -> json:
    """
    returns json data
    f_path is an address to a json file
    """
    with open(f_path, "r") as f:
        return json.load(f)


def separate_line() -> None:
    """
    returns nothing, prints a line separating different output messages
    """
    print("----" * 14)
