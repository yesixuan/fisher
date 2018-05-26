# encoding: utf-8
"""
Created by Vic on 2018/5/26 09:06
"""
from sqlalchemy import Column, Integer, String, Boolean, Float
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login_manager
from app.models.base import Base


class User(UserMixin, Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    _password = Column('password', String(128), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(50))

    @property  # getter
    def password(self):
        return self._password

    @password.setter  # setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    """明文密码与数据库中的加密密码对比"""
    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    """ 
    login_user 需要知道将 user 中的哪个字段存储在 cookie 中。（函数名是指定的）
    还有其他函数需要在 user 中定义，但我们也可以选择继承 user_login 的 UserMixin 类，从而使用 UserMixin 中的默认方法
    如果你想将 user 中的其他字段存到 cookie 中，还是需要重写 get_id 方法的
    """
    # def get_id(self):
    #     return self.id


@login_manager.user_loader
def get_user(uid):
    # 根据主键查询 model 是不需要用 filter_by 的
    return User.query.get(int(uid))
