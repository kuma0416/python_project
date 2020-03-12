import matplotlib.pyplot as plt  # 顯示圖片
import matplotlib.image as mpimg  # 讀取圖片
import numpy as np
import random
import time
import os
import sys
import tkinter as tk
from tkinter import filedialog   # 檔案位置
import tkinter.messagebox   # 各種訊息跳出框
import shutil
import glob
import matplotlib
from shutil import copyfile
from matplotlib.font_manager import FontProperties

matplotlib.font_manager._rebuild()

pathdir = os.path.abspath('.')  # get絕對路徑
path_p = 'pictrue'
path_d = 'data'
MF = 'not'
FN = 'not'
isExploreFavor = 'n'

# create window

window = tk.Tk()
window.title('古蹟保存系統')
window.geometry("600x550")

# Label

tk.Label(window, text='古蹟保存系統', font=("標楷體", 15)).place(x=0,y=0)
tk.Label(window, text='古蹟名: ', font=("標楷體")).place(x=0,y=55)
tk.Label(window, text='古蹟位址： ', font=("標楷體")).place(x=0,y=80)
tk.Label(window, text='古蹟年代： ', font=("標楷體")).place(x=0,y=105)
tk.Label(window, text='enter info： ', font=("標楷體")).place(x=0,y=130)
tk.Label(window, text='Info： ', font=("標楷體")).place(x=0,y=155)

# Entry

e1 = tk.Entry(window, width=40)
e1.place(x=100,y=55)
e2 = tk.Entry(window, width=40)
e2.place(x=100,y=80)
e3 = tk.Entry(window, width=40)
e3.place(x=100,y=105)
e4 = tk.Entry(window, width=40)
e4.place(x=100,y=130)

# Text
t = tk.Text(window, width=35, font=("標楷體"))
t.place(x=100,y=155)

# function

def del_text():
    e1.delete(0,tk.END)
    e2.delete(0,tk.END)
    e3.delete(0,tk.END)
    e4.delete(0,tk.END)
    t.delete(0.0,tk.END)  # 0.0表示地0行第0個元素
    tk.messagebox.showinfo('訊息', "成功清除訊息欄")

def count_files():
    files_path = os.path.join(pathdir, path_p)
    files_grab = []
    #types = ('*.jpg','*.PNG','*.png','*.GIF')
    for ext in ('*.jpg', '*.PNG', '*.png', '*.GIF'):
        files_grab.extend(glob.glob(os.path.join(files_path, ext)))  # glob.glob代表從該路徑中尋找所有符合的項目
    return files_grab

def explore():
    e1.delete(0,tk.END)
    e2.delete(0,tk.END)
    e3.delete(0,tk.END)
    e4.delete(0,tk.END)
    t.delete(0.1,tk.END)
    file_list = count_files()  # 找出\picture中所有符合jpg.png.gif的檔案並用串列打包
    num = random.randint(1, len(file_list))  # 在file_list的長度大小間找亂數
    temp = file_list[num - 1]  # 加算0所以要-1
    name = os.path.basename(temp).split('.')[0]  # 分割字串，獲取檔名
    e1.insert(tk.END, '' + name)
    global MF
    global FN
    FN = str(name)
    MF = os.path.join(pathdir, path_d, name + '.txt')
    # basename只會return文件名稱(檔名加副檔名)，dirname則是回傳所在路徑
    # print("\t探索的目的為 : " + name)

    # 顯示圖片
    pic = mpimg.imread(os.path.join(pathdir, path_p, name + '.jpg'))  # 圖片路徑
    pic.shape
    plt.imshow(pic)
    plt.axis('off')  # 不顯示座標
    plt.ion()
    plt.pause(0.1)

    fp = open(os.path.join(pathdir, path_d, name + '.txt'), 'r', encoding='utf8')

    for content in fp:
        if(content == 'ADDRESS:\n'):
            e2.insert(tk.END, '')
            content = fp.readline()
            e2.insert(tk.END, '\n' + content.rstrip())
        elif(content == 'YEAR:\n'):
            e3.insert(tk.END, '')
            content = fp.readline()
            e3.insert(tk.END, '\n' + content.rstrip())
        elif(content == 'INFO:\n'):
            t.insert(tk.END, "")
            content = fp.readline()
            t.insert(tk.END, '' + content.rstrip() + '\n')
    fp.close()
    # plt.close()

def explore_favorite():
    e1.delete(0,tk.END)
    e2.delete(0,tk.END)
    e3.delete(0,tk.END)
    e4.delete(0,tk.END)
    t.delete(0.1,tk.END)
    file_list = count_files()
    num = random.randint(1, len(file_list))  # 亂數
    temp = file_list[num - 1]
    name = os.path.basename(temp).split('.')[0]  # 分割字串
    # print("\t探索的目的為 : " + name)

    global isExploreFavor
    isExploreFavor = 'y'

    check=os.listdir(os.path.join(pathdir, 'favorite'))
    global FN
    global MF
    print(check)

    if len(check) == 0 :
        tk.messagebox.showerror(title='錯誤', message='沒有我的最愛')
    else :
        # 顯示簡介
        randfavor = random.randint(1, len(check)) - 1  # 亂數
        print('fa :', check[randfavor])
        e1.insert(tk.END, '' + check[randfavor].split('.')[0])
        fp = open(os.path.join(pathdir, 'favorite', check[randfavor]), 'r', encoding='utf8')
        FN=str(check[randfavor].split('.')[0])
        MF=str(os.path.join(pathdir, path_d, check[randfavor].split('.')[0]))
        print(MF)
        # 顯示圖片
        pic = mpimg.imread(os.path.join(pathdir, path_p, check[randfavor].split('.')[0] + '.jpg'))  # 圖片路徑
        pic.shape
        plt.imshow(pic)
        plt.axis('off')  # 不顯示座標
        plt.ion()
        plt.pause(0.1)

        for content in fp:
            if(content == 'ADDRESS:\n'):
                e2.insert(tk.END, '')
                content = fp.readline()
                e2.insert(tk.END, '\n' + content.rstrip())
            elif(content == 'YEAR:\n'):
                e3.insert(tk.END, '')
                content = fp.readline()
                e3.insert(tk.END, '\n' + content.rstrip())
            elif(content == 'INFO:\n'):
                t.insert(tk.END, "")
                content = fp.readline()
                t.insert(tk.END, '' + content.rstrip() + '\n')
        fp.close()
        # plt.close()

def add_favorite():
    print(MF)
    print(FN)
    global isExploreFavor
    isExploreFavor = 'n'
    favorite_list = os.listdir(os.path.join(pathdir, 'favorite'))
    print('favorite list:', favorite_list, '\n')
    for favorite in favorite_list:
        if FN == favorite.split('.')[0]:
            isExploreFavor = 'y'
    if MF == 'not':
        tk.messagebox.showerror(title='錯誤', message='尚未探索')
    elif isExploreFavor == 'y':
        tk.messagebox.showerror(title='錯誤', message='已經加入最愛')
    else:
        try:
            shutil.copyfile(MF, os.path.join(pathdir,'favorite',FN+'.txt'))
            tk.messagebox.showinfo(title='訊息', message='已加入最愛')

        except Exception as e:
            tk.messagebox.showerror(title='錯誤', message='路徑錯誤')
    
def add():
    if(e1.get() == '' or e2.get() == '' or e3.get() == '' or e4.get() == ''):
        t.insert(tk.END, '\n\t請輸入完整資料\n')
        tk.messagebox.showerror(title='錯誤', message='請輸入完整資料')
        return
    elif(e3.get().isdigit() == False):
        t.insert(tk.END, '\n年代需為數字!請重新輸入\n')
        tk.messagebox.showerror(title='錯誤', message='年代需為數字!請重新輸入')
        return
    t.insert(tk.END, '\n\t請上傳圖片\n')
    tk.messagebox.showinfo(title='訊息', message='請上傳圖片')
    fpath = filedialog.askopenfilename(defaultextension='.jpg',
    filetypes=[('All files', '*.*'),('PNG pictures', '*.png'), ('JPEG pictures', '*.jpg')])  # 開啟檔案的視窗
    temp1 = fpath
    print("fpath:" + fpath)
    if(temp1 == ""):  # if沒上傳檔案
        t.insert(tk.END, "\n\t上傳取消\n")
        tk.messagebox.showwarning(title='警告', message='上傳取消')

    else:
        lname = temp1.split('.')[1]  # 副檔名，因為會回傳一個串列，所以找第二個即為副檔名
        fcopy = os.path.join(pathdir, path_p, e1.get() + '.' + lname)    # 把當前路徑以及未來要添加進去的資料夾名稱合併
        try:
            shutil.copyfile(fpath, fcopy)    # 使用try...except...(finally)把圖片copy到fcopy這個目的地

        except BaseException:    # 例外(error)狀況
            # print("\t無法上傳圖片!")
            t.insert(tk.END, "\t無法上傳圖片!\n")
        # print("\t上傳成功!")
        t.insert(tk.END, "\n\t上傳成功!\n")
        tk.messagebox.showinfo(title='訊息', message='上傳成功!')

        file = open(os.path.join(pathdir, path_d, e1.get() + ".txt"), 'w')  # 開一個新的txt

        # 把String寫進檔案
        file.write("NAME:\n" + e1.get() + "\n\n")
        file.write("ADDRESS:\n" + e2.get() + "\n\n")
        file.write("YEAR:\n" + e3.get() + "\n\n")
        file.write("INFO:\n" + e4.get() + "\n\n")
        file.close()

def delete():

    flag = True
    try:
        os.remove(os.path.join(pathdir, path_d, e1.get() + ".txt"))
    
    except BaseException:
        t.insert(tk.END, "\n\t無法刪除資料檔案!\n")
        tk.messagebox.showerror(title='錯誤', message='無法刪除資料檔案')
        flag = False

    # 因為不能確定圖片副檔名，所以用glob來找特定名稱的檔案
    dle_pname = os.path.join(pathdir, path_p, e1.get() + '.*')
    str1 = ''.join(glob.glob(dle_pname))  # list轉成string
    try:
        os.remove(str1)
    except BaseException:
        t.insert(tk.END, "\n\t無法刪除圖片檔案!\n")
        tk.messagebox.showerror(title='錯誤', message='無法刪除圖片檔案')
        flag = False

    if flag:
        t.insert(tk.END, "\n\t圖片和資料刪除成功\n")
        tk.messagebox.showinfo(title='訊息', message='成功刪除圖片和資料')

    else:
        t.insert(tk.END, "\n圖片和資料至少有一個沒刪除成功\n")
        tk.messagebox.showwarning(title='警告', message='圖片和資料至少有一個沒刪除成功')

# button

button1 = tk.Button(window, text ='探索', command = explore, width = 10).place(x=0,y=25)
button2 = tk.Button(window, text='新增', command=add, width = 10).place(x=100,y=25)
button3 = tk.Button(window, text='刪除', command=delete, width = 10).place(x=200,y=25)
button4 = tk.Button(window, text='清除訊息', command=del_text, width = 10).place(x=300,y=25)
button5 = tk.Button(window, text='加入最愛', command=add_favorite, width = 10).place(x=400,y=25)
button6 = tk.Button(window, text='探索最愛', command=explore_favorite, width = 10).place(x=500,y=25)

window.mainloop()
