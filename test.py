# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 16:12:55 2021

@author: Administrator
"""
import random

from phe.util import getprimeover
import numpy

pr = 0


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


'''
扩展欧几里的算法
计算 ax + by = 1中的x与y的整数解（a与b互质）
'''


def ext_gcd(a, b):
    if b == 0:
        x1 = 1
        y1 = 0
        x = x1
        y = y1
        r = a
        return r, x, y
    else:
        r, x1, y1 = ext_gcd(b, a % b)
        x = y1
        y = x1 - a // b * y1
        return r, x, y


def exp_mode(base, exponent, n):
    bin_array = bin(exponent)[2:][::-1]
    r = len(bin_array)
    base_array = []

    pre_base = base
    base_array.append(pre_base)

    for _ in range(r - 1):
        next_base = (pre_base * pre_base) % n
        base_array.append(next_base)
        pre_base = next_base

    a_w_b = __multi(base_array, bin_array, n)
    return a_w_b % n


def __multi(array, bin_array, n):
    result = 1
    for index in range(len(array)):
        a = array[index]
        if not int(bin_array[index]):
            continue
        result *= a
        result = result % n  # 加快连乘的速度
    return result


# 生成公钥私钥，p、q为两个超大质数
def gen_key(p, q):
    n = p * q
    fy = (p - 1) * (q - 1)  # 计算与n互质的整数个数 欧拉函数
    e = 65537  # 选取e   一般选取65537
    # generate d
    a = e
    b = fy
    r, x, y = ext_gcd(a, b)
    # 计算出的x不能是负数，如果是负数，说明p、q、e选取失败，不过可以把x加上fy，使x为正数，才能计算。
    if x < 0:
        x = x + fy
    d = x
    # 返回：   公钥     私钥
    return (n, e), (n, d)


# 加密 m是被加密的信息 加密成为c
def encrypt(m, pubkey):
    n = pubkey[0]
    e = pubkey[1]

    c = exp_mode(m, e, n)
    return c


# 解密 c是密文，解密为明文m
def decrypt(c, selfkey):
    n = selfkey[0]
    d = selfkey[1]

    m = exp_mode(c, d, n)
    return m


# 加密
def encryptming(srcStr, password='1938762450'):
    # 将字符串转换成字节数组
    data = bytearray(srcStr.encode('utf-8'))
    # 把每个字节转换成数字字符串
    strList = [str(byte) for byte in data]
    # 给每个数字字符串前面加一个长度位
    strList = [str(len(s)) + s for s in strList]
    # 进行数字替换
    for index0 in range(len(strList)):
        tempStr = ""
        for index in range(len(strList[index0])):
            tempStr += password[int(strList[index0][index])]
        strList[index0] = tempStr
    return "".join(strList)


# 解密
def decryptming(srcStr, password='1938762450'):
    # 数字替换还原
    tempStr = ""
    for index in range(len(srcStr)):
        tempStr += str(password.find(srcStr[index]))
    # 去掉长度位，还原成字典
    index = 0
    strList = []
    while True:
        # 取长度位
        length = int(tempStr[index])
        # 取数字字符串
        s = tempStr[index + 1:index + 1 + length]
        # 加入到列表中
        strList.append(s)
        # 增加偏移量
        index += 1 + length
        # 退出条件
        if index >= len(tempStr):
            break
    data = bytearray(len(strList))
    for i in range(len(data)):
        data[i] = int(strList[i])
    return data.decode('utf-8')


def xsos(ming):
    p = getprimeover(1024)
    q = getprimeover(1024)
    # global pr
    pr = getprimeover(10)
    print("jiami pr", pr)
    global pubkey, selfkey, fn, l
    pubkey, selfkey = gen_key(p, q)
    '''需要被加密的信息转化成数字，长度小于秘钥n的长度，如果信息长度大于n的长度，那么分段进行加密，分段解密即可。'''
    fn = (p - 1) * (q - 1)
    l = pr * pubkey[0]
    r = random.randint(0, 100)
    k1 = random.randint(0, 100)
    k2 = random.randint(0, 100)
    t1 = random.randint(0, 100)
    t2 = random.randint(0, 100)
    A1 = pubkey[1] + k1 * fn
    A2 = t1 * pubkey[1] + t2 + k2 * fn
    m = int(encryptming(ming, '1938762450'))
    print("待加密信息-->", m)
    '''信息加密，m被加密的信息，c是加密后的信息'''
    u = (m + r * pubkey[0]) % l
    # 云计算内容
    r1 = exp_mode(u, A1, l)
    r2 = exp_mode(u, A2, l)
    # 验证
    temp1 = exp_mode(r1, t1, pubkey[0])
    temp2 = exp_mode(m, t2, pubkey[0])
    v1 = (temp1 * temp2) % pubkey[0]
    v2 = r2 % pubkey[0]
    print(v1)
    print(v2)
    if v1 == v2:
        ver = 1
    else:
        ver = 0
    # 恢复结果
    global res
    res = r1 % pubkey[0]
    return ver, res


def xsosde(res):
    print("jiemi pr", pr)
    r22 = random.randint(0, 100)
    k12 = random.randint(0, 100)
    k22 = random.randint(0, 100)
    t12 = random.randint(0, 100)
    t22 = random.randint(0, 100)
    A1 = selfkey[1] + k12 * fn
    A2 = t12 * selfkey[1] + t2 + k2 * fn
    u = (res + r22 * pubkey[0]) % l
    # 云计算内容
    r1 = exp_mode(u, A1, l)
    r2 = exp_mode(u, A2, l)
    # 验证
    temp1 = exp_mode(r1, t1, pubkey[0])
    temp2 = exp_mode(u, t2, pubkey[0])
    v1 = (temp1 * temp2) % pubkey[0]
    v2 = r2 % pubkey[0]
    print(v1)
    print(v2)
    if v1 == v2:
        vert = 1
    else:
        vert = 0
    # 恢复结果
    resu = r1 % pubkey[0]
    return vert, resu


if __name__ == '__main__':
    print("asdd")
    print("pr="+str(pr))
    """
    c = encrypt(m, pubkey)
    print("被加密后的密文-->%s" % c)
    '''信息解密'''
    d = str(decrypt(c, selfkey))
    outp = decryptming(d, '1938762450')
    print("被解密后的明文-->%s" % outp)
    """
"""
if __name__ == "__main__":
    '''公钥私钥中用到的两个大质数p,q，都是1024位'''
    p=getprimeover(1024)
    q=getprimeover(1024)
    r = random.randint(0,100)
    print(r)
    '''生成公钥私钥'''
    pubkey, selfkey = gen_key(p, q)
    '''需要被加密的信息转化成数字，长度小于秘钥n的长度，如果信息长度大于n的长度，那么分段进行加密，分段解密即可。'''
    inp=input()
    m=int(encryptming(inp,'1938762450'))
    print("待加密信息-->%s" % inp)
    '''信息加密，m被加密的信息，c是加密后的信息'''
    c = encrypt(m, pubkey)
    print("被加密后的密文-->%s" % c)
    '''信息解密'''
    d = str(decrypt(c, selfkey))
    outp=decryptming(d,'1938762450')
    print("被解密后的明文-->%s" % outp)
"""