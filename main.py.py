from tkinter import *  
from tkinter import filedialog

from tkinter.filedialog import askopenfile
from data_condition import filter_data
from tqdm.tk import tqdm

base = Tk()  
base.geometry("450x450")  
base.title("Data Filteration")  

lbl_0 = Label(base, text="Data Filteration", width=15,font=("bold",15),fg='brown')   
lbl_0.place(x=130,y=10) 
file_name = ''
def upload_file():
    global file_name
    file = filedialog.askopenfilename()
    file_name = file
    lbl_file_name = Label(base, text=file_name, width=50, font=("arial",8),fg='blue')  
    lbl_file_name.place(x=60,y=75)


input_file_lbl = Label(base, text="", width=10, font=("arial",10))  
input_file_lbl.place(x=0, y=70)  
b1 = Button(base, text='Upload File', width=15,command = lambda:upload_file(), fg='white',bg ='green')
b1.place(x=160,y=50) 


lb1= Label(base, text="R1V1", width=10, font=("arial",10))  
lb1.place(x=20, y=100)  
en1= Entry(base,width=10)  
en1.place(x=30, y=125)  

lb2= Label(base, text="R1V2", width=10, font=("arial",10))  
lb2.place(x=130, y=100)  
en2= Entry(base,width=10)  
en2.place(x=140, y=125)  
  
lb3= Label(base, text="R1V3", width=10, font=("arial",10))  
lb3.place(x=240, y=100)  
en3= Entry(base,width=10)  
en3.place(x=250, y=125)  
  
lb4= Label(base, text="R1V4", width=10,font=("arial",10))  
lb4.place(x=350, y=100)  
en4= Entry(base,width=10)  
en4.place(x=360, y=125)  

lb5= Label(base, text="R2V1", width=10,font=("arial",10))  
lb5.place(x=20, y=150)  
en5= Entry(base,width=10)  
en5.place(x=30, y=175)  

  
lb6= Label(base, text="R2V2", width=10,font=("arial",10))  
lb6.place(x=130, y=150)  
en6= Entry(base, width=10)  
en6.place(x=140, y=175)  
  
lb7= Label(base, text="R2V3", width=10,font=("arial",10))  
lb7.place(x=240, y=150)  
en7 =Entry(base, width=10)  
en7.place(x=250, y=175)  

lb8= Label(base, text="R2V4", width=10,font=("arial",10))  
lb8.place(x=350, y=150)  
en8 =Entry(base, width=10)  
en8.place(x=360, y=175) 

lb9= Label(base, text="R3V1", width=10,font=("arial",10))  
lb9.place(x=20, y=200)  
en9 =Entry(base, width=10)  
en9.place(x=30, y=225) 
  
lb10= Label(base, text="R3V2", width=10,font=("arial",10))  
lb10.place(x=130, y=200)  
en10 =Entry(base, width=10)  
en10.place(x=140, y=225)

lb11= Label(base, text="R3V3", width=10,font=("arial",10))  
lb11.place(x=240, y=200)  
en11 =Entry(base, width=10)  
en11.place(x=250, y=225) 

lb12= Label(base, text="R3V4", width=10,font=("arial",10))  
lb12.place(x=350, y=200)  
en12 =Entry(base, width=10)  
en12.place(x=360, y=225) 

lb13= Label(base, text="R4V1", width=10,font=("arial",10))  
lb13.place(x=20, y=250)  
en13 =Entry(base, width=10)  
en13.place(x=30, y=275) 

lb14= Label(base, text="R4V2", width=10,font=("arial",10))  
lb14.place(x=130, y=250)  
en14 =Entry(base, width=10)  
en14.place(x=140, y=275) 

lb15= Label(base, text="R4V3", width=10,font=("arial",10))  
lb15.place(x=240, y=250)  
en15 =Entry(base, width=10)  
en15.place(x=250, y=275) 

lb16= Label(base, text="R4V4", width=10,font=("arial",10))  
lb16.place(x=350, y=250)  
en16 =Entry(base, width=10)  
en16.place(x=360, y=275) 

def close():
       #win.destroy()
   base.quit()

def myclick():
    print(file_name)
    row1_list = [en1.get(), en2.get(), en3.get(), en4.get()]
    row2_list = [en5.get(), en6.get(), en7.get(), en8.get()]
    row3_list = [en9.get(), en10.get(), en11.get(), en12.get()]
    row4_list = [en13.get(), en14.get(), en15.get(), en16.get()]    
    try:
        result, opt_path  = filter_data(file_name, row1_list, row2_list, row3_list, row4_list,base)
        if not result.empty:
            opt_lbl = Label(base, text=f"Output saved: {opt_path}", width=50,font=("arial",10))
            opt_lbl.place(x=40, y=420)
        else:
            opt_lbl = Label(base, text=f"No match found", width=50,font=("arial",10))
            opt_lbl.place(x=40, y=420)

    except FileNotFoundError:
        error_lbl = Label(base, text="Error: Please select input file", width=40,font=("arial",10))
        error_lbl.place(x=50, y=310) 
        print('please select input file')
    except ValueError as e:
        # raise e
        error_lbl = Label(base, text="Error: Values missing in input field", width=40,font=("arial",10))
        error_lbl.place(x=50, y=310) 

Button(base, text="Close", command= close, width=10,bg="brown",fg='white').place(x=220,y=350) 
Button(base, text="Run", command=myclick, width=10,bg="brown",fg='white').place(x=130,y=350)  
base.mainloop()  