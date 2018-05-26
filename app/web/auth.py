from . import web
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user
from app.forms.auth import RegisterForm, LoginForm
from app.models.user import User
from app.models.base import db


@web.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attrs(form.data)
        db.session.add(user)
        db.session.commit()
        redirect(url_for('web.login'))
    return render_template('auth/register.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)  # 将用户登录信息写入到 cookie 中，remember 表示持久存储 cookie （365天）
            next = request.args.get('next')  # next 是 flask-login 帮我们加的查询参数
            if not next and not next.startswith('/'):  # 第二个判断是防止别人手动输入 next 参数调到别的地方去了
                next = url_for('web.index')
            return redirect(next)
        else:
            flash('账号不存在或密码错误！')
    return render_template('auth/login.html', form=form)


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    pass
