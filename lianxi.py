
def digui(n):
    y=''
    if n:
        y=digui(n//2)
        return y+str(n%2)





def getdigit(n):
    y=[]
    if n:
        y=getdigit(n//10)
        y.append(n%10)
        return y
    else:
        return y

def zhuce(n,m):
    conculution={n:m}
    return conculution



def password(k):
    for u in range(3):
        i=input('请输入用户名：')
        if i in k:
            b=input('请输入密码:')
            if b in k[i]:
                print('密码正确，开始启动。')
                break
            else:
                print('密码错误，请重新输入')
                print('还有%d次机会' % (2 - u))
        else:
            print('用户名错误，请重新输入')
            print('还有%d次机会' % (2 - u))




def shuru(x):
    file=open(x,'w')
    print('请输入内容【单独输入\':w\'保存退出】:')
    while True:
        y=input()
        if y!=':w':
            file.write('%s\n'%y)
        else:
            break
    file.close()

import os
#统计各类型文件夹和文件数量
def leixing():
    path=os.listdir(os.curdir)
    dicttype=dict()
    for eachfile in path:
        if os.path.isdir(eachfile):
            dicttype.setdefault('文件夹',0)
            dicttype['文件夹']+=1
        else:
            ext=os.path.splitext(eachfile)[1]
            dicttype.setdefault(ext,0)
            dicttype[ext]+=1
    for eachtype in dicttype.keys():
        print('类型为[%s]的文件有%d个'%(eachtype,dicttype[eachtype]))

#得到文件大小
def filesize():
    path=os.listdir(os.curdir)
    typesize=dict()
    for eachfile in path:
        if os.path.isfile(eachfile):
            size=os.path.getsize(eachfile)
            typesize.setdefault(eachfile,size)
    for each in typesize:
        print('类型为%s的文件大小为%dKB'%(each,typesize[each]))

import os

#查找所有文件名并打印
def findpath(startdir,target):
    os.curdir(startdir)
    file=os.listdir(os.curdir)
    for eachfile in file:
        if os.path.isfile(eachfile):
            if eachfile==target:
                print(os.getcwd()+os.sep+target)
        if os.path.isdir(eachfile):
            findpath(eachfile,target)
            os.curdir(os.pardir)


#查找指定类型文件的路径
def chazhaolujing(startdir,target):
    os.curdir(startdir)
    file=os.listdir(os.curdir)
    for eachfile in file:
        if os.path.isfile(eachfile):
            ext=os.path.splitext(eachfile)[1]
            if ext in target:
                return (os.getcwd()+os.sep+ext+os.linesep)
        if os.path.isdir(eachfile):
            chazhaolujing(eachfile,target)
            os.chdir(os.pardir)




#找到含有指定关键字的文件并定位
def searchfile(a,):
    i=os.walk(os.getcwd())
    key_value=dict()
    for each in i:
        for eachfile in each[2]:
            if os.path.isfile(eachfile):
                ext=os.path.splitext(eachfile)[1]
                if ext=='.txt':
                    key_value[a]=(os.getcwd()+os.sep+eachfile+ext)
                    print('在文件【%s】中找到关键字%s'%(key_value[a],a))
                    filetxt=open(eachfile)
                    lines=filetxt.readlines()
                    count=0
                    for eachline in lines:
                        pos = []
                        count+=1
                        if a in eachline:
                            target=eachline.find(a)
                            while target!=-1:
                                pos.append(target+1)
                                target=eachline.find(a,target+1)
                            print('关键字出现在第%s行，第%s个位置'%(count,pos))





def int_input():
    n=input('请输入一个整数：')
    try:
        z=int(n)
        return z
    except(ValueError):
        print('出错，请重新输入')
        int_input()

import random
import easygui as g



#图形界面猜数字小游戏
def cashuzi():
    g.msgbox('欢迎进入第一个小游戏')
    secret=random.randint(1,10)
    guess=g.integerbox(msg='请输入1-10的数字',title='猜数字小游戏',lowerbound=1,upperbound=10)
    while True:
        if guess==secret:
            g.msgbox('你是小甲鱼肚子里的蛔虫吗')
            g.msgbox('猜对了也没有奖励哦')
            break
        else:
            if guess>secret:
                g.msgbox('大了大了')
            else:
                g.msgbox('小了小了')
            guess = g.integerbox(msg='请输入1-10的数字', title='猜数字小游戏', lowerbound=1, upperbound=10)
    g.msgbox('游戏结束不玩了哦')

def denglu():
    msg='''【*真实姓名】为必填项
           【*手机号码】为必填项
           【*E-mail】为必填项'''
    title='账号中心'
    filename=['*用户民','*真实姓名','固定电话','*手机号码','QQ','*E-mail']
    z=g.multenterbox(msg,title,filename)
    L=len(filename)
    for each in L:
        if '*' in filename[each]:
            if z[each]==None:
                break



#查询指定文件夹的程序数目
def search(startdir):
    os.chdir(startdir)
    l=os.listdir(os.curdir)
    z=0
    k=0
    target = {'.c': 0, '.py': 0, '.java': 0}
    lines={'.c':0,'.py':0,'.java':0}
    for eachfile in l:
        if os.path.isdir(eachfile):
            search(eachfile)
        if os.path.isfile(eachfile):
            f=open(eachfile,'rb')
            for eachline in f:
                k+=1
            z+=k
            ext=os.path.splitext(eachfile)[1]
            if ext in target.keys():
                target[ext]+=1
                lines[ext]+=k
    return target,lines,z
def show(target,lines,z):
    msg='''您目前共累计编写了%d行代码，完成进度:%f 
           离十万行代码还差%d行'''%(z,z/100000,(100000-z))
    title='统计结果'
    text=''
    for each in target.keys():
        text+='【%s】源文件%d个，源代码%d行'%(each,target[each],lines[each])
    g.textbox(msg=msg,title=title,text=text)
# msg='请选择你的数据库：'
# title='浏览文件夹'
# g.msgbox(msg,title)
# startdir=g.diropenbox('请选择你的代码库')
# a,b,c=search(startdir)
# show(a,b,c)


#定义一个类打印名字
class Person:
    name='贺鹏艺'
    def printname(self):
        print(self.name)




#矩形类求面积
class juxing:
    def __init__(self):
        length=0
        width=0
    def setRect(self):
        a=float(input('矩形长为：'))
        b=float(input('矩形宽为：'))
        self.length=a
        self.width=b
    def getRect(self):
        print('矩形长度为%d'%self.length)
        print('矩形宽度为%d'%self.width)
    def getArea(self):
        try:
            self.area=self.width*self.length
            print('矩形的面积为%d'%self.area)
        except:
            print('没有设定长和宽')
# f=juxing()
# f.setRect()
# f.getArea()


#计算游乐园售票价格
class price:
    normal=100
    special=normal*1.2
    def monday_to_frieday(self):
        a = int(input('成人数量:'))
        b = int(input('小孩数量:'))
        price=self.normal*a+0.5*self.normal*b
        print('票价为：%d元'%price)
    def saturday_to_sunday(self):
        a = int(input('成人数量:'))
        b = int(input('小孩数量:'))
        price=self.special*a+0.5*self.special*b
        print('票价为：%d元' % price)


# p=price()
# p.monday_to_frieday()

###龟龟捕鱼小游戏
#定义鱼类
class fish:
    x=random.randint(0,10)
    y=random.randint(0,10)

    def move(self):
        self.y+=random.choice([-1,1])
        self.x+=random.choice([-1,1])
        z=(self.x,self.y)
        return z
#定义龟类
class turtle:
    x = random.randint(0, 10)
    y = random.randint(0, 10)
    power=100

    def move(self):
        self.y+=random.choice([-1,-2,1,2])
        self.x+=random.choice([-1,-2,1,2])
        self.power-=1
        z = (self.x, self.y)
        return z
killerscreen=turtle()
fishs=[]
for i in range(10):
    newfish=fish()
    fishs.append(newfish)

# while True:
#     if not len(fishs):
#         print('鱼儿都吃完了，游戏结束')
#         break
#     if not turtle.power:
#         print('乌龟体力耗尽了')
#         break
#     for eachfish in fishs:
#         a = eachfish.move()
#         b = killerscreen.move()
#         if a == b:
#             killerscreen.power += 20
#             print('鱼%s被吃掉了' % eachfish)
#             fishs.remove(eachfish)



#定义直线断点并计算直线长度
import math as m

class point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def getx(self):
        return self.x
    def gety(self):
        return self.y

class line:
    def __init__(self,p1,p2):
        self.y1=p1.getx()-p2.getx()
        self.y2=p1.gety()-p2.gety()
        self.lengh=m.sqrt(self.y1**2+self.y2**2)
    def getlength(self):
        return self.lengh
# p1=point(4,5)
# p2=point(1,3)
# l=line(p1,p2)
# z=l.getlength()
# print(z)



#摄氏度转换为华氏度
###第一种方法
class convert:
    def gethuashi(self,x):
        self.x=x*1.8+32
        return self.x
C2F=convert()
print(C2F.gethuashi(32))

###第二种方法
class C2F(float):
    def __new__(cls, arg=0.0):
        return float.__new__(cls,arg*1.8+32)
print(C2F(32))


#转化字符串为ASC码然后求和
class str_to_ASC(int):
    def __new__(cls, x=0):
        if isinstance(x,str):
            z=0
            for each in x:
                z+=ord(each)
        return int.__new__(cls,z)
###实例化
ASC=str_to_ASC(x='dsdkfkj')
print(ASC)


#字符串相减操作
class Nstr(str):
    def __sub__(self, other):
        return self.replace(other,'')



class nstr(str):
    def __init__(self,x):
        self.x=x
        self.total=0
        for each in self.x:
            self.total+=ord(each)
    def __sub__(self, other):
        return self.total-other.total
    def __add__(self, other):
        return self.total+other.total
    def __mul__(self, other):
        return self.total*other.total
    def __truediv__(self, other):
        return self.total/other.total
    def __floordiv__(self, other):
        return  self.total//other.total

# a=nstr('fsdffds')
# b=nstr('euiur')
# print(a+b)



#统计实例化数目的类
class count_class:
    count=0
    def __init__(self):
        count_class.count+=1
    # def get_count(self):
    #     return count_class.count

a=count_class()
b=count_class()
print(count_class.count)


#统计输入参数数目的类
# class count_arg:
#
#     def __init__(self,*args):
#         if not args:
#             print('没有输入参数')
#         else:
#             print('输入了%d个参数'%len(args))
#             for each in args:
#                 print(each,end=' ')
# a=count_arg(1,3,4,5)



#####定义华氏度和摄氏度且能转换
class Celsius:
    def __init__(self,value=26.0):
        self.value=float(value)
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        self.value=float(value)
class Fahrenheit:
    def __get__(self, instance, owner):
        return instance.cel*1.8+32
    def __set__(self, instance, value):
        instance.cel=(float(value)-32)/1.8
class Temprature:
    cel=Celsius()
    fah=Fahrenheit()

class  Countlist:
    def __init__(self,*args):
        self.values=[x for x in args]
        self.count={}.fromkeys(range(len(self.values)),0)
    def __len__(self):
        return len(self.values)
    def __getitem__(self, key):
        self.count[key]+=1
        return self.values[key]

#有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
a=[1,2,3,4]
def count_third_num(a):
    total=[]
    for i in a:
        for y in a:
            for z in a:
                if i!=y and y!=z and i!=z:
                    total.append(i*100+y*10+z)
    l=len(total)
    print('能组成%d个互不相同且无重复数字的三位数,各是'%l,end='')
    for i in total:
        print(i,end=' ')
count_third_num(a)


#企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，
# 低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？
def money(I):
    target=0
    price=[10e5,6e5,4e5,2e5,1e5,0]
    rate=[0.01,0.015,0.03,0.05,0.075,0.1]
    for i in range(6):
        if I>price[i]:
            target+=(I-price[i])*rate[i]
            I=price[i]
    print(target)
money(10.9e5)


