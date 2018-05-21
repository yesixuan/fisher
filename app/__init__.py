# encoding: utf-8
"""
Created by Vic on 2018/5/20 21:08
"""
from flask import Flask


def create_app():
    app = Flask(__name__)
    # 拆分配置文件
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)
    return app


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
