#!/usr/bin/env python
# coding: utf-8

# In[13]:


from tkinter import *
import tkinter.messagebox
 
def main():
 top1=Tk()
 top1.geometry('400x300')
 name=str(E1.get())
 L00 = Label(top1, text=name +" Your Medical Report is:",
 fg="brown",
 font="Times").grid(row=0,column=0)
 
 """____________________________BMI____________________"""
 l12=Label(top1,text="BMI:",fg="red")
 l12.grid(row=4,column=0)
 E12=Entry(top1,bd=5)
 E12.grid(row=4,column=1)
 weight1=int(E3.get())
 height1=float(E4.get())
 age1=int(E2.get())
 bmi1=weight1/(height1*height1)
 E12.insert(0,bmi1)
 E12['bg']='grey'
 ls=Label(top1,text="CURRENT",fg="blue")
 ls.grid(row=1,column=0)
 Ess=Entry(top1,bd=5)
 Ess.grid(row=1,column=1)
 if (bmi1<25):
     Ess.insert(0,"Healthy")
     Ess['bg']='grey'
 elif (bmi1>=25 and bmi1<=30):
     Ess.insert(0,"overweight")
     Ess['bg']='grey'
 else:
     Ess.insert(0,"Obese")
     Ess['bg']='grey'
    
 lbb=Label(top1,text="FOCUS",fg="red")
 lbb.grid(row=2,column=0)
 Ebb=Entry(top1,bd=5)
 Ebb.grid(row=2,column=1)
 if (Ess.get()=="Healty"):
     Ebb.insert(0,"general fitness")
     Ebb['bg']='grey'
 elif (Ess.get()=="overweight"):
     Ebb.insert(0,"calorie deficit-N(cardio)/weight training")
     Ebb['bg']='grey'
 else:
     Ebb.insert(0,"calorie deficit-I(cardio)/weight training")
     Ebb['bg']='grey'
    
 Lrr=Label(top1,text="protien",fg="red")
 Lrr.grid(row=3,column=0)
 Lbb=Entry(top1,bd=5)
 Lbb.grid(row=3,column=1)
 call0=int(E3.get())
 call1=call0*2+30
 Lbb.insert(0,call1)
 Lbb['bg']='grey'
 
 """____________________BP____________________"""
 
 L11=Label(top1,text="BP(HIGH/MEDIUM/LOW):",fg="blue")
 L11.grid(row=5,column=0)
 E11=Entry(top1,bd=5)
 E11.grid(row=5,column=1)
 bplow1=int(E5.get())
 if (bplow1<=90):
     E11.insert(0,"Low")
     E11['bg']='grey'
 elif (bplow1>90 and bplow1<120):
     E11.insert(0,"Medium")
     E11['bg']='grey'
 else:
     E11.insert(0,"High")
     E11['bg']='grey'
 
 """"________________Pulserate____________________________________"""
 
 L22=Label(top1,text="Pulse Rate(HIGH/MEDIUM/LOW):",fg="red")
 L22.grid(row=6,column=0)
 E22=Entry(top1,bd=5)
 E22.grid(row=6,column=1) 
 pulserate1=int(E6.get())
 if(pulserate1<60):
     E22.insert(0,"low")
     E22['bg']='grey'
 elif (pulserate1>60 and pulserate1<100):
     E22.insert(0,"Medium")
     E22['bg']='grey'
 else:
     E22.insert(0,"High")
     E22['bg']='grey'
 
 """________________RBC count_______________"""
 
 L33=Label(top1,text="RBC Count(HIGH/MEDIUM/LOW):",fg="blue")
 L33.grid(row=7,column=0)
 E33=Entry(top1,bd=5)
 E33.grid(row=7,column=1)
 rbccount1=int(E7.get())
 if(rbccount1<475000):
     E33.insert(0,"Low")
     E33['bg']='grey'
 elif(rbccount1>475000 and rbccount1<610000):
     E33.insert(0,"Medium")
     E33['bg']='grey'
 else:
     E33.insert(0,"High")
     E33['bg']='grey'
 """_____________WBC COUT_______________________"""
 L44=Label(top1,text="WBC Count(HIGH/MEDIUM/LOW):",fg="red")
 L44.grid(row=8,column=0)
 E44=Entry(top1,bd=5)
 E44.grid(row=8,column=1)
 wbccount1=int(E8.get())
 if(wbccount1<4000):
     E44.insert(0,"Low")
     E44['bg']='grey'
 elif(wbccount1>4000 and wbccount1<10000):
     E44.insert(0,"Medium")
     E44['bg']='grey'
 else:
     E44.insert(0,"High")
     E44['bg']='grey'
 """_____________________PLALATES_____________________"""
 L55=Label(top1,text="Platelets(HIGH/MEDIUM/LOW):",fg="blue")
 L55.grid(row=9,column=0)
 E55=Entry(top1,bd=5)
 E55.grid(row=9,column=1)
 platelets1=int(E9.get())
 if(platelets1<150000):
    E55.insert(0,"Low")
    E55['bg']='grey'
 elif (platelets1>150000 and platelets1<450000):
     E55.insert(0,"Medium")
     E55['bg']='grey'
 else:
     E55.insert(0,"High")
     E55['bg']='grey' 
 """___________________________HEMOGLOBIN_____________"""
 L66=Label(top1,text="HB(HIGH/MEDIUM/LOW):",fg="red")
 L66.grid(row=10,column=0)
 E66=Entry(top1,bd=5)
 E66.grid(row=10,column=1)
 hb1=int(E10.get())
 if(hb1<12):
     E66.insert(0,"Low")
     E66['bg']='grey'
 elif(hb1>12 and hb1<16):
     E66.insert(0,"Medium")
     E66['bg']='grey'
 else:
     E66.insert(0,"High")
     E66['bg']='grey'
 """________________URIC ACID_________________"""
 L77=Label(top1,text="Uric Acid(HIGH/MEDIUM/LOW):",fg="blue")
 L77.grid(row=11,column=0)
 E77=Entry(top1,bd=5)
 E77.grid(row=11,column=1)
 uricacid1=int(E50.get())
 
 if(uricacid1<4):
     E77.insert(0,"grey")
     E77['bg']='red'
 elif(uricacid1>4 and uricacid1<7):
     E77.insert(0,"Medium")
     E77['bg']='grey'
 else:
     E77.insert(0,"High")
     E77['bg']='grey'
 """___________________________CHOLESTROL_______________________"""
 L88=Label(top1,text="Cholestrol(HIGH/MEDIUM/LOW):",fg="red")
 L88.grid(row=12,column=0)
 E88=Entry(top1,bd=5)
 E88.grid(row=12,column=1)
 cholestrol1=int(E51.get())
 if(cholestrol1<40):
     E88['bg']='red'
     E88.insert(0,"grey")
 elif(cholestrol1>40 and cholestrol1<50):
     E88.insert(0,"Medium")
     E88['bg']='grey'
 else:
     E88.insert(0,"High")
     E88['bg']='grey'
 
 top1.mainloop()
top = Tk()
L0 = Label(top, text="Fitness Calculator",
 fg="black",
 font="Times").grid(row=0,column=1)
L1=Label(top,text="Name",
 fg="blue",
 font="Times").grid(row=1,column=0)
E1= Entry(top,bd=5)
E1.grid(row=1,column=1)
L2=Label(top,text="age ",
 fg="blue",
 font="Times").grid(row=2,column=0)
E2= Entry(top,bd=5)
E2.grid(row=2,column=1)
l3=Label(top,text="weight (in Kg)",fg="red",font="Times").grid(row=3,column=0)
E3= Entry(top,bd=5)
E3.grid(row=3,column=1)
l4=Label(top,text="Height (in M)",fg="red",font="Times").grid(row=4,column=0)
E4=Entry(top,bd=5)
E4.grid(row=4,column=1)
L77=Label(top,text="Goal",
 fg="red",
 font="Times").grid(row=5,column=0)
E77= Entry(top,bd=5)
E77.grid(row=5,column=1)
L78=Label(top,text="current cal intake",
 fg="red",
 font="Times").grid(row=6,column=0)
E78= Entry(top,bd=5)
E78.grid(row=6,column=1)
L79=Label(top,text="Protien Intake",
 fg="red",
 font="Times").grid(row=7,column=0)
E79= Entry(top,bd=5)
E79.grid(row=7,column=1)
l5=Label(top,text="Bp (0-120)",fg="red",font="Times").grid(row=8,column=0)
E5=Entry(top,bd=5)
E5.grid(row=8,column=1)
L6=Label(top,text="Pulserate (0-100)",
 fg="blue",
 font="Times").grid(row=9,column=0)
E6= Entry(top,bd=5)
E6.grid(row=9,column=1)
L7=Label(top,text="RBCcount ( 310000-610000)",
 fg="blue",
 font="Times").grid(row=10,column=0)
E7 = Entry(top,bd=5)
E7.grid(row=10,column=1)
L8=Label(top,text="WBCcount (2000-10000)",
 fg="blue",
 font="Times").grid(row=11,column=0)
E8= Entry(top,bd=5)
E8.grid(row=11,column=1)
L9=Label(top,text="Platelets (150000-615000)",
 fg="blue",
 font="Times").grid(row=12,column=0)
E9 = Entry(top,bd=5)
E9.grid(row=12,column=1)
L10=Label(top,text="HEMOGLOBIN(0-16)",
 fg="blue",
 font="Times").grid(row=13,column=0)
E10 = Entry(top,bd=5)
E10.grid(row=13,column=1)
L50=Label(top,text="URIC ACID (0-7)",
 fg="blue",
 font="Times").grid(row=14,column=0)
E50 = Entry(top,bd=5)
E50.grid(row=14,column=1)
L51=Label(top,text="CHOLESTROL(40-55)",
 fg="blue",
 font="Times").grid(row=15,column=0)
E51 = Entry(top,bd=5)
E51.grid(row=15,column=1)
def clear_textbox():
 E1.delete(0,END)
 E2.delete(0, END)
 E3.delete(0, END)
 E4.delete(0, END)
 E5.delete(0, END)
 E6.delete(0, END)
 E7.delete(0, END)
 E8.delete(0, END)
 E9.delete(0, END)
 E10.delete(0, END)
 E50.delete(0, END)
 E51.delete(0, END)
 E77.delete(0,END)
 E78.delete(0,END)
 E79.delete(0,END)

def close_window (): 
 top.destroy()
D=Label(top,text="Developed By:-",fg='green')
D.grid(row=19,column=0)
D1=Label(top,text="Prakhar Arora",fg='brown')
D1.grid(row=19,column=1)
D2=Label(top,text="K Deepak",fg='black')
D2.grid(row=19,column=2)
D2=Label(top,text="Kalyani Rajesh Parayil",fg='purple')
D2.grid(row=19,column=3)
B14=Button(top, text='RESET ALL ENTRIES',command=clear_textbox,bg="brown")
B14.grid(row=17,column=0)
B15=Button (top,text = "EXIT",command=close_window,bg="red")
B15.grid(row=14,column=2)
B1=Button(top, text='Generate Report',command=main,bg="orange")
B1.grid(row=13,column=2)
top.mainloop()


# In[ ]:




