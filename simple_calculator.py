class Calculator:
    def __init__(self, init_value=0):
        self.value = init_value

    def power(self, *args):  # последовательное возведение в степень
        for x in args:
            self.value **= x
        return self

    def root(self, *args):  # последовательное извлечение корней из числа
        for x in args:
            if x != 0:
                self.value **= (1/x)
        return self

    def add(self, *args):
        self.value += sum(args)
        return self

    def multiply(self, *args):
        for x in args:
            self.value *= x
        return self

    def divide(self, *args, integer_divide=False):
        for x in args:
            if integer_divide:
                self.value //= x
            else:
                self.value /= x
        return self

    def subtract(self, *args):
        self.value -= sum(args)
        return self

    def __repr__(self):
        return self.value

    def __str__(self):
        return str(self.value)


if __name__ == '__main__':
    calculator = Calculator(4)
    print(calculator)
    print('power:', calculator.power(-2))
