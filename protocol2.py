from  phe import  paillier
import  random
import GM
def protocol2():
    public_key, private_key = paillier.generate_paillier_keypair()
    c = 0
    m = [0,1]
    r = random.choice(m)
    p, q, R = 232312311797, 971179711797, 17
    alice = GM.Alice(p, q, R)
    bob = GM.Bob(R, p * q)
    rr1 = bob.Ec(str(r))
    cc1 = bob.Ec(str(c))
    temp1 = GM.testTong(cc1,rr1 , p * q)
    t = alice.Dc(temp1)
    if t[0] == "0":
        temp2 = public_key.encrypt(0)
    else :
        temp2 = public_key.encrypt(1)
    #A得到第二次加密方案后的密文
    if r == 0 :
        cc2 = temp2
    else:
        cc2 = public_key.encrypt(1) - temp2
    print(private_key.decrypt(cc2))

protocol2()