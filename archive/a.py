#!/usr/bin/env python3
from collections import OrderedDict

SRC="TEXT_20221127.txt"
SKIP = " 【】「」"
DIGITS="123456789"
ALPHA_LEFT= "【"
ALPHA_RIGHT = "】"
BETA_LEFT = "「"
BETA_RIGHT = "」"

def main():
    with open(SRC) as fd:
        lines=fd.readlines()
    for line in lines:
        line = line.strip()
        #print(line)
        print(parseline(line))
        #print()

def isChinese(ch): return not ch in DIGITS+SKIP
def alpha(mark): return ALPHA_LEFT + mark + ALPHA_RIGHT
def beta (mark): return  BETA_LEFT + mark +  BETA_RIGHT

def parseline(line):
    line=line.strip()
    while line and line[0]=='X': line=line[1:]
    while line and line[-1]=='X': line=line[:-1]

    dikt=OrderedDict()

    for ch in line:
        if isChinese(ch):
            dikt[ch]=[]

    index=None
    for ch in line:
        if ch in DIGITS:
            index = ch
        if isChinese(ch) and not index in dikt[ch]:
            dikt[ch].append(index)

    acc=[]
    seen=[]
    for ch in dikt.keys():
        marks=dikt[ch]
        first = marks.pop(0)
        if not first in seen:
            acc.append(alpha(first))
            seen.append(first)
        for mark in marks:
            acc.append(beta(mark))
        acc.append(ch)
    return 'X%sX' % ''.join(acc)

if __name__ == "__main__":
    main()
# X【1】AEF【2】AB【3】DDAX
# X【1】A「2」「3」EF【2】B【3】DX
# X【1】A {2} {3} EF【2】B【3】DX
# X [1] A {1} {2} {3} E {1} F {1} B {2} D {3}# 
# X【1】AEF【2】AB【3】DDAX
# X [1] {2} {3} A E F [2] B [3]  DX
#IN = "X【1】AEF【2】AB【3】DDAX"
#OUT = "X[1] {2} {3} A E F [2] B [3] DX"

