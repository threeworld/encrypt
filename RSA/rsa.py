# -*- coding = utf-8 -*-

import math
import random

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
    if b == 0:
        return 1, 0, a
    else:
        x, y, q = ext_gcd(b, a % b) 
        x, y = y, (x - (a // b) * y)
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
            n = n // i
            ret = int(ret*i) - ret
            while n % i == 0:
                n = n//i
                ret = ret*i
        i = i + 1
    if n > 1:
        ret = int(ret*n) -ret
        
    return ret

def computeD(fn, e):
    (x, y, r) = ext_gcd(fn, e)
    #y maybe < 0, so convert it 
    if y < 0:
        return fn + y
    return y

def random_prime(halfkeylength):
    """
    随机选出素数p,q
    """
    while True:
        #选择随机数
        n = random.randint(0, 1<<halfkeylength)
        if n % 2 != 0:
            found = True
            #随机性测试
            for i in range(0, 5):
                if prime_test(n) == 'composite':
                    found = False
                    break
            if found == True:
                return n

def prime_test(n):
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

def generate_key(key_len):
    """
    生成 n ,e ,d
    """
    p = random_prime(key_len//2)
    q = random_prime(key_len//2)
    n = p * q
    fn = (p - 1) * (q - 1)
    print(fn)
    e = 65537
    d = computeD(fn, e)
    return (n, e, d)

def encryption(M, e, n):
    return mod_exp(M, e, n)

def decryption(C, d, n):
    return mod_exp(C, d, n)

if __name__ == '__main__':
    #print(random_prime(60))
    (n, e, d) = generate_key(100)
    print(n,e,d)
    text = random.randint(0, 1<<20)
    C = encryption(text, e, n)
    M = decryption(C, d, n)
    print(text)
    print(C)
    print(M==text)