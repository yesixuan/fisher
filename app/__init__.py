# encoding: utf-8
"""
Created by Vic on 2018/5/20 21:08
"""
from flask import Flask
from flask_login import LoginManager
from app.models.book import db

login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    # 拆分配置文件
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    db.init_app(app)  # sqlalchemy 与 flask 核心对象关联
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'
    db.create_all(app=app)
    return app


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
