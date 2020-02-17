#coding=utf-8
from tkinter import *
import cv2
import os
from PIL import Image, ImageTk

from tkinter import filedialog

def ReadVideo():
    global file_path
    global height
    global width

    file_path = filedialog.askopenfilename(title='Select the diagnostic instrument .exe file',filetypes=[('mp4', '*.mp4'), ('avi', '*.avi')], initialdir='./')
    cap = cv2.VideoCapture(file_path)
    cap.set(cv2.CAP_PROP_POS_FRAMES, 1)
    ret, frame = cap.read()
    global current_img
    current_img=frame
    [height, width, pixels] = frame.shape #获取视频的宽和高
    new_height =height # int(screenheight * 0.85)
    new_width=width #int(new_height *  width/height)

    image_page.place(x=0, y=0, width=new_width, height=new_height)
    print(new_height)
    print(new_width)

    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    current_image = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=current_image)
    show_img_label.imgtk = imgtk
    show_img_label.config(image=imgtk)

def calib_img():
    #root.pack_forget()  # 隐藏界面
    # cv2.imshow('frame',current_img)
    # out_win = "output_style_full_screen"
    # cv2.namedWindow(out_win, cv2.WINDOW_NORMAL)
    # cv2.setWindowProperty(out_win, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    # cv2.imshow(out_win, current_img)
    show_img_label.bind("<Button-1>", callback)
def callback(event):
    print("当前位置：",event.x,event.y)
    point_1_label_x["text"] = "x=" + str(event.x)
    point_1_label_y["text"] = "y=" + str(event.y)


if __name__ == '__main__':


    root = Tk()
    root.title('Calib')
    #root.geometry('%dx%d' % (800, 600))



    global screenwidth
    screenwidth= root.winfo_screenwidth() # 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
    global screenheight
    screenheight = root.winfo_screenheight()

    width = screenwidth#/1.5#800
    height = screenheight#/1.5#600
    root.geometry('%dx%d' % (width, height))
    root.attributes("-topmost", True)
    #alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    #root.geometry(alignstr)
    root.resizable(width=True, height=True)# 设置窗口是否可变长、宽，True：可变，False：不可变

    #page_top = Frame(root,width=width,bg='#090')
    #page_top.pack(side='left')
    #page1 = Frame(page_top,bg='#900')

    #page_two = Frame(root, bg='#900', )



    image_page = Frame(root,bg='#900')
    image_page.pack(side='top')
    image_page.place(x=0, y=0, width=1280, height=960)
    # Label(page2, text='车位标注工具', font=('粗体', 10)).pack()
    show_img_label = Label(image_page)
    show_img_label.pack(side='top',padx=5, pady=5)

    # information_page = Frame(bg='#0f0')
    # information_page.pack()
    # # Label(page2, text='车位标注工具', font=('粗体', 10)).pack()
    # show_img_label = Label(information_page, width=1280, height=720)
    # show_img_label.pack(padx=5, pady=5)

    page_one = Frame(root, bg='#0f0')
    page_one.pack(side='right', padx=20, pady=10)
    #page_one.place(width=500)
    label_one = Label(page_one, bg='#00f')
    label_one.pack(side='top', padx=0, pady=0)
    button_open_video = Button(label_one, text="打开视频", bg='#999', font=("宋", 18),relief='raise', command=ReadVideo)
    button_open_video.pack(side='left', padx=5, pady=10)
    calib_button = Button(label_one, text="开始标注", bg='#999', font=("宋", 18), padx=10, relief='raise', command=calib_img)
    calib_button.pack(side='left', padx=5, pady=10)

    label_two = Label(page_one, bg='#f4f')
    label_two.pack(side='top', padx=0, pady=0)
    pre_img_5 = Button(label_two, text="<<", bg='#999', font=("宋", 18),padx=10, relief='raise', command=ReadVideo)
    pre_img_5.pack(side='left', padx=5, pady=10)
    pre_img = Button(label_two, text="<", bg='#999', font=("宋", 18),padx=10, relief='raise', command=ReadVideo)
    pre_img.pack(side='left', padx=5, pady=10)

    next_img = Button(label_two, text=">", bg='#999', font=("宋", 18),padx=10, relief='raise', command=ReadVideo)
    next_img.pack(side='left', padx=5, pady=10)
    next_img_5 = Button(label_two, text=">>", bg='#999', font=("宋", 18),padx=10, relief='raise', command=ReadVideo)
    next_img_5.pack(side='left', padx=5, pady=10)

    label_three = Label(page_one, bg='#0ff',height=500,width=20)
    label_three.pack(side='top', padx=10, pady=10)

    point_1_label_x =Label(label_three,text="x=", bg='#0ff',font=("宋", 18))
    point_1_label_x.pack(side='left', padx=5, pady=10)
    point_1_label_y = Label(label_three, text="y=", bg='#0ff', font=("宋", 18))
    point_1_label_y.pack(side='left', padx=5, pady=10)


    #page_two = Frame(root,bg='#900')
    #page_two.pack(side='bottom', padx=10, pady=10)


    mainloop()



