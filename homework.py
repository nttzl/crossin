# -*- coding: UTF-8 -*-
import datetime,requests,json

f = open("words.txt","a+")
f.seek(0)
lines = f.readlines()
words = [line.split("\t")[0] for line in lines if line.strip()]
key = "0B1BB61A44BE91B250ADFB416F2AD53B"
url = "http://dict-co.iciba.com/api/dictionary.php?w={}&type=json&key=" + key

while 1:
    word=input("请输入你要记录的单词(直接回车退出程序):").strip()
    if not word:
        break
    if word in words:
        print("单词已存在")
    else:
        r = requests.get(url.format(word))
        d = json.loads(r.text)
        if not d.get("word_name"):
            print("not a word")
        else:
            words.append(word)
            ph_en = d["symbols"][0]["ph_en"]
            parts = d["symbols"][0]["parts"]
            means = "".join([i["part"] + "".join(i["means"]) for i in parts])
            worditem = word+'\t['+ph_en+']'+means+'\t'+str(datetime.date.today())
            print(worditem)
            f.write(worditem + '\n')
            f.flush()
    print("已记录{}个单词/词组".format(len(words)))
    print()
f.close()

   
  
