### 我们每次取到的 request 对象是同一个吗

在真实线上的项目中，web 服务器一般会自动开启多个线程来保证代码的执行效率  
不同线程实例化的 request 对象自然是不一样的  
flask 如何让我们获取 request 对象，最终拿到的是不同的对象  
我们取 request 对象时，flask 并不是直接返回 request 对象给我们，而是以当前线程名字为 key 值，获取对应的 request 对象