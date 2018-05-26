# encoding: utf-8
"""
Created by Vic on 2018/5/26 09:08
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, SmallInteger

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True  # Base 这个类直接继承 db.Model 的话会尝试给这个数据表创建主键，加这个就不会报错
    # create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)  # 软删除

    """
    定义这个方法是因为数据表字段跟前端提交的数据大都一一对应，一个一个从 request 中取数据实例化 model 太傻了
    """

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)  # 动态添加属性
