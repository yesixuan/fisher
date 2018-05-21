# encoding: utf-8
"""
Created by Vic on 2018/5/20 19:30
"""
from app.libs.httper import HTTP
from flask import current_app  # 从 flask 中获取当前 app


class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    """
    类方法中用类变量 cls.类方法，也可以使用 类名.类方法，但不推荐
    """

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        url = cls.keyword_url.format(keyword, current_app.config['PER_PAGE'], cls.calculate_start(page))
        result = HTTP.get(url)
        return result

    @staticmethod
    def calculate_start(page):
        return (page - 1) * current_app.config['PER_PAGE']
