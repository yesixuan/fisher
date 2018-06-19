### 路由的另一种注册方式

关键词：`add_url_rule`  
装饰器路由的方式是通过闭包返回了内层函数，并且调用了这个内层函数（顺便将外部参数传入到这个内层函数当中）

### 配置文件如何引用

关键词：`app.config.from_object('config')`（config 是 py 模块的路径）  
读取配置文件：`app.config['DEBUG']``(配置文件中的变量名必须为全大写)

### `if __name__ == '__main__'`在 flask 中的意义

生产环境中不用用自带的服务器（用的 nginx + uwsgi）  
生产环境中，入口文件不再是 `fisher.py`，`fisher.py` 只是一个由 uwsgi 引用的一个模块。







