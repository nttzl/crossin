# -*- coding: UTF-8 -*-
import datetime,requests,sqlalchemy

f = open("words.txt","a+",encoding="UTF-8")
f.seek(0)      # 指针挪到文件开始，再"a+"模式下默认最后
lines = f.readlines()
words = [line.split("\t")[0] for line in lines if line.strip()]
k = open("key.txt")
key = k.read()
url = "http://dict-co.iciba.com/api/dictionary.php?w={}&type=json&key=" + key       # api构造

def get_chs(word):
    try:
        r = requests.get(url.format(word))
        d = r.json()
        if not d.get("word_name"):          #　分析json的格式，当word不存在时，key"word_name"也不存在
            print("单词/词组不存在")
        else:
            words.append(word)              #实时更新单词列表
            ph_en = d["symbols"][0]["ph_en"]
            parts = d["symbols"][0]["parts"]
            means = "".join([i["part"] + "".join(i["means"]) for i in parts])
            worditem = word+'\t['+ph_en+']'+means+'\t'+str(datetime.date.today())
            print(worditem)
            f.write(worditem + '\n')
            f.flush()
    except:
        print("获取中文失败")
    
while 1:
    word=input("请输入你要记录的单词(直接回车退出程序):").strip()
    if not word:                  #回车退出循环
        break
    if word in words:
        print("单词已存在")
# 打出存在的单词和解释
        n = words.index(word)
        print(lines[n])
    else:
        get_chs(word)
        
    print("已记录{}个单词/词组".format(len(words)))
    print()
f.close()

   
  
