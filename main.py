
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from phe import  paillier
import numpy as np
import protocol4 as p4
import paillierself
import random
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """public_key, private_key = paillier.generate_paillier_keypair()
    secret_number_list = [3.141592653, 300, -4.6e-12]
    encrypted_number_list = [public_key.encrypt(x) for x in secret_number_list]
    print([private_key.decrypt(x) for x in encrypted_number_list])
    A = [3.6, 300, -5e-10]
    enA = [public_key.encrypt(x) for x in A]
    print(enA)
    B = [3, 300, -3e-10]
    enB = [public_key.encrypt(x) for x in B]
    en = np.add(enA , enB)
    print([private_key.decrypt(x) for x in en])
    c = np.random.permutation([1, 4, 9, 12, 15])
    print(c)
    a = 12
    k = a.bit_length()
    print(k)"""
    n, public_key, private_key = paillierself.generate_paillier_keypair()
    """
    print("客户端输入X:")
    arr = input()
    x = [int(n) for n in arr.split()]
    #print(x)
    print("服务端输入K和W:")
    k = int(input())
    line = [[0] * k] * k
    for i in range(k):
        line[i] = input().split(" ")
        line[i] = [int(j) for j in line[i]]
    """
    d = 2
    x = np.random.randint(64, size=d)
    k = 3
    w = [[0] * d] * k
    for i in range(k):
        w[i] = np.random.randint(128, size=d)
        w[i] = [int(j) for j in w[i]]
    x1 = [int(i) for i in x]
    print(x1, w)
    print(p4.protocol4(x1, w, public_key, private_key))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/