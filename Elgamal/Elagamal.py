# -*- coding=utf-8 -*-
import random
import math


class PrivateKey:
    
    #私钥
    def __init__(self, p=None, g=None, d=None, iNumbits=0):
        self.p = p
        self.g = g
        self.d = d
        self.iNumbit = 0

class PublicKey:

    #公钥
    def __init__(self, p=None, g=None, y=None, iNumbits=0):
        self.p = p
        self.g = g
        self.y = y
        self.iNumbits = iNumbits

#求模p的原根
def find_primitive_root(p):
    if p == 2:
        return 1
    p1 = 2
    p2 = (p - 1) // p1

    while True:
        g = random.randint(2, p-1)
        if not mod_exp(g, p2, p) == 1:
            if not mod_exp(g, (p-1)//p2, p) == 1:
                return g    

#寻找素数
def find_prime(iNumbits):
    pass

    
#模指运算
def mod_exp(base, exp, modulus):
    return pow(base, exp, modulus)

#Miller素数概率检测
def Miller_Rabin(n):
    """
    测试n是否为素数
    """
    q = n - 1
    k = 0
    #寻找k,q 是否满足2^k*q =n - 1 
    while q % 2 == 0:
        k += 1;
        q = q // 2
    a = random.randint(2, n-2);
    #如果 a^q mod n= 1, n 可能是一个素数
    if mod_exp(a, q, n) == 1:
        return "inconclusive"
    #如果存在j满足 a ^ ((2 ^ j) * q) mod n == n-1, n 可能是一个素数
    for j in range(0, k):
        if mod_exp(a, (2**j)*q, n) == n - 1:
            return "inconclusive"
    #n 不是素数
    return "composite"