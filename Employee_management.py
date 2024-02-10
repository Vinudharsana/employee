
import tkinter as tk
import mysql.connector
from tkinter import messagebox
from tkinter import ttk


window = tk.Tk()
window.configure(bg="black")
window.title("Employee database")
window.geometry("1200x700")

mydb = mysql.connector.connect(
    host="localhost", user="root",
    password="1234", database="employeereg")
cursor = mydb.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS employee(
                Name varchar(50) NOT NULL,
                ID varchar(20) NOT NULL PRIMARY KEY,
                Sex varchar(20) NOT NULL,
                date varchar(5) NOT NULL,
                Month varchar(5) NOT NULL,
                Year varchar(6) NOT NULL,
                Phone varchar(20) NOT NULL,
                Email varchar(100) NOT NULL UNIQUE,
                Address varchar(150) NOT NULL)''')

vars = 0 
sex = "none" 

def female_selected():
    global sex
    sex = "Female"
    return sex

def male_selected():
    global sex
    sex = "Male"
    return sex

def add_info():
    global sex
    name = Entry_Employee_Name.get()
    sex = sex
    id = Entry_Employee_ID.get()
    date = Entry_Date.get()
    month = Entry_Month.get()
    year = Entry_Year.get()
    phone = Entry_Phone_Number.get()
    email = Entry_Email.get()
    address = Entry_Address.get(1.0, "end-1c")
    proceedOrNot = messagebox.askyesno("Employee Adding", "Are You Sure add Student \nName = {}\nId = {}\nSex = {}\ndate = {}/{}/{}\nPhone = {}\nEmail = {}\nAddress = {}".format(name, id, sex, date, month, year, phone, email, address))
    if proceedOrNot == 1:        
       cursor = mydb.cursor()
       sql = "INSERT INTO employee(name, id, sex, date, month, year, phone, email, address) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
       cursor.execute(sql,(name, id, sex, date, month, year, phone, email, address))

       for i in cursor:
           tree.insert("", 0, text=i[0], values=(i[1], i[2], i[3], i[4]+" - "+i[5]+" - "+i[6], i[7], i[8], i[9], i[10], i[11]))      
       messagebox.showinfo("Employee Adding", "Successfully added Employee \nName = {}\nId = {}\nSex = {}\ndate = {}/{}/{}\nPhone = {}\nEmail = {}\nAddress = {}".format(name, id, sex, date, month, year, phone, email, address))      
       mydb.commit()
    else:
       messagebox.showinfo("Unsuccessfull", "Cancelled")

def show():
    cursor = mydb.cursor()
    sql = "SELECT * FROM employee"
    cursor.execute(sql)
    for i in cursor:
        tree.insert("", 0, text=i[0], values=(i[1], i[2], i[3]+"-"+i[4]+"-" +i[5], i[6],i[7],i[8]))
        
def delete_employee():
   id = Entry_Employee_ID.get()
   proceedOrNot = messagebox.askyesno("Employee Information", "Delete Employee ?\nId = {} ".format(id))
   if proceedOrNot == 1:
       cursor = mydb.cursor()
       sql = "DELETE FROM employee WHERE ID=%s"
       cursor.execute(sql,(id, ))
       mydb.commit()
       messagebox.showinfo("Deleting Employee", "Successfully deleted Employee \n Id = {}".format(id))
   else:
       messagebox.showinfo("Unsuccessfully", "Canceled")

def reset_info():
   Entry_Employee_ID.delete(0, 40)
   Entry_Employee_Name.delete(0,40)
   Entry_Employee_ID.delete(0, 40)
   Entry_Date.delete(0, 40)
   Entry_Month.delete(0, 40)
   Entry_Year.delete(0, 40)
   Entry_Phone_Number.delete(0, 40)
   Entry_Email.delete(0, 40)
   Entry_Address.delete(1.0, "end-1c")

def refresh_info():
   tree.delete(*tree.get_children())
   cursor = mydb.cursor()
   sql = "select * from employee"
   cursor.execute(sql)
   for i in cursor:
       tree.insert("", 0)



Label = tk.Label()
Label.place(relx=0.0, rely=0.0, height=60, width=1358)
Label.configure(background="#000d66", foreground="#FF0000",font="-family {Segoe UI} -size 30 -weight bold", text="Employee Management System",anchor="center")

# Creating a label Frame for Employee's Information
Left_Employee_Information = tk.LabelFrame()
Left_Employee_Information.place(relx=0.004, rely=0.099, relheight=0.900, relwidth=0.385)
Left_Employee_Information.configure(relief='groove', background="#FF1493")

Employee_ID = tk.Label(Left_Employee_Information)
Employee_ID.place(relx=0.077, rely=0.080, height=31, width=160, bordermode='ignore')
Employee_ID.configure(background="#8B1C62",font="-family {Segoe UI} -size 12", foreground="white", text="Employee ID", anchor="center" )

Employee_Name = tk.Label(Left_Employee_Information)
Employee_Name.place(relx=0.077, rely=0.190, height=31, width=160, bordermode='ignore')
Employee_Name.configure(background="#8B1C62",font="-family {Segoe UI} -size 12", foreground="white", text="Employee Name", anchor="center")

Sex = tk.Label(Left_Employee_Information)
Sex.place(relx=0.077, rely=0.315, height=31, width=160, bordermode='ignore')
Sex.configure(background="#8B1C62", font="-family {Segoe UI} -size 12", foreground="white", text="Gender", anchor="center")

Date_of_Birth = tk.Label(Left_Employee_Information)
Date_of_Birth.place(relx=0.077, rely=0.450, height=31, width=160, bordermode='ignore')
Date_of_Birth.configure(background="#8B1C62",  font="-family {Segoe UI} -size 12", foreground="white", text="Date of Birth", anchor="center" )

Phone_Number = tk.Label(Left_Employee_Information)
Phone_Number.place(relx=0.077, rely=0.590, height=31, width=160, bordermode='ignore')
Phone_Number.configure(background="#8B1C62",  font="-family {Segoe UI} -size 12", foreground="white", text="Phone Number", anchor="center" )

Email = tk.Label(Left_Employee_Information)
Email.place(relx=0.077, rely=0.710, height=31, width=160, bordermode='ignore')
Email.configure(background="#8B1C62",  font="-family {Segoe UI} -size 12", foreground="white", text="Email", anchor="center" )

Address = tk.Label(Left_Employee_Information)
Address.place(relx=0.077, rely=0.845, height=31, width=160, bordermode='ignore')
Address.configure(background="#8B1C62",  font="-family {Segoe UI} -size 12", foreground="white", text="Address", anchor="center" )

# Creating input fields

Entry_Employee_ID = tk.Entry(Left_Employee_Information)
Entry_Employee_ID.place(relx=0.442, rely=0.080, height=30, relwidth=0.488, bordermode='ignore')
Entry_Employee_ID.configure(font="-family {Segoe UI} -size 12", foreground="black")
Entry_Employee_ID.insert(0, "Enter Employee ID")
Entry_Employee_ID.bind("<FocusIn>", lambda args: Entry_Employee_ID.delete('0', 'end'))

Entry_Employee_Name = tk.Entry(Left_Employee_Information)
Entry_Employee_Name.place(relx=0.442, rely=0.190, height=29, relwidth=0.488, bordermode='ignore')
Entry_Employee_Name.configure(font="-family {Segoe UI} -size 12", foreground="black")
Entry_Employee_Name.insert(0, "Enter Employee Name")
Entry_Employee_Name.bind("<FocusIn>", lambda args: Entry_Employee_Name.delete('0', 'end'))

Radiobutton_Sex_Male = tk.Radiobutton(Left_Employee_Information)
Radiobutton_Sex_Male.place(relx=0.442, rely=0.315, relheight=0.059, relwidth=0.217, bordermode='ignore')
Radiobutton_Sex_Male.configure(text="Male", variable=vars, value=1, state="active", background="#FF1493", foreground="black", command=male_selected)
Radiobutton_Sex_Female = tk.Radiobutton(Left_Employee_Information) 
Radiobutton_Sex_Female.place(relx=0.673, rely=0.315, relheight=0.059, relwidth=0.252, bordermode='ignore')
Radiobutton_Sex_Female.configure(text="Female", variable=vars, value=2, state= "normal", background="#FF1493", foreground="black", command=female_selected)

Entry_Date = tk.Entry(Left_Employee_Information)
Entry_Date.place(relx=0.442, rely=0.450, relheight=0.059, relwidth=0.106, bordermode='ignore')
Entry_Date.configure(font="-family {Segoe UI} -size 12", foreground="black")
Entry_Date.insert(0, "DD")
Entry_Date.bind("<FocusIn>", lambda args: Entry_Date.delete('0', 'end'))
Entry_Month = tk.Entry(Left_Employee_Information)
Entry_Month.place(relx=0.577, rely=0.450, relheight=0.059, relwidth=0.125, bordermode='ignore')
Entry_Month.configure(font="-family {Segoe UI} -size 12", foreground="black")
Entry_Month.insert(0, "MM")
Entry_Month.bind("<FocusIn>", lambda args: Entry_Month.delete('0', 'end'))
Entry_Year = tk.Entry(Left_Employee_Information)
Entry_Year.place(relx=0.731, rely=0.450, relheight=0.059, relwidth=0.183, bordermode='ignore')
Entry_Year.configure(font="-family {Segoe UI} -size 12", foreground="black")
Entry_Year.insert(0, "YYYY")
Entry_Year.bind("<FocusIn>", lambda args: Entry_Year.delete('0', 'end'))

Entry_Phone_Number = tk.Entry(Left_Employee_Information)
Entry_Phone_Number.place(relx=0.442, rely=0.590, height=29, relwidth=0.488, bordermode='ignore')
Entry_Phone_Number.configure(font="-family {Segoe UI} -size 12", foreground="black")
Entry_Phone_Number.insert(0, "Enter Employee Phone Number")
Entry_Phone_Number.bind("<FocusIn>", lambda args: Entry_Phone_Number.delete('0', 'end'))

Entry_Email = tk.Entry(Left_Employee_Information)
Entry_Email.place(relx=0.442, rely=0.710, height=29, relwidth=0.488, bordermode='ignore')
Entry_Email.configure(font="-family {Segoe UI} -size 12", foreground="black")
Entry_Email.insert(0, "Enter Employee Email")
Entry_Email.bind("<FocusIn>", lambda args: Entry_Email.delete('0', 'end'))

Entry_Address = tk.Text(Left_Employee_Information)
Entry_Address.place(relx=0.442, rely=0.845, relheight=0.1, relwidth=0.488, bordermode='ignore')
Entry_Address.configure(font="-family {Segoe UI} -size 12", foreground="black")


# Creating frame for the right side of the window
Frame_right = tk.Frame()
Frame_right.place(relx=0.388, rely=0.099, relheight=0.900, relwidth=0.607)
Frame_right.configure(relief='groove', borderwidth="2", background="#FF1493")

# Creating a frame for the action buttons
Button_Frame = tk.Frame()
Button_Frame.place(relx=0.395, rely=0.100, relheight=0.375, relwidth=0.600)
Button_Frame.configure(relief='raised', background="#FF1493")

Button_ADD = tk.Button(Button_Frame)
Button_ADD.place(relx=0.100, rely=0.260, height=45, width=130)
Button_ADD.configure(background="#BDFCC9", borderwidth="3", font="-family {Segoe UI} -size 14", foreground="#000000", text="INSERT", command=add_info)

Button_SHOW = tk.Button(Button_Frame)
Button_SHOW.place(relx=0.410, rely=0.260, height=45, width=130)
Button_SHOW.configure(background="#BDFCC9", borderwidth="5",  font="-family {Segoe UI} -size 14", foreground="#000000", text="DISPLAY", command=show)

Button_REFRESH = tk.Button(Button_Frame)
Button_REFRESH.place(relx=0.700, rely=0.260, height=45, width=130)
Button_REFRESH.configure(background="#BDFCC9", borderwidth="5", font="-family {Segoe UI} -size 14", foreground="#000000", text="REFRESH", command=refresh_info)

Button_DELETE = tk.Button(Button_Frame)
Button_DELETE.place(relx=0.300, rely=0.600, height=40, width=130)
Button_DELETE.configure(background="#BDFCC9", borderwidth="5",  font="-family {Segoe UI} -size 14", foreground="#000000", text="DELETE", command=delete_employee)

Button_RESET = tk.Button(Button_Frame)
Button_RESET.place(relx=0.600, rely=0.600, height=40, width=130)
Button_RESET.configure(background="#BDFCC9", borderwidth="5",  font="-family {Segoe UI} -size 14", foreground="#000000", text="RESET", command=reset_info)


# Creating a listbox inside the frame
Listbox = tk.Listbox(Frame_right)
Listbox.place(relx=0.020, rely=0.550, relheight=0.350, relwidth=0.960)

label = tk.Label(Frame_right)
label.place(relx=0.020, rely=0.500, relheight=0.050, relwidth=0.960)
label.configure(background="#8B1C62",  font="-family {Segoe UI} -size 17", foreground="white", text="Employee Database Information", anchor="center")

tree = ttk.Treeview(Listbox, columns=(' Name', 'ID', 'Gender', 'Date of Birth', 'Phone Number', 'Email', 'Address'))
tree.place(relx=0.020, rely=0.100, relheight=0.350, relwidth=0.960)
tree.heading('#0', text='Name')
tree.heading('#1', text='ID')
tree.heading('#2', text='Gender')
tree.heading('#3', text='Date of Birth')
tree.heading('#4', text='Phone Number')
tree.heading('#5', text='Email')
tree.heading('#6', text='Address')
tree.column('#0', width=150, anchor='center')
tree.column('#1', width=50, anchor='center')
tree.column('#2', width=60, anchor='center')
tree.column('#3', width=100, anchor='center')
tree.column('#4', width=100, anchor='center')
tree.column('#5', width=120, anchor='center')
tree.column('#6', width=120, anchor='center')
tree.pack()






