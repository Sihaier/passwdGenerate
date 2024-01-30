#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@illustrate：
    根据用户输入的关键词，生成关联的密码本
@File ：main.py
@Author ：zsh
@Date ：2024/1/30 11:56 
@author： 
'''
import itertools
import argparse

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--min', type=int, default=6, help="min number for password length")
parser.add_argument('--max', type=int, default=10, help="max number for password length")
parser.add_argument('-k', '--keys', dest="list", nargs='+', help="Use these keys as an extension")
parser.add_argument('-o', '--output', type=str, default="passwd.txt", help="output filename")

args = parser.parse_args()

min_number = args.min
max_number = args.max
keys_wd = args.list
file_name = args.output

print("min number: ", min_number)
print("max number: ", max_number)
print("keys list: ", keys_wd)
print("output filename: ", file_name)

# custom these keys
before_common_str = ["qwe", "Qwe", "Qaz", "!@#", "!234", "admin",
                     "root", "password", "Abc", "abc",
                     "@@", "##", "!!", "zxc",
                     ]
middle_common_str = ["@@", "@", "#", "!@#", "??", "$", "*", "&&", "&", "!!", "!", ".", ".."]

after_common_str = [".", "$", "123", "1234", "123456", "qwE", "qweR"
                                                              "!@#", "123$", "admin", "root", "password", "Abc", "abc",
                    "987", "321", "@@", "##", "!!", "zxc", "1314", "502", "520",
                    "2023", "2022", "2021", "2024"
                    ]

all_keys = []

# 前中后组合
options_combination = [
    [before_common_str, keys_wd],
    [before_common_str, keys_wd, middle_common_str],
    [before_common_str, keys_wd, after_common_str],
    [before_common_str, keys_wd, middle_common_str, after_common_str],
    [before_common_str, middle_common_str, keys_wd, after_common_str],
    [keys_wd, middle_common_str],
    [keys_wd, after_common_str],
    [keys_wd, middle_common_str, after_common_str],
    # [middle_common_str, keys_wd],
    # [middle_common_str, keys_wd, after_common_str],
    [before_common_str, after_common_str],
    [before_common_str, middle_common_str, after_common_str]
]

for combination in options_combination:
    for comb_ss in itertools.product(*combination):
        key = "".join(comb_ss)
        if len(key) >= min_number and len(key) <= max_number:
            all_keys.append(key + "\n")

# 去重并写入
all_keys = set(all_keys)
f = open(file_name, 'a', encoding='utf-8')
for k in all_keys:
    f.write(k)
f.close()

print("success output password in your current dir path")
