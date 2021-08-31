# Simple-Stack-VM

一个简单的栈式虚拟机

## 当前支持的指令

1. `PUSH`
2. `POP`
3. `ADD`
4. `SUB`
5. `MUL`
6. `DIV`
7. `EQ`
8. `GT`
9. `LT`
10. `AND`
11. `OR`
12. `NOT`
13. `XOR`

## 使用方法

```python3
simple_vm = SimpleVM() # 初始化一个 VM
simple_vm.code = [
    # 指令放在这里
]
res = simple_vm.run() # 运行指令, 如果有输出, 会赋值给 res 变量
```

举个栗子, 计算 `(1 + 2) * (3 - 4)` 的值:

```python3
simple_vm = SimpleVM()
simple_vm.code = [
    "PUSH", 1, # [1]
    "PUSH", 2, # [1, 2]
    "ADD",     # [3]
    "PUSH", 3, # [3, 3]
    "PUSH", 4, # [3, 3, 4]
    "SUB",     # [3, -1]
    "MUL",     # [-3]
    "POP",     # []
]
res = simple_vm.run()
```
然后 `res` 的值就是 `-3` 啦
