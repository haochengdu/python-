### 1-Python的函数参数传递
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
### 2-写出A0，A1至An的最终值
```
A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
A1 = range(10)
A2 = [i for i in A1 if i in A0]
A3 = [A0[s] for s in A0]
A4 = [i for i in A1 if i in A3]
A5 = {i: i * i for i in A1}
A6 = [[i, i * i] for i in A1]
```

### 3-以下代码运行结果是什么？
```
l = []
for i in range(10):
    l.append({'num': i})
print(l)

l = []
a = {'num': 0}
for i in range(10):
    a['num'] = i
    l.append(a)
print(l)
```

### 4-4G内存怎么读取一个5G的数据？
方法一：可以通过生成器，分多次读取，每次读取数量相对少的数据（比如500MB）进行处理，处理结束后
在读取后面的 500MB的数据。
```
def read_in_chunks(file_path, chunk_size=1024 * 1024):
    """
    Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1M
    You can set your own chunk size
    """
    with open(file_path, 'rb') as f:
        while True:
            chunk_data = f.read(chunk_size)
            if not chunk_data:
                break
            yield chunk_data


with open('new_file.jpg', 'wb') as f:
    for chunk in read_in_chunks('./fire_test_000491.jpg'):
        f.write(chunk)
```

### 5-2赋值、浅拷贝和深拷贝的区别？
1、赋值：在Python中，对象的赋值就是简单的对象引用。
```
a = [1,2,"hello",['python', 'C++']]
b = a
```
在上述情况下，a和b是一样的，他们指向同一片内存，b不过是a的别名，是引用。  
我们可以使用b is a 去判断，返回True，表明他们地址相同，内容相同，也可以使用id()函数来查看两个列表的地址是否相同。  
赋值操作(包括对象作为参数、返回值)不会开辟新的内存空间，它只是复制了对象的引用。也就是
说除了b这个名字之外，没有其他的内存开销。修改了a，也就影响了b，同理，修改了b，也就影响
了a。  

2、浅拷贝(shallow copy)  
浅拷贝会创建新对象，其内容非原对象本身的引用，而是原对象内第一层对象的引用。  
浅拷贝有三种形式:切片操作、工厂函数、copy模块中的copy函数。  
比如上述的列表a:  
切片操作：b = a[:] 或者 b = [x for x in a]；  
工厂函数：b = list(a)；  
copy函数：b = copy.copy(a)；  
浅拷贝产生的列表b不再是列表a了，使用is判断可以发现他们不是同一个对象，使用id查看，
他们也不指向同一片内存空间。但是当我们使用id(x) for x in a 和 id(x) for x in b来查看a和b 中元
素的地址时，可以看到二者包含的元素的地址是相同的。  
在这种情况下，列表a和b是不同的对象，修改列表b理论上不会影响到列表a。  
但是要注意的是，浅拷贝之所以称之为浅拷贝，是它仅仅只拷贝了一层，在列表a中有一个嵌套的
list，如果我们修改了它，情况就不一样了。  
比如：a[3].append('java')。查看列表b，会发现列表b也发生了变化，这是因为，我们修改了嵌
套的list，修改外层元素，会修改它的引用，让它们指向别的位置，修改嵌套列表中的元素，列表的地
址并未发生变化，指向的都是用一个位置。  

3、深拷贝(deep copy)  
深拷贝只有一种形式，copy模块中的deepcopy()函数。  
深拷贝和浅拷贝对应，深拷贝拷贝了对象的所有元素，包括多层嵌套的元素。因此，它的时间和空
间开销要高。  
同样的对列表a，如果使用 b = copy.deepcopy(a)，再修改列表b将不会影响到列表a，即使嵌
套的列表具有更深的层次，也不会产生任何影响，因为深拷贝拷贝出来的对象根本就是一个全新的对象，
不再与原来的对象有任何的关联。  

4、拷贝的注意点？
对于非容器类型，如数字、字符，以及其他的“原子”类型(即不可变类型)，没有拷贝一说，产生的都是原对象的
引用。  

### 6- 类中__init__ 和__new__的区别？
init在对象创建后，对对象进行初始化。  
new是在对象创建之前创建一个对象，并将该对象返回给init。  

### 7- 单例，只初始化一次
```
class ConfigFileHandler(object):
    __instance = None
    __first_init = False

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, *args, **kwargs):
        if not ConfigFileHandler.__first_init:
            # 对实例对象的初始化操作
            ConfigFileHandler.__first_init = True
```

### 8- 排序
1、字典排序  
现有字典 d = {'a': 24, 'g': 52, 'i': 12, 'k': 33}请按字典中的 value值进行排序？  
```
sorted(d.items(), key=lambda x:x[1])
```
2、sort和sorted的区别  
```
In [104]: list_test = [1,22,55,32,2,0]

In [105]: list_test
Out[105]: [1, 22, 55, 32, 2, 0]

In [106]: list_test.sort()

In [107]: list_test
Out[107]: [0, 1, 2, 22, 32, 55]

In [108]: list_test2 = [1,22,55,32,2,0]

In [109]: sorted(list_test2)
Out[109]: [0, 1, 2, 22, 32, 55]

In [110]: list_test2
Out[110]: [1, 22, 55, 32, 2, 0]

```
sort 会对变量进行修改  
sorted不会修改原来的变量  

3、对列表 list_test = [{'name': 'aa', 'age': 11}, {'name': 'bb', 'age': 22}, {'name': 'cc', 'age': 10}, {'name': 'dd', 'age': 5}] 
按age由大到小进行排序
```
In [113]: list_test3
Out[113]: 
[{'age': 11, 'name': 'aa'},
 {'age': 22, 'name': 'bb'},
 {'age': 10, 'name': 'cc'},
 {'age': 5, 'name': 'dd'}]

In [114]: list_test3.sort(key=lambda x:x['age'], reverse=True)

In [115]: list_test3
Out[115]: 
[{'age': 22, 'name': 'bb'},
 {'age': 11, 'name': 'aa'},
 {'age': 10, 'name': 'cc'},
 {'age': 5, 'name': 'dd'}]
```
### 9- 字典推导式
d = {key: value for (key, value) in iterable}
d = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))






