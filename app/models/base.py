# encoding: utf-8
"""
Created by Vic on 2018/5/26 09:08
"""
from contextlib import contextmanager
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from sqlalchemy import Column, Integer, SmallInteger


class SQLAlchemy(_SQLAlchemy):
    """
    定义一个类，继承 SQLAlchemy 类
    增加一个 auto_commit 的方法，每次需要存储数据，并且出现错误自动回滚的操作
    auto_commit 方法中的核心操作是在 yield 的位置
    真正使用这个 auto_commit 方法是需要借助上下文管理器（with、contextmanager）
    """

    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


class Query(BaseQuery):
    """
    自定义一个 Query 类，继承 BaseQuery
    重写里边的 filter_by 方法
    自动在参数中添加 status=1 这个查询条件
    """

    def filter_by(self, **kwargs):
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        return super(Query, self).filter_by(**kwargs)


# flask-sqlalchemy 允许我们传入自己的查询类
db = SQLAlchemy(query_class=Query)


class Base(db.Model):
    __abstract__ = True  # Base 这个类直接继承 db.Model 的话会尝试给这个数据表创建主键，加这个就不会报错
    create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)  # 软删除

    def __int__(self):
        """自动添加创建时间不能使用 default ，因为 create_time 是类变量，不是实例变量"""
        self.create_time = int(datetime.now().timestamp())

    """
    定义这个方法是因为数据表字段跟前端提交的数据大都一一对应，一个一个从 request 中取数据实例化 model 太傻了
    """

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)  # 动态添加属性

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None
