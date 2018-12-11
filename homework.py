# -*- coding: UTF-8 -*-
import datetime
filename = r"C:\Users\nttzl\Desktop\words.txt"

def read_file():
    with open(filename,'r') as f:
        con = f.readlines()
        return con
def add_word(wd):
    with open(filename,'a+') as f:
        f.write(wd+"\t"+str(datetime.date.today())+"\n")

def main():
    count = 0
    wd=input("请输入你要记录的单词(直接回车退出程序):").strip()
    print(wd)
    con = read_file()
    n = len(con)
    if wd == "":
        exit(0)
    for i in con:
        if wd in i:
            print("单词已存在")
            count = 1
    
    if count == 0:
        add_word(wd)
    print("已记录{}个单词/词组".format(n+1-count))
    print()
   
  
if __name__ == "__main__":
    while True:
        main()
