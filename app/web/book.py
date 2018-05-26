# encoding: utf-8
"""
Created by Vic on 2018/5/20 20:27
"""
import json

from flask import jsonify, request, render_template, flash

from app.forms.book import SearchForm
from . import web

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookCollection, BookViewModel


@web.route('/book/search')
def search():
    # 实力化 wtforms 对象，还需要调用该对象的 validate 方法才能真正实施调用
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        """
            通过 wtforms 取得表单数据而不是通过 request.args
            这样才能取到 wtforms 中定义的默认值
        """
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q)

        # dict 序列化
        books.fill(yushu_book, q)
        # return json.dumps(books, default=lambda o: o.__dict__)
    else:
        flash('搜索关键字不符合要求，请重新输入！')
        return jsonify(form.errors)

    return render_template('search_result.html', books=books)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)
    return render_template('book_detail.html', book=book, wishes=[], gifts=[])

