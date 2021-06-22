import paillierself
import protocol7 as p7
import numpy as np
import random
import time
def protocol1(enA,l):
    start = time.perf_counter()
    n,public_key, private_key = paillierself.generate_paillier_keypair()
    enA = [public_key.encrypt(x) for x in enA]
    k = len(enA)
    ena = enA[0]
    for index,x in enumerate(enA):
        if index == k - 1:
            enA[index] = ena
        else:
            enA[index] = enA[index+1]
    print("数组加密值：")
    for x in enA:
        x_raw = private_key.decrypt(x)
        print("密文："+str(public_key.raw_encrypt(x_raw)))
    maxx = enA[0]
    m_number = 0
    for index,x in enumerate(enA):
        b = p7.protocol7(private_key.decrypt(maxx),private_key.decrypt(x),public_key, private_key)
        r = random.randint(1, 2 ** l)
        s = random.randint(1, 2 ** l)
        rr = public_key.encrypt(r)
        ss = public_key.encrypt(s)
        mm = np.add(maxx,rr)
        aa = np.add(x,ss)
        b_int = int (b[0])
        bb_int = public_key.encrypt(b_int)
        if b_int:
            m_number = index
            vv = aa
        else:
            vv = mm
        g=1
        gg = public_key.encrypt(g)
        maxx = vv + (bb_int - gg) * r - bb_int * s
        #print(b_int)
        #print("r:"+str(r),"s:"+str(s),"m:"+str(private_key.decrypt(mm)),"a:"+str(private_key.decrypt(aa)))
        #print(private_key.decrypt(x))
        location = (m_number + 1) % k + 1
    end = time.perf_counter()
    print("运行时间：" + str(end - start) + "秒")
    return location
#public_key, private_key = paillier.generate_paillier_keypair()
#a= [1856, 1742, 2022, 1356,2023]
#print(protocol1(a,11))