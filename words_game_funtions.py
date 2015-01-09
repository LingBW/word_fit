# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 20:34:39 2014

@author: san
"""
from collections import Counter
def fval(st,wt):  
    v = []; u = []
    l = Counter(st); w = Counter(wt)
    m = max(l.values())
    if max(w.values())>m: return False
    if max(w.values())==1: return True
    for i,j in l.items():
        if j>1: v.append(i)
    for i,j in w.items():
        if j>1: u.append(i)
    return set(u).issubset(set(v))
def o_words(string,num):
    ws = []
    if num==2:
        for a in string:
            ws.append(a)
            for b in string:
                ws.append(a+b)
        #return ws
    if num==3:
        for a in string:
            ws.append(a)
            for b in string:
                ws.append(a+b)
                for c in string:
                    ws.append(a+b+c)
        #return ws
    if num==4:
        for a in string:
            ws.append(a)
            for b in string:
                ws.append(a+b)
                for c in string:
                    ws.append(a+b+c)
                    for d in string:
                        ws.append(a+b+c+d)
        #return ws
    if num==5:
        for a in string:
            ws.append(a)
            for b in string:
                ws.append(a+b)
                for c in string:
                    ws.append(a+b+c)
                    for d in string:
                        ws.append(a+b+c+d)
                        for e in string:
                            ws.append(a+b+c+d+e)
        #return ws
    if num==6:
        for a in string:
            ws.append(a)
            for b in string:
                ws.append(a+b)
                for c in string:
                    ws.append(a+b+c)
                    for d in string:
                        ws.append(a+b+c+d)
                        for e in string:
                            ws.append(a+b+c+d+e)
                            for f in string:
                                ws.append(a+b+c+d+e+f)
        #return ws
    if num==7:
        for a in string:
            ws.append(a)
            for b in string:
                ws.append(a+b)
                for c in string:
                    ws.append(a+b+c)
                    for d in string:
                        ws.append(a+b+c+d)
                        for e in string:
                            ws.append(a+b+c+d+e)
                            for f in string:
                                ws.append(a+b+c+d+e+f)
                                for g in string:
                                    ws.append(a+b+c+d+e+f+g)
        #return ws
    if num==8:
        for a in string:
            ws.append(a)
            for b in string:
                ws.append(a+b)
                for c in string:
                    ws.append(a+b+c)
                    for d in string:
                        ws.append(a+b+c+d)
                        for e in string:
                            ws.append(a+b+c+d+e)
                            for f in string:
                                ws.append(a+b+c+d+e+f)
                                for g in string:
                                    ws.append(a+b+c+d+e+f+g)
                                    for h in string:
                                        ws.append(a+b+c+d+e+f+g+h)
        #return ws
    if num==9:
        for a in string:
            ws.append(a)
            for b in string:
                ws.append(a+b)
                for c in string:
                    ws.append(a+b+c)
                    for d in string:
                        ws.append(a+b+c+d)
                        for e in string:
                            ws.append(a+b+c+d+e)
                            for f in string:
                                ws.append(a+b+c+d+e+f)
                                for g in string:
                                    ws.append(a+b+c+d+e+f+g)
                                    for h in string:
                                        ws.append(a+b+c+d+e+f+g+h)
                                        for i in string:
                                            ws.append(a+b+c+d+e+f+g+h+i)
        #return ws
    if num==10:
        for a in string:
            ws.append(a)
            for b in string:
                ws.append(a+b)
                for c in string:
                    ws.append(a+b+c)
                    for d in string:
                        ws.append(a+b+c+d)
                        for e in string:
                            ws.append(a+b+c+d+e)
                            for f in string:
                                ws.append(a+b+c+d+e+f)
                                for g in string:
                                    ws.append(a+b+c+d+e+f+g)
                                    for h in string:
                                        ws.append(a+b+c+d+e+f+g+h)
                                        for i in string:
                                            ws.append(a+b+c+d+e+f+g+h+i)
                                            for j in string:
                                                ws.append(a+b+c+d+e+f+g+h+i+j)
    #s=Counter(string)
    #mx=max(s.values())
    ls=set(ws)
    #print ls,len(ls)
    ct=[]
    for k in ls:
        if fval(string,k):
            ct.append(k)
        '''m=Counter(k) #统计相同元素的个数
        if max(m.values())<=mx:
            if max(m.values())==2: 
                if fval(string,k):
                    ct.append(k)
                continue
            if max(m.values())==3: 
                if fval(string,k):
                    ct.append(k)
                continue
            ct.append(k)'''
        
        '''for i in m.values():
            if i<=mx:
                ct.append(k)
    #print ct,len(ct)
    for ar in ct:
        ls.remove(ar)
    #ls=set(ws) #合并相同的元素'''
    return ct
