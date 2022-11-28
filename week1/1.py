import numpy as np
import pandas as pd
import difflib
from tkinter import *
import time 
import os
import shutil


basedata="data.txt" #(需要格式清理 只保留需要的地方) 保存为txt文件
screenshot="screenshot.txt" #(逐行读取 需要格式清理，在excel中去除中文) 需要转化输出为保存为txt文件

##识别文字，最好一行保留eid和姓名。
##https://github.com/hiroi-sora/Umi-OCR



def callback1():
    global click 
    click = True
    #time.sleep(1)
    root.destroy()
    
def callback2():
    global click 
    click = False
    #time.sleep(1)
    root.destroy()    
    

def callback3():
    global click 
    click = False
    #time.sleep(1)
    root.destroy() 
    print("EXIT, Programm Finished by you!  Jiaao Wang@Henkelman Group")
    sys.exit()

#####manual函数 输入一段文字 如果点yes,函数返回yes，如果点no 函数返回False.
def manual(text):
    #####输入一段文字 如果点yes,函数返回yes，如果点no 函数返回False.   
    ###打字到屏幕
    global root
    root = Tk()
    root.geometry("500x500+400+200")
    frame1 = Frame(root)
    frame2 = Frame(root)
    var = StringVar()
    var.set(text)
    var1 = StringVar()
    var1.set("Jiaao@ Henkelman Group _ UT Austin")
    textLabel = Label(frame1,textvariable=var,justify=LEFT)
    textLabel1 = Label(frame2,textvariable=var1,justify=LEFT)#左对齐
    textLabel.pack()
    textLabel1.pack()
    theButton1 = Button(frame1, text='Yes', command=callback1)
    theButton2 = Button(frame1, text='No', command=callback2)
    theButton3 = Button(frame2, text='QUIT', command=callback3)
    theButton1.pack()
    theButton2.pack()
    theButton3.pack()
    frame1.pack(padx=30, pady=30)
    frame2.pack(padx=30, pady=30)
    mainloop() 
    
    ##选择后传入值(click)关闭
    
    if click==True:
        result=True
    
    else:
        
        result=False
    return result









###ss 函数是文本相似性比较

def ss(s1,s2):
    return difflib.SequenceMatcher(None, s1,s2).quick_ratio()



#df=pd.read_csv("1.csv", encoding='utf-8',header=0)

#df=np.loadtxt("1.csv")

#打开库文本（一行就是一个学生信息）



with open(basedata) as f:
    data=f.readlines()
    
#打开学生的截图文本，得到学生信息
with open(screenshot) as f:
    screen=f.readlines()










####comapare (text测试文本和库list文本)返回最可能的相似性的东西
def compare(text,base):
    valuelist=[0]
    maxindex=0
    for i in range(len(base)):


        value=ss(text,base[i])
        #print(str("\n"+text))
        #print(base[i])

        if value > max(valuelist):
            maxvalue=value
            maxindex=i
            
        else:
            maxvalue=max(valuelist)
        
        valuelist.append(value)
        

    if maxvalue>=0.65:######################################
        
        student=base[maxindex]
        print("Student match, take it into sign up sheet!")
        
    elif maxvalue<0.65 and maxvalue>0.4 :
        
        
        print("Wait for Manual determination...")
        
        if manual(str(maxvalue)+str("\n"+text)+str(base[maxindex]))==True:
            
            student=base[maxindex]
        
        else:
        
            student=None
    
    else:
        
        student=None
        
    #print(student)
    return student
    
        
        
        


####得到signed_student文件

with open("signed_student", "a+") as f:
    f.truncate(0)

for i in range(len(screen)):
    finished_stu=compare(screen[i],data)
    
    if finished_stu!=None:
        print(finished_stu)
        
        
        
        ####探测库
        
        ####如果有 那么在原来的库中加 x 
        ####复制一个新的库命名signed_student 然后如果匹配就在行尾加 x
        
        with open("signed_student", "a+") as f:
            #f.truncate(0)
            f.writelines([str(finished_stu)])
            
            
            
            
            
        
        
        
        
###数据输出

if os.path.exists("student_sheet_new"):
    print("Read signed_student.")
    
#####

else:
    ff=open("student_sheet_new","a+")
    ff.truncate(0)
    with open(basedata) as f:
        student_list=f.readlines()
        
    
    for line_list in student_list:
        
        print(line_list)
        
        
        if "	x\n" in line_list:
            print("x there, change to marked_x")
            line_new = line_list.replace('x\n','')
            line_new = line_new+r'marked_x'+'\n'  #行末尾加上"|",同时加上"\n"换行符
            print(line_new)
            ff=open("student_sheet_new","a+")
            ff.write(line_new)
            
        
        elif line_list in open("signed_student").readlines(): ###如果学生行在存在文件中的某行
            
            print("yes")
            
            line_new = line_list.replace('\n','')
            line_new = line_new+r'marked_x'+'\n'  #行末尾加上"|",同时加上"\n"换行符
            print(line_new)
            ff=open("student_sheet_new","a+")
            ff.write(line_new)
            
        else:
            print("no change")
            line_new = line_list
            ff=open("student_sheet_new","a+")
            ff.write(line_new)
    
    







        
        
#     #print(screen[i])

    
# #print(df)