# -*- coding: utf-8 -*- 

from array import array

#轮秘钥生成使用的RC表
Rcon = [
    0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
    0x80, 0x1B, 0x36,
]

#S盒表
SBox = [
    [0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,],
    [0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,],
    [0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,],
    [0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,],
    [0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,],
    [0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,],
    [0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,],
    [0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,],
    [0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,],
    [0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,],
    [0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,],
    [0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,],
    [0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,],
    [0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,],
    [0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,],
    [0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,],
]

#逆S盒表
InvSBox = [
    [0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,],
    [0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,],
    [0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,],
    [0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,],
    [0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,],
    [0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,],
    [0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,],
    [0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,],
    [0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,],
    [0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,],
    [0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,],
    [0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,],
    [0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,],
    [0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,],
    [0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,],
    [0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,],
]

#shift Table
shiftTable = [
    [0, 1, 2, 3],
    [1, 2, 3, 0],
    [2, 3, 0, 1],
    [3, 0, 1, 2],
]
#inv shift table
inv_shiftTable = [
    [0, 3, 2, 1],
    [1, 0, 3, 2],
    [2, 1, 0, 3],
    [3, 2, 1, 0],
]

# 有限域GF(2^8)定义的乘法
def gf_multi(a, b):
    p = 0
    while b:
        if b & 0x01:
            p ^= a
        a <<= 1
        if a & 0x100:
            a ^= 0x1b
        b >>= 1
    return p & 0xff

#encrypt 列混合使用的表
gf_mul_by_02 = array('B', [gf_multi(x, 2) for x in range(256)])
gf_mul_by_03 = array('B', [gf_multi(x, 3) for x in range(256)])

#decrypt 列混合使用的表
gf_mul_by_09 = array('B', [gf_multi(x, 9) for x in range(256)])
gf_mul_by_0b = array('B', [gf_multi(x, 11) for x in range(256)])
gf_mul_by_0d = array('B', [gf_multi(x, 13) for x in range(256)])
gf_mul_by_0e = array('B', [gf_multi(x, 14) for x in range(256)])

#将明文text转换成矩阵
def text_to_matrix(text):
    matrix = []
    for i in range(16):
        byte = (text >> (8 * (15 - i))) & 0xff
        if i % 4 == 0:
            matrix.append([byte])
        else:
            matrix[i // 4].append(byte)
    return matrix

#将矩阵转成明文text
def matrix_to_text(matrix):
    text = 0
    for i in range(4):
        for j in range(4):
            text |= matrix[i][j] << (120 - 8*(4*i+j))
    return text

class AES:
    
    #初始化化秘钥
    def __init__(self, cipher_key):
        self.cipher_key = cipher_key
        self.keyExpansion(self.cipher_key)

    #轮秘钥生成
    def keyExpansion(self, cipher_key):
        self.round_keys = text_to_matrix(cipher_key)
        #生成10个轮秘钥
        for i in range(4, 4 * 11):
            self.round_keys.append([])
            if i % 4 == 0:
                tmp = self.round_keys[i-1][1:]+self.round_keys[i-1][:1]
                for j in range(4):
                    row = tmp[j] >> 4
                    column = tmp[j] & 0x0f
                    if j == 0:
                        byte = self.round_keys[i-4][0] ^ SBox[row][column] ^ Rcon[i // 4]
                        self.round_keys[i].append(byte)
                    else:
                        byte = self.round_keys[i-4][j] ^ SBox[row][column]
                        self.round_keys[i].append(byte)
            else:
                for j in range(4):
                    byte = self.round_keys[i - 4][j] ^ self.round_keys[i - 1][j]
                    self.round_keys[i].append(byte)
    
    #生成解密轮秘钥
    def inv_keyExpansion(self, round_key):
        self.inv_round_keys = round_key[ :4]
        for i in range(1, 10):
            tmp = self.inv_mixColumn(round_key[4*i: 4*(i+1)])
            for j in range(4):
                self.inv_round_keys.append(tmp[j])
        self.inv_round_keys += round_key[40:]

    #S盒变换
    def byteSub(self, matrix):
        for i in range(4):
            for j in range(4):
                a = matrix[i][j]
                row = a >> 4
                column = a & 0x0f
                matrix[i][j] = SBox[row][column]
    
    #逆S盒变换
    def inv_byteSub(self, matrix):
        for i in range(4):
            for j in range(4):
                a = matrix[i][j]
                row = a >> 4
                column = a & 0x0f
                matrix[i][j] =InvSBox[row][column]

    #行移位变换
    def shiftRow(self, matrix):
        result = []
        for j in range(4):
            result.append([])
            for i in range(4):
                tmp = matrix[shiftTable[j][i]][i]
                result[j].append(tmp)
        self.state = result

    #逆行移位
    def inv_shiftRow(self, matrix):
        result = []
        for j in range(4):
            result.append([])
            for i in range(4):
                tmp = matrix[inv_shiftTable[j][i]][i]
                result[j].append(tmp)
        self.state = result    

    #列混合变换
    def mixColumn(self, matrix):
        mul_by_2 = gf_mul_by_02
        mul_by_3 = gf_mul_by_03
        j = 0
        for i in range(4):
            v0, v1, v2, v3 = matrix[i]
            matrix[i][j] = mul_by_2[v0] ^ mul_by_3[v1] ^ v2 ^v3
            matrix[i][j+1] = v0 ^ mul_by_2[v1] ^ mul_by_3[v2] ^ v3
            matrix[i][j+2] = v0 ^ v1 ^ mul_by_2[v2] ^ mul_by_3[v3]
            matrix[i][j+3] = mul_by_3[v0] ^ v1 ^ v2 ^ mul_by_2[v3]

    #逆列混合变换
    def inv_mixColumn(self, matrix):
        mul_by_9 = gf_mul_by_09
        mul_by_b = gf_mul_by_0b
        mul_by_d = gf_mul_by_0d
        mul_by_e = gf_mul_by_0e
        j = 0
        for i in range(4):
            v0, v1, v2, v3 = matrix[i]
            matrix[i][j] = mul_by_e[v0] ^ mul_by_b[v1] ^ mul_by_d[v2] ^ mul_by_9[v3]
            matrix[i][j+1] = mul_by_9[v0] ^ mul_by_e[v1] ^ mul_by_b[v2] ^ mul_by_d[v3]
            matrix[i][j+2] = mul_by_d[v0] ^ mul_by_9[v1] ^ mul_by_e[v2] ^ mul_by_b[v3]
            matrix[i][j+3] = mul_by_b[v0] ^ mul_by_d[v1] ^ mul_by_9[v2] ^ mul_by_e[v3]

        return matrix

    #轮秘钥加变换
    def addRoundKey(self, state_matrix, key_matrix):
        for i in range(4):
            for j in range(4):
                state_matrix[i][j] ^= key_matrix[i][j]
        return state_matrix
    
    #加密函数
    def encrypt(self, text):
        
        #轮秘钥加
        matrix = text_to_matrix(text)
        self.state = self.addRoundKey(matrix, self.round_keys[:4])

        #轮函数
        for i in range(4, 44, 4):
            print('N = %s' % (i // 4))
            self.byteSub(self.state)
            print('    After byteSub: %s \n'% hex(matrix_to_text(self.state))[2:])
            self.shiftRow(self.state)
            print('   After shiftRow: %s \n' % hex(matrix_to_text(self.state))[2:])
            if i != 40:
                self.mixColumn(self.state)
            else:
                pass
            print('  After mixColumn: %s \n' % hex(matrix_to_text(self.state))[2:])
            self.addRoundKey(self.state, self.round_keys[i:i+4])
            print('        round_key: %s \n' % hex(matrix_to_text(self.round_keys[i:i+4]))[2:])
            print('After addRoundKey: %s \n' % hex(matrix_to_text(self.state))[2:])
        
        return hex(matrix_to_text(self.state))

    #解密函数
    def decrypt(self, text):
        
        tmp = self.round_keys
        self.inv_keyExpansion(tmp)
        matrix = text_to_matrix(text)
        #轮密钥加
        self.state = self.addRoundKey(matrix, self.inv_round_keys[40:])

        for i in range(10, 0, -1):
            print('N = %s' % i)
            self.inv_byteSub(self.state)
            print('  After inv_byteSub: %s \n'% hex(matrix_to_text(self.state))[2:])
            self.inv_shiftRow(self.state)
            print(' After inv_shiftRow: %s \n' % hex(matrix_to_text(self.state))[2:])
            if i != 1:
                self.inv_mixColumn(self.state)
            else:
                pass
            print('After inv_mixColumn: %s \n' % hex(matrix_to_text(self.state))[2:])
            self.addRoundKey(self.state, self.inv_round_keys[4*(i-1): 4*i])
            print('          round_key: %s \n' % hex(matrix_to_text(self.round_keys[4*(i-1): 4*i]))[2:])
            print('  After addRoundKey: %s \n' % hex(matrix_to_text(self.state))[2:])

if __name__ == '__main__':

    key = 0x00012001710198aeda79171460153594
    plaintext = 0x0001000101a198afda78173486153566
    ciphertext = 0x6cdd596b8f5642cbd23b47981a65422a
    aes = AES(key)
    aes.encrypt(plaintext)
    aes.decrypt(ciphertext)