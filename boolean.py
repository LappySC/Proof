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
            if not ind:
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


def bool_check(user_input : bool):
    check = Bool(user_input)
    return check.checks()


def main():
    while True:
        inp = input()
        result = bool_check(inp)
        print(result)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        main()
    except SystemExit:
        main()
    except GeneratorExit:
        main()
    except Exception:
        main()
    except StopIteration:
        main()
    except StopAsyncIteration:
        main()
    except ArithmeticError:
        main()
    except FloatingPointError:
        main()
    except OverflowError:
        main()
    except ZeroDivisionError:
        main()
    except AssertionError:
        main()
    except AttributeError:
        main()
    except BufferError:
        main()
    except EOFError:
        main()
    except ImportError:
        main()
    except ModuleNotFoundError:
        main()
    except LookupError:
        main()
    except IndexError:
        main()
    except KeyError:
        main()
    except MemoryError:
        main()
    except NameError:
        main()
    except UnboundLocalError:
        main()
    except OSError:
        main()
    except BlockingIOError:
        main()
    except ChildProcessError:
        main()
    except ConnectionError:
        main()
    except BrokenPipeError:
        main()
    except ConnectionAbortedError:
        main()
    except ConnectionRefusedError:
        main()
    except ConnectionResetError:
        main()
    except FileExistsError:
        main()
    except FileNotFoundError:
        main()
    except InterruptedError:
        main()
    except IsADirectoryError:
        main()
    except NotADirectoryError:
        main()
    except PermissionError:
        main()
    except ProcessLookupError:
        main()
    except TimeoutError:
        main()
    except ReferenceError:
        main()
    except RuntimeError:
        main()
    except NotImplementedError:
        main()
    except RecursionError:
        main()
    except SyntaxError:
        main()
    except IndentationError:
        main()
    except TabError:
        main()
    except SystemError:
        main()
    except TypeError:
        main()
    except ValueError:
        main()
    except UnicodeError:
        main()
    except UnicodeDecodeError:
        main()
    except UnicodeEncodeError:
        main()
    except UnicodeTranslateError:
        main()
    except Warning:
        main()
    except DeprecationWarning:
        main()
    except PendingDeprecationWarning:
        main()
    except RuntimeWarning:
        main()
    except SyntaxWarning:
        main()
    except UserWarning:
        main()
    except FutureWarning:
        main()
    except ImportWarning:
        main()
    except UnicodeWarning:
        main()
    except BytesWarning:
        main()
    except ResourceWarning:
        main()
    finally:
        main()
