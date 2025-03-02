# official document

import tkinter as tk

# 创建窗口
window = tk.Tk()
window.title('Matsk On')
window.geometry("500x350")

# add_task()用于新建任务
def add_task():
    # 返回任务名称与番茄钟数
    task_name = e1.get()
    tomato_count = e2.get()

    # 判断名称合法性
    if not task_name or not tomato_count.isdigit():
        return
    
    # 输出格式
    task_text = f"\"{task_name}\"   ({tomato_count}*🍅)"
    
    # toggle_task()用于实现任务栏的复选
    def toggle_task():
        # 如果var不等于0（为1）
        if var.get():
            # 将文字划线
            label.config(fg="gray",font=("Segoe UI",10,"overstrike"))
            
        else:
            # 正常状态
            label.config(fg="gray",font=("Segoe UI",10,"normal"))


    ## 动态渲染的按钮
    # 用于包装bool值的变量
    var = tk.BooleanVar()
    # checkbutton绑定var变量，如果被触发，就执行toggle_task
    check = tk.Checkbutton(f1,variable=var,command=toggle_task)
    label = tk.Label(f1,text=task_text,font=("Segoe UI",10))

    # 参数含义anchor控制文本或者图像位置 ewsn东西南北也就是右左下上
    # 参数含义padx,pady指定垂直，水平方向上的内容与边框的间距
    label.pack(anchor="center",padx=5,pady=2)
    check.pack(anchor="w")

    f1.update_idletasks()

    e1.delete(0,tk.END)
    e2.delete(0,tk.END)

# 利用Frame动态生成任务列表
f1 = tk.Frame(window,bg='orange')
f1.grid(row=2,column=1,columnspan=3,sticky='w')  

## 定义一个按钮Button
b1 = tk.Button(window,
               text='新\nAdd',
               bg='red',
               font=('Segoe UI',12),
               width=10,height=2,
               command=add_task).grid(row=1,column=0)
# 记得自定义执行指令'command=run'

## 输入提示词
l1 = tk.Label(window,
              text='任务名称：',
              bg='gold',
              font=('Cascadia Code',12),
              width=10,height=1).grid(row=0,column=0)
## 任务名称输入文本框
e1 = tk.Entry(window,bg='ghost white',font=('Segoe UI',10))
e1.grid(row=0,column=1)

## 输入提示词
l2 = tk.Label(window,
              text='番茄时钟数',
              bg='gold',
              font=('Cascadia Code',12),
              width=10,height=1).grid(row=0,column=2)
## 番茄钟数输入文本框
e2 = tk.Entry(window,bg='ghost white',font=('Segoe UI',10))
e2.grid(row=0,column=3)

## 主栏提示‘任务’
l3 = tk.Label(window,
              text='任务\nTask',
              bg='gold',
              font=('Segoe UI',15),
              width=8,height=10).grid(row=2,column=0)


# 执行窗口
window.mainloop()


