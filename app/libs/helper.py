# encoding: utf-8
"""
Created by Vic on 2018/5/19 14:17
"""


def is_isbn_or_key(word):
    """
    判断关键字是书名还是 isbn 码
    """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
