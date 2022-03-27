class Stack:
    def __init__(self, string_to_expect):
        self.string = string_to_expect
        self.result_list = list(self.string)
        self.symbols = {"(": ")", "[": "]", "{": "}"}
        self.list = []

    def is_empty(self):
        if len(self.result_list) > 0:
            return True
        else:
            return False

    def push(self, elem):
        self.result_list.append(elem)

    def pop(self):
        pop_elem = self.result_list.pop()
        return pop_elem

    def peek(self):
        second_elem = self.result_list[-1]
        return second_elem

    def size(self):
        return len(self.result_list)

    def check_balance(self):
        while self.is_empty():
            if self.size() % 2:
                return "Не сбалансированно"
            else:
                while self.result_list:
                    if self.peek() in self.symbols.keys():
                        if self.symbols[self.peek()] in self.list:
                            self.list.remove(self.symbols[self.pop()])
                        else:
                            return "Не сбалансированно"
                    elif self.peek() in self.symbols.values():
                        self.list.append(self.pop())
                return "Сбалансированно"
        return "Не сбалансированно"

examp = ["(((([{}]))))", "[([])((([[[]]])))]{()}", "{{[()]}}", "}{}", "{{[(])]}}", "[[{())}]", ""]

for any_examp in examp:
    test = Stack(any_examp)
    print(test.check_balance())

