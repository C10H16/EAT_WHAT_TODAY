#-*- coding:utf8 -*-
import random

def main():
    print ("早饭请按1\n午饭请按2\n晚饭请按3")
    while 1:
        a = input()
        if a=='1':
            fi = open("breakfast.txt",'r', encoding='utf8')
            break
        elif a=='2':
            fi = open("lunch.txt",'r', encoding='utf8')
            break
        elif a=='3':
            fi = open("dinner.txt",'r', encoding='utf8')
            break
        else:
            print ("没有夜宵\n,请重新输入！")
    meal_list = []
    start = 0
    end = 0
    while(1):
        line = fi.readline()
        if not line:
            break
        line = line.strip()
        meal, factor = line.split()
        start = end
        end += int(factor)
        for i in range(start, end):
            meal_list.append(meal)
    
    i = 'r'
    while(i=='r'or i=='R'):
        print("\n今天吃:\n\t", meal_list[random.randint(0,end-1)],"\n")
        i = input("按r/R再试一次，其他任意键退出")
    fi.close()

if __name__=="__main__":
    main()
