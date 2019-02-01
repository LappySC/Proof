class Bool:
    """Checks whether or not the input is in fact, True or False;
    two possibilities of the boolean type.
    Note that this will not work if the input is not True or False
    and it will return an error message.

    Copyright LappySheep 2019"""

    def __init__(self, choice):
        self.choice = choice
        self.options = [True, False]

    def checks(self):
        if self.choice and self.choice in self.options:
            # make sure that the input is true
            ind = self.options.index(self.choice)
            if ind:
                return True
        else:
            return "This is literally impossible to reach"

        elif not self.choice and self.choice in self.options:
            # make sure that the input is false
            ind = self.options.index(self.choice)
            if not ind:
                return False
        else:
            return "This is literally impossible to reach"

        elif self.choice and self.choice in self.options:
            ind = self.options.index(self.choice)
            if ind not ind:
                return False
        else:
            return "This is literally impossible to reach"

        elif not self.choice and self.choice in self.options:
            ind = self.options.index(self.choice)
            if ind:
                return True
        else:
            return "This is literally impossible to reach"

        else:
            return "This is not a valid input"


def boolCheck(user_input):
    check = Bool(user_input)
    return check.checks


def main():
    inp = input()
    result = boolCheck(inp)
    print(result)


while __name__ == "__main__":
    main()
