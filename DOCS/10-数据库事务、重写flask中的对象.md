class BaseQuery(object):
    pass### 如何快捷地拿到当前登录用户的信息

关键对象：`current_user`  
该对象由 flask-login 插件提供，本质上是 User 模型的一个实例

### 事务（同时操作多张表时，要保证一荣俱荣，一损俱损）

在执行数据库操作的时候一定要捕获错误，并且在出现异常的时候进行回滚

### 数据库操作封装

1. 定义类继承 `AQLAlchemy` 类  
2. 在这个类里面定义一个操作数据库的方法  
3. 这个方法需要用 `contextmanager` 来装饰成为一个上下文管理器  
4. 有了这个上下文管理器，就可以在执行真正的数据库操作的前后自动做一些事情  

```python
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy

class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield 
            self.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
            
db = SQLAlchemy()            
```

### 数据模型的创建时间如何处理

`create_time`是定义在模型的基类中的  
不能够使用 default 给这个字段默认时间（这样会导致时间都是一致的）  
使用构造方法给 create_time 赋值就好了  

```python
from datetime import datetime

class Base(db.Model):
    create_time = Colume('create_time', Integer)
    
    def __init__(self):
        self.create_time = int(datetime.now().timestamp())
    
    # 取时间时要用这个属性，方便格式化 （xx.create_datetime.strftime('%Y-%m-%d')）    
    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None
```

### 判断用户是否登录

`current_user.is_authenticated`

### 如何优雅地在每次查询时默认加上 `status=1`

status 我软删除的控制字段，大多数时候我们都只需要查询没有被删除（即status=1）的数据  
所以我们要重写 filter_by 方法：  
1. 定义 Query 类，继承 flask-sqlalchemy 的 BaseQuery 类
2. 定义我们自己的 filter_by  
3. 替换原有的 BaseQuery  

```python
# Base 类所在的模块中
class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        return super(Query, self).filter_by(**kwargs)

# 替换原来的 Query 对象        
db = SQLAlchemy(query_class=Query)
```