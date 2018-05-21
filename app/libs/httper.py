# encoding: utf-8
"""
Created by Vic on 2018/5/19 14:26
"""
import requests


class HTTP:
    """
    1. 静态方法可以通过类名.方法名来调取
    2. 没有用到类变量，所以不推荐使用 classmethod
    """
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
