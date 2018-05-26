# encoding: utf-8
"""
Created by Vic on 2018/5/26 11:17
"""
from wtforms import Form, StringField, IntegerField, PasswordField
from wtforms.validators import Length, NumberRange, DataRequired, Email, ValidationError
from app.models.user import User


class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='电子邮箱格式不正确')])

    password = PasswordField(validators=[DataRequired(message='密码不能为空'), Length(6, 32)])

    nickname = StringField(validators=[DataRequired(), Length(2, 10, message='昵称为 2 ~ 10 位')])

    """自定义校验规则，不需要再将验证函数放到验证列表中，wtforms 可以识别这个命名"""
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已被注册')


class LoginForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='电子邮箱格式不正确')])

    password = PasswordField(validators=[DataRequired(message='密码不能为空'), Length(6, 32)])