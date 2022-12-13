import socket
import threading 
import datetime as dt
import ssl
import pprint



        
    

# 向客户端发送信息
def sendInfo(sslSocket):
    while True:
            info=''
            info=input()
            if len(info)>0:
                sslSocket.send(info.encode())
                if info=='exit':
                    print('已断开连接')
                    exit()
            
      

    

if __name__ =='__main__':
    
    
    
    # 创建一个ssl上下文，参数表示双方支持最高协议版本
    
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    
    # 该ssl需要对方提供证书
    
    context.verify_mode=ssl.CERT_REQUIRED
    
    # 加载可信根的证书
    
    context.load_verify_locations('F:/大学四年级/程序设计课程/代码/cert/ca.crt')
    
    # 加载自己的证书和私钥
    
    context.load_cert_chain(certfile='F:/大学四年级/程序设计课程/代码/cert/server.crt',keyfile='F:/大学四年级/程序设计课程/代码/cert/server.key')
   
    # 创建一个套接字
    sock=socket.socket()
    sock.bind(('127.0.0.1',12000))
    sock.listen(1)
    
    
    sock,address=sock.accept()
    # 将套接字与ssl绑定
    sslSocket=context.wrap_socket(sock,server_side=True)
    print('服务器已就绪')
    
    
    # 打印客户端证书
    pprint.pprint(sslSocket.getpeercert())
    print('已与客户端接通，可以开始通信')
  

    
    
    server1_threading = threading.Thread(target=sendInfo, args=(sslSocket,))
    server1_threading.start()    
    
    # 接受客户端信息
    while True:
        info=''
        info=sslSocket.recv(1024).decode()
        if len(info)>0:
            nowTime=dt.datetime.now().strftime('%F %T')
            print('[client'+' at'+nowTime+']'+info)
        elif info=='exit':
            sslSocket.close()
            exit()







