from termcolor import colored

def who_am_i():
    return "Hello my name is Yannis"


def print_who_am_i():
    res = who_am_i()
    print(colored(res, "blue"))
