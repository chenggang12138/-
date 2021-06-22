from phe import paillier
def protocol3(x,y,public_key, private_key):
    v = 0
    vv = public_key.encrypt(v)
    yy = [public_key.encrypt(i) for i in y]
    for index,i in enumerate(yy) :
        vv = vv + i * x[index]
    #print(private_key.decrypt(vv))
    #v = private_key.decrypt(vv)
    return  vv

#x = [1,2,3,4]
#y = [4,5,6,7]
#protocol3(x,y)