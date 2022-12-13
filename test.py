import binascii
from pyDes import des,CBC,PAD_PKCS5


def des_encrypt(s, key='yzw12345'):
    secret_key = key
    iv = '12345678'      # 偏移量8位
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(s, padmode=PAD_PKCS5)
    return binascii.b2a_hex(en)


def des_descrypt(s, key):
    secret_key = key
    iv = '12345678'      # 偏移量8位
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
    return de

def read_record():
    password='yzw12345'
   
    fp= open('record.txt','rb')
    record=fp.read()
            # print(type(record))
            # print(record)
    record=des_descrypt(s=record,key=password)
    print(record)
    fp.close()

        
def write_record(s):
    fp=open('record.txt','rb')
    old_s=fp.read()
    old_s=des_descrypt(old_s,'yzw12345')
    old_s=str(old_s)
    s=s+old_s[2:len(old_s)-1]
    fp.close()
    fp=open('record.txt','wb')
        # print(s)
    es=des_encrypt(s=s)
        # print(type(es))
        # bytes_io=BytesIO(es)
    fp.write(es)
    fp.close()


while True:
    s=input(':')
    if(s=='exit'):
        exit()
        
    write_record(s)
    read_record()