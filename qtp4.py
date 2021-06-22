import paillierself
import protocol3 as p3
import protocol1 as p1
import time
def protocol4(x,w):
    start = time.perf_counter()
    n, public_key, private_key = paillierself.generate_paillier_keypair()
    v=[]
    #x =  [1,2,3]
    #w = [[10,20,30],[14,25,26],[17,16,29]]
    k = len(w)
    i = 0
    while i<k:
        temp =  p3.protocol3(x,w[i],public_key, private_key)
        i = i+1
        #print(private_key.decrypt(temp))
        v.append(temp)
    print("点积和密文值：")
    for x in v:
        x_raw = private_key.decrypt(x)
        print("密文："+str(public_key.raw_encrypt(x_raw)))
        print("明文："+str(x_raw))
    re = p1.protocol1(v,40,public_key, private_key)
    end = time.perf_counter()
    print("运行时间：" + str(end - start) + "秒")
    return  re
