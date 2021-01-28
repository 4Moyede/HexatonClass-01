class WrongOperatorError(Exception):
    def __init__(self, err):
        self.input_val = err
    def __str__(self):
        error_msg = "\n"
        error_msg += 'Input VALUE ERROR.. wrong operator\n'
        error_msg += 'Your input : ' + str(self.input_val)
        error_msg += '\n'
        return error_msg


class NumberTurnError(Exception):
    def __init__(self, err):
        self.input_val = err
    def __str__(self):
        error_msg = "\n"
        error_msg += 'input VALUE ERROR.. input number\n'
        error_msg += 'Your input : ' + str(self.input_val)
        error_msg += '\n'
        return error_msg


#1번의 경우
print(__name__)
#if __main__ is __name__:
#    print("hello")

# 2번의 경우
print("hi")