# -*- coding:utf-8 -*-

import base64, random,sys, time

#初始化IP
PI = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

#初始化置换选择1
CP_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]
    
#初始化置换选择2
CP_2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]

#选择运算E,将32位明文扩展成48位
E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

#SBOX
S_BOX = [
         
[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
 [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
 [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
 [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
],

[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
 [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
 [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
 [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
],

[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
 [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
 [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
 [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
],

[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
 [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
 [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
 [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
],  

[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
 [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
 [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
 [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
], 

[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
 [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
 [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
 [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
], 

[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
 [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
 [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
 [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
],
   
[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
 [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
 [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
 [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
]
]

#初始化置换运算P, 将32位的数据打乱重新排序
P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

#逆初始置换IP^-1,是初始置换IP的逆置换
PI_1 = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]

#没产生子密钥所需的循环左移的位数
SHIFT = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

ENCRYPT = 1
DECRYPT = 0
"""
task 1
"""
#计算给定对应差分计算输入对
def diff_pair(pair):
    value = 0
    diff_pair_list = []
    for i in range(0,64):
        xor_value = i ^ pair
        bin_value_xor = binvalue(xor_value, 6)
        bin_value_i = binvalue(i, 6)
        diff_pair_list.append([bin_value_i, bin_value_xor])
    return diff_pair_list

#输出差分
def out_diff(diff_pair_list):
    out_xor_value = 0
    diffpair_key = {}
    for i in range(0, 64):
        SB_1 = substitute(diff_pair_list[i][0], 0)
        SB_2 = substitute(diff_pair_list[i][1], 0)
        out_xor_value = int(SB_1, 2) ^ int(SB_2, 2)
        bin_value = binvalue(out_xor_value, 4)
        diffpair_key[str(diff_pair_list[i])] = bin_value
    return diffpair_key

#输出信息函数
def print_message(diffpair, diff_pair_list, diffpair_key):
    out_list = []
    print('----------- 输入差分：'+ str(diffpair)+' -----------')
    for i in range(64):
        print('第'+ str(i+1)+ '对：'+ str(diff_pair_list[i]) + '\t输出差分：'+ diffpair_key[str(diff_pair_list[i])])
    print('S1的输出差分\t\t可能输入的值')
    for i in range(16):
        stat_list = []
        for j in range(64):
            tmp = int(diffpair_key[str(diff_pair_list[j])], 2)
            if tmp == i:
                stat_list.append(diff_pair_list[j][0])
                stat_list.append(diff_pair_list[j][1])
        bin_i = binvalue(i, 4)
        print(bin_i+'\t\t\t' + str(list(set(stat_list))))
            

#使用sbox替代函数
def substitute(data, S_BOX_I):
    array = list()
    array.extend([int(x) for x in list(data)])
    result = []
    row = int(str(array[0])+str(array[5]),2) #行号
    column = int(''.join([str(x) for x in array[1:][:-1]]), 2) #列号
    val = S_BOX[S_BOX_I][row][column] #该位置的值
    bin = binvalue(val,4)  #输入到列表
    return bin

#输入输出差分统计主函数
def io_diff_main(diffpair):
    #eg: diffpair = 0b000001
    diff_pair_list = diff_pair(diffpair)
    result = out_diff(diff_pair_list)
    print_message(diffpair, diff_pair_list,result)

"""
task 2
"""
#对arr数组改变n位
def change_arr_number(arr, n):
    flag = []
    res = []
    for i in range(64):
        flag.append(False)
        res.append(arr[i])
    while n > 0:
        id = random.randint(0, 63)
        if flag[id] == False:
            flag[id] = True
            res[id] = res[id] ^ 1
            n = n-1
    return res

#改变明文
def change_arr():
    arr = []
    for i in range(64):
        arr.append(random.randint(0, 1)) 
    return arr

#查找两个数组不同的位数
def find_diff(arr1, arr2):
    count = 0
    for i in range(64):
        if arr1[i] != arr2[i]:
            count+=1
    return count

#明文改变1...64位，统计密文输出改变位数主函数
def text_change_statist(arr_text, arr_key):
    des = DES()
    arr1 = des.stat_run(arr_key, arr_text, ENCRYPT)
    print('明文改变位数\t\t输出密文平均改变的位数')
    for i in range(1, 65):
        count = 0
        for j in range(100):
            res = change_arr_number(arr_text, i)
            arr2 = des.stat_run(arr_key, res, ENCRYPT)
            count += find_diff(arr1, arr2)
        print(str(i)+ '\t\t\t\t'+ str((count/100)))
        

#测试主函数
def text_statist_main():
    arr_key = change_arr()
    for i in range(1):
        print('*'*10+' 第 ' + str((i+1)) + '次测试 '+'*'*10)
        arr_text = change_arr()
        text_change_statist(arr_text, arr_key)

"""
task 3
"""
#密钥改变n位，输出密文改变的位数
def key_change_statist(arr_text, arr_key):
    des = DES()
    #密钥没改变时生成密文
    arr1 = des.stat_run(arr_key, arr_text, ENCRYPT)
    print('密钥改变位数\t\t输出密文平均改变的位数')
    for i in range(1, 65):
        count = 0
        for j in range(100):
            #密钥改变 i 位
            arr_key = change_arr_number(arr_key, i)
            #密钥改变时生成的密文
            arr2 = des.stat_run(arr_key, arr_text, ENCRYPT)
            count += find_diff(arr1, arr2)
        print(str(i)+ '\t\t\t\t'+ str((count/100)))

#测试主函数
def key_statist_main():
    arr_text = change_arr()
    for i in range(1):
        print('*'*10+' 第 ' + str((i+1)) + '次测试 '+'*'*10)
        arr_key = change_arr()
        key_change_statist(arr_text, arr_key)

"""
功能函数
"""
#将字符串转换为位列表
def string_to_bit_array(text):
    array = list()
    for char in text:
        binval = binvalue(char, 16) #得到字符的二进制位
        array.extend([int(x) for x in list(binval)])
    return array

# 将给定大小的字符串返回其二进制值
def binvalue(val, bitsize):
    if isinstance(val, int):
        binval = bin(val)[2:]
    else:
        binval = bin(ord(val))[2: ]
    if len(binval) > bitsize:
        raise 'binary value larger than the expected size'
    while len(binval) < bitsize:
        binval = '0'+binval
    return binval

#位数组重新生成字符串
def bit_array_to_string(array):
    res = ''.join([chr(int(y, 2)) for y in [''.join([str(x) for x in byte]) for byte in  nsplit(array,16)]])
    return res

#将列表拆分为长度为n的子序列
def nsplit(s, n):
    #print([s[k:k+n] for k in range(0, len(s), n)])
    return [s[k:k+n] for k in range(0, len(s), n)]
    

class DES():
    
    def __init__(self):
        self.password = None
        self.text = None
        self.keys = list()
    
    def run(self, key, text, action = ENCRYPT, padding = True):
        if len(key) < 8:
            raise('Key Should be 8 bytes long')
        elif len(key) > 8:
            key = key[ :8] #如果key大于8个字符，取前面8个字符
        
        self.password = key  #密钥
        self.text = text     #明文

        if padding and action == ENCRYPT:
            self.addPadding()
        
        #生成是所有的字密钥
        self.generatekeys()
        text_blocks = nsplit(self.text, 4)
        result = list()
        for block in text_blocks:
            block = string_to_bit_array(block) #生成64位二进制位列表
            block = self.permut(block, PI)  #初始置换IP
            g, d = nsplit(block, 32)  #将明文分为左32位,右32位
            tmp = None
            for i in range(16):
                d_e = self.expend(d, E)
                if action == ENCRYPT:
                    tmp = self.xor(self.keys[i],d_e)
                else:
                    tmp = self.xor(self.keys[15-i],d_e)
                tmp = self.substitute(tmp) #sbox
                tmp = self.permut(tmp, P)
                tmp = self.xor(g, tmp)
                g = d
                d = tmp
            result += self.permut(d+g, PI_1)
        
        final_res = bit_array_to_string(result)
        if padding and action == DECRYPT:
            return self.removePadding(final_res)
        else:
            return final_res.encode('utf-8')
    
    #统计改变位数的加密函数
    def stat_run(self, arr_key, arr_text, action = ENCRYPT, padding = False):
        if len(arr_key) < 64:
            raise('Key Should be 8 bytes long')
        elif len(arr_key) > 64:
            key = arr_key[ :64] #如果key大于8个字符，取前面8个字符
        
        self.password = arr_key  #密钥
        self.text = arr_text     #明文

        if padding and action == ENCRYPT:
            self.addPadding()

        self.generatekeys_change(arr_key)

        result = []
        block = self.permut(arr_text, PI)
        g, d = nsplit(block, 32)  #将明文分为左32位,右32位
        tmp = None
        for i in range(16):
            d_e = self.expend(d, E)
            if action == ENCRYPT:
                tmp = self.xor(self.keys_change[i],d_e)
            else:
                tmp = self.xor(self.keys_change[15-i],d_e)
            tmp = self.substitute(tmp) #sbox
            tmp = self.permut(tmp, P)
            tmp = self.xor(g, tmp)
            g = d
            d = tmp
        result = self.permut(d+g, PI_1)
        return result

    #置换选择函数
    def permut(self, block, table):
        return [block[x-1] for x in table]

    #将右边32位的明文输入经过选择运算E扩展成48位
    def expend(self, block, table):
        return [block[x-1] for x in table]

    def xor(self, t1, t2):
        return [x^y for x, y in zip(t1, t2)]

    #生成16个子密钥
    def generatekeys(self):
        self.keys = []
        key = string_to_bit_array(self.password)
        key = self.permut(key, CP_1)
        g, d = nsplit(key, 28)
        for i in range(16): #循环16次
            g, d = self.shift(g, d, SHIFT[i])
            tmp = g + d
            self.keys.append(self.permut(tmp, CP_2))
    
    #改变n位数之后生成16个子密钥
    def generatekeys_change(self, arr):
        self.keys_change = []
        key = self.permut(arr, CP_1)
        g, d = nsplit(key, 28)
        for i in range(16): #循环16次
            g, d = self.shift(g, d, SHIFT[i])
            tmp = g + d
            self.keys_change.append(self.permut(tmp, CP_2))
    
    #使用sbox代替函数
    def substitute(self, data):
        subblocks = nsplit(data, 6)
        result = []
        for i in range(len(subblocks)):
            block = subblocks[i]
            row = int(str(block[0])+str(block[5]),2) #行号
            column = int(''.join([str(x) for x in block[1:][:-1]]), 2) #列号
            val = S_BOX[i][row][column] #该位置的值
            bin = binvalue(val,4)
            result += [int(x) for x in bin]  #输入到列表
        return result

    #循环左移函数
    def shift(self, g, d, n):
        return g[n:] + g[:n], d[n:] + d[:n]

    #根据PKCS5规范填充位数
    def addPadding(self):
        pad_len = 8 - len(self.text) % 8
        self.text += pad_len*chr(pad_len)

    #移除填充的部分
    def removePadding(self, data):
        pad_len = ord(data[-1]) #最后的数字
        return data[:-pad_len]
    
    #加密函数
    def encrypt(self, key, text, padding=True):
        return self.run(key, text, ENCRYPT, padding)
    
    #解密函数
    def decrypt(self, key, text, padding=True):
        return self.run(key, text, DECRYPT, padding)

if __name__ == '__main__':
    text = 'testtest'
    key = 'password'
    #text_statist_main()
    #key_statist_main()
    io_diff_main(0b000001)
    des = DES()
    print(base64.b64encode(des.encrypt(key, text)))