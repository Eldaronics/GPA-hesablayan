from tkinter import *
import tkinter.messagebox  as tkmb
qiymet = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #26
qVeGPA = ["Orta:",0,"GPA:",0]; #2
sum = 0
dersSay = (int(input("Neche dersiniz var(idi)?: "))) 
if dersSay > 26:
 print("Bir semestra",dersSay," ders ola bilmez!Yalandan yazmayin")
 quit()
elif dersSay <=0:
    print("1-26 arasi qiymet daxil edin")
    quit()
for a in range(0,dersSay):
    qiymet[a] = int(input("dersden aldiginiz qiymeti daxil edin: "))
    if (qiymet[a] < 0 or qiymet[a] >= 101):
       tkmb.showinfo("Xeta","0 ile 100 arasi qiymet daxil edin")
       quit()
for  b in range (0,dersSay):
    sum += qiymet[b]
netice = int(sum/dersSay)
qVeGPA[1] = netice
neticeGPA = float(netice*0.04)
qVeGPA[3] = neticeGPA
#print(netice)
if(netice>=70 and netice<=76):
    tkmb.showinfo(qVeGPA,"Yaxshidir!Ugurlar!Bele davam edin")
elif(netice>=77 and netice<=85):
    tkmb.showinfo(qVeGPA,"Supersiniz!Ela neticedir,sukani bele saxlayin")
elif(netice>=86 and netice<=101):
     tkmb.showinfo(qVeGPA,"Xalxin ushagi sizsiniz,tebrikler!")
else:
    tkmb.showerror(qVeGPA,"Chox pis!Niye oxumursuz?!Kime/Neye guvenirsiz?")
    

