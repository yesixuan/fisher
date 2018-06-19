### 由一个经典错误`Working outside of application context`引发的血案

flask 中维护着两个栈`_app_ctx_stack`(存放AppContext)与`_request_ctx_stack`(存放Request Context)  
当一个请求进入，一个 request 上下文就就会被压入它的栈（在这之前它会先做下面这件事）  
检查`_app_ctx_stack`中有没有 app 上下文，如果没有就推一个进去  
综上所述，request 对象与 app 核心对象都需要在请求上下文中间使用，否则就会爆出标题上的经典错误  

### 能否手动将 app 核心对象推入到`_app_ctx_stack`栈中

```python
"""方法一"""
ctx = app.app_context()
ctx.push()
# 此时可以开心地访问 current_app 对象了

"""方法二"""
with app.app_context():
    # do something
```