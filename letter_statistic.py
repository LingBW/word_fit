# -*- coding: utf-8 -*-
"""
Created on Thu Nov 20 21:17:38 2014

@author: san
"""

words_file = open('words.txt')
words_list = []
for line in words_file:
    word=line.strip()
    words_list.append(word)
########################
a=0;b=0;c=0;d=0;e=0;f=0;g=0;h=0;i=0;j=0;k=0;l=0;m=0;n=0;o=0;p=0;q=0;r=0;s=0;t=0
u=0;v=0;w=0;x=0;y=0;z=0
for word in words_list:
    for li in word:
        if li=='a':
            a=a+1
        if li=='b':
            b=b+1
        if li=='c':
            c=c+1
        if li=='d':
            d=d+1
        if li=='e':
            e=e+1 
        if li=='f':
            f=f+1
        if li=='g':
            g=g+1
        if li=='h':
            h=h+1
        if li=='i':
            i=i+1
        if li=='j':
            j=j+1
        if li=='k':
            k=k+1
        if li=='l':
            l=l+1
        if li=='m':
            m=m+1
        if li=='n':
            n=n+1
        if li=='o':
            o=o+1
        if li=='p':
            p=p+1
        if li=='q':
            q=q+1
        if li=='r':
            r=r+1
        if li=='s':
            s=s+1
        if li=='t':
            t=t+1
        if li=='u':
            u=u+1
        if li=='v':
            v=v+1
        if li=='w':
            w=w+1
        if li=='x':
            x+=1
        if li=='y':
            y+=1
        if li=='z':
            z+=1
print 'a:%d\n'%a,'b:%d\n'%b,'c:%d\n'%c,'d:%d\n'%d,'e:%d\n'%e,'f:%d\n'%f,'g:%d\n'%g,'h:%d\n'%h,'i:%d\n'%i
print 'j:%d\n'%j,'k:%d\n'%k,'l:%d\n'%l,'m:%d\n'%m,'n:%d\n'%n,'o:%d\n'%o,'p:%d\n'%p,'q:%d\n'%q,'r:%d\n'%r
print 's:%d\n'%s,'t:%d\n'%t,'u:%d\n'%u,'v:%d\n'%v,'w:%d\n'%w,'x:%d\n'%x,'y:%d\n'%y,'z:%d\n'%z
ls = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
ls.sort()
print ls
