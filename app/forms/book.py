# encoding: utf-8
"""
Created by Vic on 2018/5/21 09:12
"""
from wtforms import Form, StringField
from wtforms.validators import Length


class SearchForm(Form):
    q = StringField(validators=[Length(min=1, max=30)])
