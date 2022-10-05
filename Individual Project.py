from random import randint
file=open("Exercises.txt",'w',encoding='utf-8')
file1=open("Answers.txt",'w',encoding='utf-8')
number=eval(input("请输入生成题目的个数:"))
ls=[]
i=0
while i<number:
    SymbolNumber=randint(1,2)
    if SymbolNumber==1:
        s=randint(0,1)
        if s==0:
            x1=str(randint(0,100))
            x2=str(randint(0,100-int(x1)))
            if (x1,"+",x2) not in ls:
                ls.append((x1,"+",x2))
                i=str(i+1)
                file.write(i+"."+"四则运算题目"+i+" "+x1+"+"+x2+"=\n")
                file1.write(i+"."+"答案"+i+" "+str(int(x1)+int(x2))+"\n")
                i=int(i)
        else:
            x1=str(randint(0,100))
            x2=str(randint(0,int(x1)))
            if (x1,"-",x2) not in ls:
                ls.append((x1,“-”，x2))
                i=str(i+1)
                file.write(i+"."+"四则运算题目"+i+" "+x1+"-"+x2+"=\n")
                file1.write(i+"."+"答案"+i+" "+str(int(x1)-int(x2))+"\n")
                i=int(i)

    if SymbolNumber==2:  
        s1=randint(0,1)
        s2=randint(0,1)
        if s1==0 and s2==0:
            x1=str(randint(0,100))
            x2=str(randint(0,100-int(x1)))
            x3=str(randint(0,100-int(x1)-int(x2)))
            if (x1,"+",x2,"+",x3) not in ls:
                ls.append((x1,"+",x2,"+",x3))
                i=str(i+1)
                file.write(i+"."+"四则运算题目"+i+" "+x1+"+"+x2+"+"+x3+"=\n")
                file1.write(i+"."+"答案"+i+" "+str(int(x1)+int(x2)+int(x3))+"\n")
                i=int(i)
        elif s1==0 and s2==1:
            x1=str(randint(0,100))
            x2=str(randint(0,100-int(x1)))
            x3=str(randint(0,int(x1)+int(x2)))
            if (x1,"+",x2,"-",x3) not in ls:
                ls.append((x1,"+",x2,"-",x3))
                i=str(i+1)
                file.write(i+"."+"四则运算题目"+i+" "+x1+"+"+x2+"-"+x3+"=\n")
                file1.write(i+"."+"答案"+i+" "+str(int(x1)+int(x2)-int(x3))+"\n")
                i=int(i)
        elif s1==1 and s2==0:
            x1=str(randint(0,100))
            x2=str(randint(0,int(x1)))
            x3=str(randint(0,100-int(x1)+int(x2)))
            if (x1,"-",x2,"+",x3) not in ls:
                ls.append((x1,"-",x2,"+",x3))
                i=str(i+1)
                file.write(i+"."+"四则运算题目"+i+" "+x1+"-"+x2+"+"+x3+"=\n")
                file1.write(i+"."+"答案"+i+" "+str(int(x1)-int(x2)+int(x3))+"\n")
                i=int(i)
        else:
            x1=str(randint(0,100))
            x2=str(randint(0,int(x1)))
            x3=str(randint(0,int(x1)-int(x2)))
            if (x1,"-",x2,"-",x3) not in ls:
                ls.append((x1,"-",x2,"-",x3))
                i=str(i+1)
                file.write(i+"."+"四则运算题目"+i+" "+x1+"-"+x2+"-"+x3+"=\n")
                file1.write(i+"."+"答案"+i+" "+str(int(x1)-int(x2)-int(x3))+"\n")
                i=int(i)

file.close()
file1.close()
