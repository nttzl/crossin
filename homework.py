# -*- coding: UTF-8 -*-
import datetime,requests

while 1:
    f = open("words.txt","a+")
    f.seek(0)
    lines = f.readlines()
    n = len(lines)
    words = []
    words.extend([line.split("\t")[0] for line in lines if line.strip()])
    
    word=input("请输入你要记录的单词(直接回车退出程序):").strip()
    if not word:
        break
    if word in words:
        print("单词已存在")
    else:
        worditem = word + '\t' + str(datetime.date.today())
        print(worditem)
        f.write(worditem + '\n')
        print("已记录{}个单词/词组".format(n+1))
    print()
    f.flush()
    f.close()

   
  
