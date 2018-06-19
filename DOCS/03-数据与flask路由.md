### 如何构造一个 response 对象

关键词：`make_response`（flask 中的一个方法）  
意义：response 信息太多，揉搓在一起不好处理，通过上述方法得到的 response 对象可以通过打点的方式来动态添加 response 信息

### 函数为什么不能写得又臭又长（承载太多功能）

单一职责，一个职责对应一个函数，每个函数就是最好的自注释  
将许多细节都暴露在一个函数中就是强迫读你代码的人来了解你代码的细节，这样特别不人道

### python 中的三元表达式

`{} if return_json else ''`

### python 中的模板字符串

```python
'呵呵{}'.format('haha')
```

### 怎样快速返回 JSON 数据（jsonify）

```python
jsonify(result)
# 等价于下面的
json.dumps(result), 200, {'content-type': 'application/json'}
```

### flask 中的URL与视图函数是如何对应起来的

flask 核心对象中有一个 url_map 对象存储 url 与 endpoint 对应关系，然后有一个 eiew_functions 对象存储 endpoint 与 视图函数 的对应关系。

### 循环引用如何分析

1. 所有 Python 文件都只会被导入运行一次
2. 入口文件除了初始运行一次，还可以被导入一次
3. 被导入的文件执行完之后将回到导入文件继续执行  

