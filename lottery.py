# -*- coding: utf-8 -*-  
__author__ = 'wangyang'
from Tkinter import *   #引入Tkinter工具包
import os
import random

this_file_path = os.path.split(os.path.realpath(__file__))[0] + '\\';

print this_file_path
def hello():
    print('hello world!')


# def main():
# 	win = Tk()  #定义一个窗体
# 	win.title('Hello World')    #定义窗体标题
# 	win.geometry('800x600')     #定义窗体的大小，是400X200像素

# 	begin_btn = Button(win, text='开始' ,height = 4, width = 6, command=hello)
# 	#注意这个地方，不要写成hello(),如果是hello()的话，
# 	#会在mainloop中调用hello函数，
# 	# 而不是单击button按钮时出发事件
# 	begin_btn.pack(expand=NO, fill=X, side=BOTTOM) #将按钮pack，充满整个窗体(只有pack的组件实例才能显示)

# 	end_btn = Button(win, text='结束' ,height = 4, width = 6, command=hello)
# 	#注意这个地方，不要写成hello(),如果是hello()的话，
# 	#会在mainloop中调用hello函数，
# 	# 而不是单击button按钮时出发事件
# 	end_btn.pack(expand=NO, fill=X, side=BOTTOM) #将按钮pack，充满整个窗体(只有pack的组件实例才能显示)

# 	ans_label = Label(win,text = '中奖的人', height = 10 , width = 10 );

# 	ans_label.pack();
# 	mainloop() #进入主循环，程序运行

user_list = [];

def read_from_file(filename):
    file_handle = open(this_file_path + filename)
    # if file_handle == null:
    # 	return;
    line = file_handle.readline()

    while len(line) > 0 :
        line = line.rstrip('\r\n')
        line = line.replace('\n','')
        line = line.replace('\r','')
        user_list.append(line)
        print line
        line = file_handle.readline()

    file_handle.close()

def choose_next():
    num = len(user_list)
    rand = random.randint(0, num - 1)
    chosen_user = user_list[rand]
    del user_list[rand]
    return chosen_user

def main():
    read_from_file('test.txt')
    print user_list

    print choose_next();
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
