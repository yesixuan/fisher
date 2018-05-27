# encoding: utf-8
"""
Created by Vic on 2018/5/26 09:07
"""
from flask import current_app
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, SmallInteger, desc, func
from sqlalchemy.orm import relationship
from app.models.base import Base, db
from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook


class Gift(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('book.id'))
    launched = Column(Boolean, default=False)

    @classmethod
    def get_user_gifts(cls, uid):
        gifts = Gift.query.filter_by(uid=uid, launched=False).order_by(desc(Gift.create_time)).all()
        return gifts

    @classmethod
    def get_wish_counts(cls, isbn_list):
        count_list = db.session.query(
            func.count(Wish.id), Wish.isbn).filter(
            Wish.launched == False, Wish.isbn.in_(isbn_list), Wish.status == 1).group_by(
            Wish.isbn).all()
        count_list = [{'count': w[0], 'isbn': w[1]} for w in count_list]
        return count_list

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    @classmethod
    def recent(cls):
        # 要先分组才能去重
        recent_gift = Gift.query.filter_by(
            launched=False).group_by(
            Gift.id).order_by(  # 这里本来该用 isbn 但是会报错，没有解决
            Gift.create_time).limit(
            current_app.config['RECENT_BOOK_COUNT']).distinct().all()
        return recent_gift
