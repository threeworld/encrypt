# -*- coding = utf-8 -*-

import math

def gcd(a, b):
    """
    辗转相除法求最大公约数
    :param type(a) == int
           type(b) == int
    """
    if type(a) != int or type(b) != int:
        return 
    a, b = (a, b) if a >= b else (b, a)
    while b:
        a, b = b, a%b
    return a

def isPrime(n):
    """
    判断一个数是否为素数
    :param type(n) == int
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def ext_gcd(a, b):
    """
    扩展欧几里得算法
    """
    if type(a) != int or type(b) != int:
        return 
    if b == 0:
        return 1, 0, a
    x, y, q = ext_gcd(b, a%b)
    x, y = y, (x - int(a/b)*y)
    return x, y, q

def mod_exp(b, n, m):
    """
    模指运算，计算 b^n (mod m)
    """
    """ ret = 1
    while n > 0:
        ret = b * ret % m
        n = n-1

    return ret """
    ret = 1
    tmp = b
    while n:
        if n&0x1:
            ret = ret * tmp % m
        tmp = tmp*tmp % m
        n >>=1
    return ret

def phi(n):
    """
    欧拉函数
    """
    ret = 1
    i = 2
    n = int(n)
    while i*i <= n:
        if n%i == 0:
            n = int(n/i)
            ret = int(ret*i) - ret
            while n % i == 0:
                n = int(n/i)
                ret = ret*i
        i = i + 1
    if n > 1:
        ret = int(ret*n) -ret
        
    return ret

def random_prime(n):
    pass