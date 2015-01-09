# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 22:05:01 2014

@author: san
"""
from words_game_funtions import o_words
words_file = open('words.txt')
f_word = []
words_list = []
for line in words_file:
    word=line.strip()
    words_list.append(word)
#words_num = len(words_list)  #result: 113809
prefix = raw_input('Prefix:')
suffix = raw_input('Suffix:')
en_letter = raw_input('Enter your letters: ')
num = input('Enter word length: ')
print en_letter,num
#ou_letter = sorted(in_letter)
'''letter_list=[]
for le in en_letter:
    letter_list.append(le)
print 'You enter %s letters.\n'%len(letter_list), letter_list 
'''
ls = o_words(en_letter, num)
if prefix :
    ps = []
    for m in ls:
        ps.append(prefix+m)
    ls = ps
if suffix :
    ss = []
    for n in ls :
        ss.append(n+suffix)
    ls = ss
#print ls,len(ls)
for w in words_list:
    if len(w)>(num+len(prefix)+len(suffix)): continue
    if w.find(prefix,0,len(prefix))==-1: continue
    if w.rfind(suffix,(len(w)-len(suffix)))==-1: continue
    for b in ls:
        if w==b:
            print b
            f_word.append(b)
print f_word
#raw_input()

                



    
