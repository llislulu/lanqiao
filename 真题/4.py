import os
import sys
import re


def convertSize(byte):
    size = {'GB': 0, 'MB': 0, 'KB': 0, 'B': 0}
    if byte > 1073741824:
        size['GB'] = byte // 1073741824
    byte %= 1073741824
    if byte > 1048576:
        size['MB'] = byte // 1048576
    byte %= 1048576
    if byte > 1024:
        size['KB'] = byte // 1024
    byte %= 1024
    size['B'] = byte
    return size


def printSize(l):
    size = convertSize(l)
    ans = ''
    if size['GB'] > 0:
        ans += f"{size['GB']}GB"
    if size['MB'] > 0:
        ans += f"{size['MB']}GB"
    if size['KB'] > 0:
        ans += f"{size['KB']}GB"
    if size['B'] > 0:
        ans += f"{size['B']}GB"
    print(ans)


n = int(input())
l = 0
typs = {'int': 4, 'long': 8, 'String': 1}
for i in range(n):
    s = input()
    os = s.split(maxsplit=1)
    t = os[0]
    r = os[1]
    if '[]' in t:
        tp = t.replace('[]', '')
        zkh = re.compile('\[\d+?\]')
        tm = zkh.findall(r)
        for j in tm:
            it = int(j[1: -1]) * typs[tp]
            l += it
    else:
        if t == 'String':
            zk = re.compile('”.+?”')
            tm = zk.findall(r)
            for j in tm:
                it = len(j) - 2
                l += it
        else:
            dh = r.count('，') + 1
            l += dh * typs[t]
printSize(l)
