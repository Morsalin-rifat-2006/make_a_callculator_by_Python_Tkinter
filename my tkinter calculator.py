from tkinter import *
from tkinter import messagebox
#------------all function ----------
def btn_click(number):
    try:
        global  operator
        operator=operator +str(number)
        Text_Input.set(operator)
    except:
        pass
def clear():
    try:
        global operator
        operator =""
        Text_Input.set("")
    except:
        pass
def equ():
    try:
        global operator
        sum=str(eval(operator))
        Text_Input.set(sum)
        operator=""
    except:
        pass
#-------messagebox---------------
def info():
    messagebox.showinfo("About","This is my frist calculator by- Rifat.")
def quit_messagebox():
    ask=messagebox.askyesno("Exit","Do You Want to Exit This Calculator.")
    if  ask==1:
        quit_it=window.quit()
    else:
        pass            
window=Tk()
operator=""
Text_Input=StringVar()
#--------------text window------------
display=Entry(window,width=20,font=('arial',15,'bold'),bd=10,insertwidth=20,highlightbackground="gray",
textvariable=Text_Input,bg="powder blue",justify='right').grid(columnspan=10,ipady=39)
#-------------all button--------
#----------frist row---------
btn_clr=Button(window,highlightbackground="white",width=13,height=2,bg="gray",fg="#484848",bd='5',font=('arial',10,'bold'),text="C",command=clear).grid(column=0,row=1,columnspan=3)
#-------second row-------
btn7=Button(window,highlightbackground="white",width=2,height=2,fg="#484848",bg='gray',bd='5',font=('arial',10,'bold'),text="7",command=lambda:btn_click(7)).grid(column=0,row=2,columnspan=1)
btn8=Button(window,highlightbackground="white",width=2,height=2,bg="gray",fg="#484848",bd='5',font=('arial',10,'bold'),text="8",command=lambda:btn_click(8)).grid(column=1,row=2)
btn9=Button(window,highlightbackground="white", width=2,height=2,bg="gray",fg="#484848",bd='5',font=('arial',10,'bold'),text="9",command=lambda:btn_click(9)).grid(column=2,row=2)
btn_add=Button(window,highlightbackground="white",width=2,height=2,bg="gray",fg="#484848",bd='5',font=('arial',10,'bold'),text="+",command=lambda:btn_click("+")).grid(column=3,row=2)
btn_mul=Button(window,highlightbackground="white",width=2,height=2,bg="gray",fg="#484848",bd='5',font=('arial',10,'bold'),text="x",command=lambda:btn_click("*")).grid(column=4,row=2)
#-----------row 3-------------
btn4=Button(window,highlightbackground="white",width=2,height=2,bg="gray",fg="#484848", bd='5',font=('arial',10,'bold'),text="4",command=lambda:btn_click(4)).grid(column=0,row=3)
btn5=Button(window,highlightbackground="white",width=2,height=2,bg="gray",fg="#484848",bd='5',font=('arial',10,'bold'),text="5",command=lambda:btn_click(5)).grid(column=1,row=3)
btn6 =Button(window,highlightbackground="white",width=2,height=2,bg="gray",fg="#484848",bd='5',font=('arial',10,'bold'),text="6",command=lambda:btn_click(6)).grid(column=2,row=3)
btn_sub=Button(window,highlightbackground="white",width=2,height=2,bg="gray",fg="#484848",bd='5',font=('arial',10,'bold'),text="-",command=lambda:btn_click("-")).grid(column=3,row=3)
btn_div=Button(window,highlightbackground="white",width=2,height=2,bg="gray",fg="#484848",bd='5',font=('arial',10,'bold'),text="/",command=lambda:btn_click("/")).grid(column=4,row=3)
#----------------row 4-------------------#
btn3=Button(window,highlightbackground="white",width=2,height=2,bg="gray",fg="#484848",bd='5',font=('arial',10,'bold'),text="3",command=lambda:btn_click(3)).grid(column=0,row=4)
btn2=Button(window,highlightbackground="white",width=2,height=2,bg="gray",fg="#484848",bd='5',font=('arial',10,'bold'),text="2",command=lambda:btn_click(2)).grid(column=1,row=4)
btn1=Button(window,highlightbackground="white",width=2,height=2,bg="gray",fg="#484848",bd='5',font=('arial',10,'bold'),text="1",command=lambda:btn_click(1)).grid(column=2,row=4)
btn_pwr=Button(window,highlightbackground="white",width=8,height=2,bg="gray",fg="#484848",bd='5',font=('arial',10,'bold'),text="Power",command=lambda:btn_click("**")).grid(column=3,row=4,columnspan=2)
#-----------row 5-------------#
btn0=Button(window,highlightbackground="white",width=2,height=2,bg="gray",fg="#484848",bd='5',font=('arial',10,'bold'),text="0",command=lambda:btn_click(0)).grid(column=0,row=5)
btn_equ =Button(window,highlightbackground="white",width=8,height=2,bg="gray",fg="#484848",bd='5',font=('arial',10,'bold'),text="=",command=equ).grid(column=3,row=5,rowspan=1,columnspan=2)
btn_point=Button(window,highlightbackground="white",width=8,height=2,bg="gray",fg="#484848",bd='5',font=('arial',10,'bold'),text=".",command=lambda:btn_click(".")).grid(column=1,row=5,columnspan=2)
#.........message box button.......
mess_box=Button(window,width=8,height=2,bd="5",bg="gray",fg="green",font=('arial',10,'bold'),text="Read Me",command=info).grid(row=8,column=0,columnspan=2)
exit_btn=Button(window,width=8,height=2,bd="5",bg="gray",fg="red",font=('arial',10,'bold'),text="Exit",command=quit_messagebox).grid(row=9,column=0,columnspan=2,pady=20)
window.mainloop()