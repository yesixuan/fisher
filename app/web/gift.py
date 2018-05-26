from . import web
from flask_login import login_required  # 权限控制装饰器


@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'my gifts'


@web.route('/gifts/book/<isbn>')
def save_to_gifts(isbn):
    pass


@web.route('/gift/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
