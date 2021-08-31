#!/usr/bin/env python3

from VM import SimpleVM

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
