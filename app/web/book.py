# encoding: utf-8
"""
Created by Vic on 2018/5/20 20:27
"""
from flask import jsonify, request

from app.forms.book import SearchForm
from . import web

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookViewModel


@web.route('/book/search')
def search():
    # 实力化 wtforms 对象，还需要调用该对象的 validate 方法才能真正实施调用
    form = SearchForm(request.args)
    if form.validate():
        """
            通过 wtforms 取得表单数据而不是通过 request.args
            这样才能取到 wtforms 中定义的默认值
        """
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
            # 通过 viewModel 层，对数据进行处理
            result = BookViewModel.package_single(result, q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
            result = BookViewModel.package_collection(result, q)
        # dict 序列化
        return jsonify(result)
    else:
        return jsonify(form.errors)
