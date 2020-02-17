#coding=utf-8

import tkinter as tk
import tkinter.filedialog
import cv2


def choose_file():  # 选择文件
    selectFileName = tk.filedialog.askopenfilename(title='选择文件')
    e.set(selectFileName)


def show(e_entry):  # 显示图片
    img = cv2.imread(e_entry.get())
    cv2.imshow("PICTURE", img)
    cv2.waitKey(0)


def window():
    root = tk.Tk()
    root.geometry('650x450+150+100')
    root.title('test')
    root.resizable(False, False)

    global e
    e = tk.StringVar()  # 文本输入框
    e_entry = tk.Entry(root, width=68, textvariable=e)
    # e_entry.pack()

    # 选择文件控件
    sumbit_btn = tk.Button(root, text="选择文件", bg='yellow', command=choose_file)
    sumbit_btn.pack()
    # 展示文件控件
    show_btn = tk.Button(root, text='查看图片', bg='blue', \
                         command=lambda: show(e_entry))
    show_btn.pack()

    root.mainloop()


window()