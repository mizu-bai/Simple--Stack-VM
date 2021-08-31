class SimpleVM():
    def __init__(self):
        self.stack = []
        self.operations = {
            "PUSH": self.op_push,
            "POP":  self.op_pop,
            "ADD":  self.op_add,
            "SUB":  self.op_sub,
            "MUL":  self.op_mul,
            "DIV":  self.op_div,
            "EQ":   self.op_eq,
            "GT":   self.op_gt,
            "LT":   self.op_lt,
            "AND":  self.op_and,
            "OR":   self.op_or,
            "NOT":  self.op_not,
            "XOR":  self.op_xor
        }
        self.code = []

    def op_push(self, x):
        self.stack.append(x)

    def op_pop(self):
        return self.stack.pop()

    def op_add(self):
        t1 = self.stack.pop()
        t2 = self.stack.pop()
        self.op_push(t2 + t1)

    def op_sub(self):
        t1 = self.stack.pop()
        t2 = self.stack.pop()
        self.op_push(t2 - t1)

    def op_mul(self):
        t1 = self.stack.pop()
        t2 = self.stack.pop()
        self.op_push(t2 * t1)

    def op_div(self):
        t1 = self.stack.pop()
        t2 = self.stack.pop()
        self.op_push(t2 // t1)

    def op_eq(self):
        t1 = self.stack.pop()
        t2 = self.stack.pop()
        self.op_push(1 if t2 == t1 else 0)
        
    def op_gt(self):
        t1 = self.stack.pop()
        t2 = self.stack.pop()
        self.op_push(1 if t2 > t1 else 0)

    def op_lt(self):
        t1 = self.stack.pop()
        t2 = self.stack.pop()
        self.op_push(1 if t2 < t1 else 0)

    def op_and(self):
        t1 = self.stack.pop()
        t2 = self.stack.pop()
        self.op_push(t2 & t1)

    def op_or(self):
        t1 = self.stack.pop()
        t2 = self.stack.pop()
        self.op_push(t2 | t1)

    def op_not(self):
        t1 = self.stack.pop()
        self.op_push(~t1)

    def op_xor(self):
        t1 = self.stack.pop()
        t2 = self.stack.pop()
        self.op_push(t2 ^ t1)

    def run(self):
        def shift(l):
            t = l[0]
            l = l[1:]
            return t, l
        
        while self.code:
            t, self.code = shift(self.code)
            if t == "PUSH":
                t2, self.code = shift(self.code)
                self.operations[t](t2)
            elif t == "POP":
                return self.operations[t]()
            else:
                self.operations[t]()

        return None

if __name__ == "__main__":
    simple_vm = SimpleVM()
    # 20!
    simple_vm.code = []
    for i in range(1, 21):
        simple_vm.code += [
            "PUSH", i
        ]
        if i > 1:
            simple_vm.code += [
                "MUL"
            ]
        if i == 20:
            simple_vm.code += [
                "POP"
            ]

    res = simple_vm.run()
    if res:
        print(f"20! = {res}")
