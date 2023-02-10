import _thread

DEBUG_MODE = True


# decorator Errors handling
def decorator(func):
    if DEBUG_MODE:
        print("Debugger mode is on")

    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return "Wrong input (*tip format of string in CMD: 1st - command, 2nd - Name, 3rd - Phone#). Try again!"
        # except TypeError:
        #     return "Wrong input. Command should be first. (*tip format of string in CMD: 1st - command, 2nd - Name, 3rd - Phone#). Try again!"

    return inner


contacts = {'name': 'phone'}


# text case insensetive
# @decorator
def flat_text(text: str) -> str:
    return text.casefold()


@decorator
def add(*args):
    name = args[0]
    phone = args[1]
    return f"add() func returned, this is name: {name} and phone: {phone}"


def abort(*args):
    print("Closing... \nGood bye! See you later.")
    _thread.exit()


INSTRUCTIONS = {
    add: ['add'],
    abort: ["close", "."]
}


def instructions_parser(user_input: str):
    for instr, key_word in INSTRUCTIONS.items():
        # if user_input.startswith(key_word):
        #     return instr, user_input.replace(key_word, "").strip().split()
        if user_input.startswith([i for i in key_word]):
            return instr, user_input.replace(i, "").strip().split()
    return None, None


def main():
    while True:
        user_input = input(">>>")
        command, data = instructions_parser(user_input)
        if not command:
            print("Unsupported command")
        else:
            print(command(*data))


if __name__ == "__main__":
    main()
    # print(flat_text("Hello Baby"))
