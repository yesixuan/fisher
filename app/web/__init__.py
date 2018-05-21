# encoding: utf-8
"""
Created by Vic on 2018/5/20 21:12
"""
from flask import Blueprint

web = Blueprint('web', __name__)
from app.web import book
# from app.web import user
