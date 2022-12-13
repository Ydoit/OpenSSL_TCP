# 简单（丑陋）实现基于`OpenSSL`的安全聊天系统

* 点对点
* 基于`openssl`的安全套接字通信
* 客户端服务器双向验证
* 聊天记录本地加密，输入正确口令查看

* `openssl`需要安装`pyOpenSSL`

``pip install pyOpenSSl``

* `DES-CBC`加密 需要安装`pycryptodome`

``pip install pycrytodome``

* `CA、client、server`的证书生成过程

`CA`私钥生成（注意将所有私钥生成`1024`位改成`2048`位）

![1生成ca密钥](证书生成图/1生成ca密钥.png)

`CA`请求文件生成

![2生成ca请求](证书生成图/2生成ca请求.png)

`CA`证书生成

![3生成ca证书](证书生成图/3生成ca证书.png)

`server`私钥生成

![4生成服务器密钥](证书生成图/4生成服务器密钥.png)

`server`请求文件生成

![5生成服务器请求](证书生成图/5生成服务器请求.png)

`server`证书生成

![6生成服务器证书](证书生成图/6生成服务器证书.png)

`client`私钥生成

![7生成客户端的密钥](证书生成图/7生成客户端的密钥.png)

`client`请求文件生成

![8生成客户端请求](证书生成图/8生成客户端请求.png)

`client`证书生成

![9生成客户端证书](证书生成图/9生成客户端证书.png)

* 先运行`tcpserver.py`，再运行`tcpclient.py`就可以进行通信
* 任意一方输入`exit`结束通信
* `client`输入`read`读取本地聊天
* ~~程序鲁棒性~~(**课设要啥鲁棒性`bushi`**)
* ~~聊天记录可读性~~（**课设要啥可读`bushi`**）



