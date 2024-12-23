from tkinter import *
root=Tk()
root.title("calculator")
inputcalc=Entry(root,width=75,borderwidth=1)
inputcalc.grid(row=0,columnspan=4,column=0)
index=0
def insert(number):
   global index
   inputcalc.insert(index,number)
   index+=1
def result():
    x=inputcalc.get()
    inputcalc.delete(0,END)
    inputcalc.insert(0,eval(x))
def clear():
    inputcalc.delete(0,END)
btn7=Button(root,text="7",padx=50,pady=50,command=lambda : insert("7")).grid(row=1,column=0)
btn8=Button(root,text="8",padx=50,pady=50,command=lambda : insert("8")).grid(row=1,column=1)
btn9=Button(root,text="9",padx=50,pady=50,command=lambda : insert("9")).grid(row=1,column=2)
btns=Button(root,text="+",padx=50,pady=50,command=lambda : insert("+")).grid(row=1,column=3)
btn4=Button(root,text="4",padx=50,pady=50,command=lambda : insert("4")).grid(row=2,column=0)
btn5=Button(root,text="5",padx=50,pady=50,command=lambda : insert("5")).grid(row=2,column=1)
btn6=Button(root,text="6",padx=50,pady=50,command=lambda : insert("6")).grid(row=2,column=2)
btnm=Button(root,text="-",padx=50,pady=50,command=lambda : insert("-")).grid(row=2,column=3)
btn1=Button(root,text="1",padx=50,pady=50,command=lambda : insert("1")).grid(row=3,column=0)
btn2=Button(root,text="2",padx=50,pady=50,command=lambda : insert("2")).grid(row=3,column=1)
btn3=Button(root,text="3",padx=50,pady=50,command=lambda : insert("3")).grid(row=3,column=2)
btnx=Button(root,text="x",padx=50,pady=50,command=lambda : insert("*")).grid(row=3,column=3)
btnc=Button(root,text="c",padx=50,pady=50 ,command=clear).grid(row=4,column=0)
btn0=Button(root,text="0",padx=50,pady=50,command=lambda : insert("0")).grid(row=4,column=1)
btne=Button(root,text="=",padx=50,pady=50,command=lambda: result()).grid(row=4,column=2)
btnd=Button(root,text="/",padx=50,pady=50,command=lambda : insert("/")).grid(row=4,column=3)
root.mainloop()