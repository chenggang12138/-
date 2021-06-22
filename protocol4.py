import protocol3 as p3
import protocol1 as p1
import paillierself
def protocol4(x,w,public_key, private_key):
    n, public_key, private_key = paillierself.generate_paillier_keypair()
    v=[]
    k = len(w)
    i = 0
    while i<k:
        temp =  p3.protocol3(x,w[i],public_key, private_key)
        i = i+1
        v.append(temp)
    return  p1.protocol1(v,14,public_key, private_key)

