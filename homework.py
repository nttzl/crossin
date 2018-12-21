# -*- coding: UTF-8 -*-
import datetime,requests

f = open("words.txt","a+")
f.seek(0)
lines = f.readlines()
n = len(lines)
words = [line.split("\t")[0] for line in lines if line.strip()]

while 1:
    word=input("请输入你要记录的单词(直接回车退出程序):").strip()
    if not word:
        break
    if word in words:
        print("单词已存在")
    else:
        worditem = word + '\t' + str(datetime.date.today())
        print(worditem)
        f.write(worditem + '\n')
        f.flush()
    print("已记录{}个单词/词组".format(n+1))
    print()
f.close()

   
  
