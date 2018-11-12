### 1 Python的函数参数传递
```
a= 3

def func():
    a = 4

func()
print(a)
```

```
a= 3

def func():
    global a
    a = 4

func()
print(a)
```

```
a= []

def func():
    a.append(4)

func()
print(a)
```
可变类型和不可变类型；数字、字符串、元组是不可变的，列表、字典是可变的。