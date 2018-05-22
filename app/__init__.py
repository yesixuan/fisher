# encoding: utf-8
"""
Created by Vic on 2018/5/20 21:08
"""
from flask import Flask
from app.models.book import db


def create_app():
    app = Flask(__name__)
    # 拆分配置文件
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    db.init_app(app)  # sqlalchemy 与 flask 核心对象关联
    db.create_all(app=app)
    return app


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
