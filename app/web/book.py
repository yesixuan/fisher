# encoding: utf-8
"""
Created by Vic on 2018/5/20 20:27
"""
from flask import jsonify, request
from . import web

from helper import is_isbn_or_key
from yushu_book import YuShuBook


@web.route('/book/search')
def search():
    q = request.args['q']
    page = request.args['page']
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q, page)
    # dict 序列化
    return jsonify(result)

