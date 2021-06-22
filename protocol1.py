from phe import paillier
import protocol7 as p7
import numpy as np
import random
def protocol1(enA,l,public_key, private_key):
    #enA = [public_key.encrypt(x) for x in a]
    k = len(enA)
    maxx = enA[0]
    """for index, x in enumerate(enA):
        if index == k - 1:
            enA[index] = maxx
        else:
            enA[index] = enA[index + 1]"""

    m_number = 0
    dot_x = []
    for index,x in enumerate(enA):
        b = p7.protocol7(private_key.decrypt(maxx),private_key.decrypt(x),public_key, private_key)
        print("当前最大值"+str(private_key.decrypt(maxx))+"与值"+str(private_key.decrypt(x)))
        print("比较结果为"+str(b))
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
            print(m_number)
        else:
            vv = mm
            print(m_number)
        g=1
        gg = public_key.encrypt(g)
        maxx = vv + (bb_int - gg) * r - bb_int * s

        #print(b_int)
        #print("r:"+str(r),"s:"+str(s),"m:"+str(private_key.decrypt(mm)),"a:"+str(private_key.decrypt(aa)))
        dot_x.append(private_key.decrypt(x))
    #print(dot_x)
    #indexmax = dot_x[k-1]
    #print(indexmax)
    #print("最终最大值位置："+str(m_number))
    i = k
    """while k-2>=0:
        dot_x[k-1] = dot_x[k-2]
        k = k-1
    dot_x[0] = indexmax"""
    print("点积和为："+str(dot_x))
    #print("最大值为："+str(indexmax))
    location = (m_number + 1)
    return location
#public_key, private_key = paillier.generate_paillier_keypair()
#a= [1856, 1742, 2022, 1356,2023]
#protocol1(a,11,public_key, private_key)


