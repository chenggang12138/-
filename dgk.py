
import random
def dgk(a,b,p1, p2):      #a<=b
    ka = a.bit_length()
    kb = b.bit_length()
    if ka != kb:
        if ka > kb :
            return  0
        else:
            return  1

    else:
        i,j,k= 0,0,0
        ai,bi,ci_en,wi_en = {},{},{},{}
        while i<ka :
            ai[i] = int(a % 2)
            bi[i] = int(b % 2)
            a = a / 2
            b = b / 2
            if ai[i] == 0:         #A计算，B发送加密给A
                wi_en[i] = p1.encrypt(bi[i])
            else:
                wi_en[i] = p1.encrypt(1) - p1.encrypt(bi[i])
            i = i+1
        rA = random.randint(0, 1)
        rB = 0
        #print(rA)
        s = 1 - 2 * rA
        s_en = p1.encrypt(s)
        while j<ka :
            t = j + 1
            temp = 0
            while t <= ka -1 :
                temp =  temp + wi_en[t]
                t =t+1
            temp = temp * 3
            ci_en[j] = p1.encrypt(s) + p1.encrypt(ai[j]) - p1.encrypt(bi[j]) + temp
            ci_en[j] = ci_en[j] * 2
            j =j+1
        while k<ka:
            if p2.decrypt(ci_en[k]) == 0:
                rB = 1
                if rA == 1:
                    return 0
                else:
                    return 1
            k = k+1
        return rA



    #print(ai,bi)

