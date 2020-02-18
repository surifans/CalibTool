#coding=utf-8
from tkinter import *
import cv2
import os
from PIL import Image, ImageTk

from tkinter import filedialog

def createSecondPage():
    video_play = 0
    file_path = filedialog.askopenfilename(title='Select the diagnostic instrument .exe file',
                                filetypes=[('mp4', '*.mp4'), ('avi', '*.avi')], initialdir='./')
    #file_path = filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser('H:/')))
    print(file_path)
    if file_path is not None:
        video_play = 1
        #root.after_cancel()
    #page_one.pack()
    cap = cv2.VideoCapture(file_path)

    #button21 = Button(page2, width=18, height=2, text="返回", bg='gray', font=("宋", 12),relief='raise', command=backFirst)
    #button21.pack(padx=25, pady=10)

    video_loop(data2,cap)

def video_loop(panela,cap_temp):
    ret, frame = cap_temp.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)  # 转换颜色从BGR到RGBA
    current_image = Image.fromarray(cv2image)  # 将图像转换成Image对象
    imgtk = ImageTk.PhotoImage(image=current_image)
    panela.imgtk = imgtk
    panela.config(image=imgtk)
    root.after(1, lambda: video_loop(panela,cap_temp))
    # if video_play==0:
    #     root.after_cancel()







if __name__ == '__main__':

    root = Tk()
    root.title('Calib')
    #root.geometry('%dx%d' % (800, 600))



    screenwidth = root.winfo_screenwidth() # 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
    screenheight = root.winfo_screenheight()

    width = screenwidth#screenwidth/1.5#800
    height = screenheight#screenheight/1.5#600
    root.geometry('%dx%d' % (width, height))
    root.attributes("-topmost", True)
    #alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    #root.geometry(alignstr)
    root.resizable(width=True, height=True)# 设置窗口是否可变长、宽，True：可变，False：不可变

    #page_top = Frame(root,width=width,bg='#090')
    #page_top.pack(side='left')
    #page1 = Frame(page_top,bg='#900')

    page_one = Frame(root)
    page_one.pack( side='bottom',padx=10, pady=10)

    page2 = Frame(width=1280, height=720)
    page2.pack()
    # Label(page2, text='车位标注工具', font=('粗体', 10)).pack()
    data2 = Label(page2, width=1280, height=720)
    data2.pack(padx=5, pady=5)

    video_play=0;
    button_open_video = Button(page_one, text="打开视频", bg='#999', font=("宋", 18),relief='raise', command=createSecondPage)
    button_open_video.pack(side='left', padx=5, pady=10)

    mainloop()



