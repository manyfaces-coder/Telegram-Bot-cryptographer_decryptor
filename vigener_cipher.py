# -*- coding: utf-8 -*-

import dict_symbs

def encode_val(word):
    list_code = []
    d = dict_symbs.d

    for w in range(len(word)):
        for value in d:
            if word[w] == d[value]:
               list_code.append(value)
    return list_code

def comparator(value, key):
    len_key = len(key)
    dic = {}
    iter = 0
    full = 0

    for i in value:
        dic[full] = [i,key[iter]]
        full = full + 1
        iter = iter +1
        if (iter >= len_key):
            iter = 0
    return dic

def full_encode(value, key):
    dic = comparator(value, key)
    encryption = []
    d = dict_symbs.d

    for i in dic:
        go = (dic[i][0]+dic[i][1]) % len(d)
        encryption.append(go)
    return encryption

def decode_val(list_in):
    list_code = []
    d = dict_symbs.d

    for i in range(len(list_in)):
        for value in d:
            if list_in[i] == value:
               list_code.append(d[value])
    return list_code

def full_decode(value, key):
    dic = comparator(value, key)
    d = dict_symbs.d
    decryption =[]

    for v in dic:
        go = (dic[v][0]-dic[v][1]+len(d)) % len(d)
        decryption.append(go)
    return decryption

