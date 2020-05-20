
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

def



