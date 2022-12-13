import socket
import threading 
import datetime as dt
import ssl
import pprint
import binascii
from pyDes import des,CBC,PAD_PKCS5
# from io import BytesIO



# des-cbc加密
def des_encrypt(s, key='yzw12345'):
    secret_key = key
    iv = '12345678'      # 偏移量8位
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(s, padmode=PAD_PKCS5)
    return binascii.b2a_hex(en)

# des-cbc解密
def des_descrypt(s, key):
    secret_key = key
    iv = '12345678'      # 偏移量8位
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
    return de

# 从记录文本中读取信息
def read_record():
    password=input('请输入聊天记录密码\n')
   
    fp= open('record.txt','rb')
    record=fp.read()
            # print(type(record))
            # print(record)
    record=des_descrypt(s=record,key=password)
    record=str(record)
    print(record[2:len(record)-1])
    fp.close()



# 将聊天信息加密写入记录文本      
def write_record(s):
    fp=open('record.txt','rb')
    old_s=fp.read()
    
    old_s=des_descrypt(old_s,'yzw12345')
   
    
    old_s=str(old_s)
  
    s=old_s[2:len(old_s)-1]+'\n'+s
    fp.close()
    fp=open('record.txt','wb')
  
    es=des_encrypt(s=s)
       
    fp.write(es)
    fp.close()



# 与服务器建立双向验证的连接
def sslConnect(serverIP,dPort):
    severname=serverIP
    serverPort=dPort
    
    # 创建一个ssl上下文，参数表示双方支持最高协议版本
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    
    
    # 该ssl需要对方提供证书
    context.verify_mode=ssl.CERT_REQUIRED
    
    # 加载可信根的证书
    context.load_verify_locations('F:/大学四年级/程序设计课程/OpenSSL_TCP/cert/ca.crt')
    
    # 加载自己的证书和私钥
    context.load_cert_chain(certfile='F:/大学四年级/程序设计课程/OpenSSL_TCP/cert/client.crt',keyfile='F:/大学四年级/程序设计课程/OpenSSL_TCP/cert/client.key')
    
    # 创建一个套接字
    sock=socket.socket()
    
    # 将套接字与ssl绑定
    sslSocket=context.wrap_socket(sock,server_hostname=serverIP)
    
    sslSocket.connect((serverIP,dPort))
        
    # 打印证书信息
    pprint.pprint(sslSocket.getpeercert())
    
    
    
    print('已与服务器接通，请开始聊天')
    return sslSocket


# 接受服务器的信息

def rcvInfo(sslSocket):
    
    if(sslSocket==False):
        return False
    else :
        while True:
          
              
                info=sslSocket.recv(1024).decode()
                if info=='exit':
                    print('服务器断开连接')
                    sslSocket.close()
                    exit()
                    break
                
                elif len(info)>0:
                    # print(1)
                    nowtime=dt.datetime.now().strftime('%F %T')
                    # print(2)
                    info='[server at'+nowtime+']'+info
                    # print(3)
                    print(info)
                    # info=des_encrypt(s=info)
                    # print(4)
                    write_record(info)
                    
          
        return True

# 向服务器发送信息
def sendInfo(sslSocket,serverIP):
    if(sslSocket==False):
        return False
    else:
        # print("请开始你的聊天")
        while True:
            sentence=''
            sentence=input('')
            if len(sentence)>0:
                sslSocket.send(sentence.encode())
                if sentence=='exit':
                    exit()
                elif sentence=='read':
                    read_record()
                else:
                    nowtime=dt.datetime.now().strftime('%F %T')
                    sentence='[client at'+nowtime+']'+sentence
                    write_record(s=sentence)
                
                
if __name__ =='__main__':
    
    s='record\n'
    s=des_encrypt(s)
    fp=open('record.txt','wb')
    fp.write(s)
    fp.close()
    
    serverIP='127.0.0.1'
    serverPort=int(12000)
    
    
    
    sslSocket=sslConnect(serverIP=serverIP,dPort=serverPort)
    # print(sslSocket)
    client1_threading = threading.Thread(target=rcvInfo, args=(sslSocket,))
    client1_threading.start()
    client2_threading = threading.Thread(target=sendInfo, args=(sslSocket,serverIP,))
    client2_threading.start()
    
            
                        
                
    
    
    






 


# 循环阻塞式地从socket中读取数据，必须放在一个独立的线程中，
# 否则，就没办法实现用户能够同时输入消息和程序实时打印接收到的消息
# class ReceivingThread(Thread):
#     def __init__(self):
#         super().__init__()

#     def run(self):
#         while True:  # 不停地读取TCP套接字的信息
#             receiveSentence = clientSocket.recv(1024)
#             if len(receiveSentence) > 0:    # 客户端收到的服务器端的信息长度大于0，则将信息输出到控制台
#             #    # 返回的句子长度为0，说明对端已close
#              #   clientSocket.close()
#              #   return
#                 print( receiveSentence.decode())


# # 开启上面定义的线程
# receivingThread = ReceivingThread()
# receivingThread.start()
# print('Please enjoy yourself')
# while True:
#     sentence = input()
    
#     clientSocket.send(sentence.encode())  #客户端实现信息的发送
#     if sentence=='exit': #客户端实现主动关闭连接
#         clientSocket.close()
#         print("exit!")
#         exit()
