import tkinter as tk
root=tk.Tk()

root.title("from inputs")

root.geometry("400x400")

heading=tk.Label(root,text="FEEDBACK FORM")

heading.grid(row=0,column=1,pady=80)


field1=tk.Label(root,text="Name")
field1.grid(row=1,column=0,pady=10)
input1=tk.Entry(root)
input1.grid(row=1,column=1,pady=10)

field2=tk.Label(root,text="AGE")
field2.grid(row=2,column=0,pady=10)
input2=tk.Entry(root)
input2.grid(row=2,column=1,pady=10)



field3=tk.Label(root,text="GENDER")
field3.grid(row=3,column=0,pady=10)
input3=tk.Entry(root)
input3.grid(row=3,column=1,pady=10)



field4=tk.Label(root,text="DATE OF BIRTH")
field4.grid(row=4,column=0,pady=10)
input4=tk.Entry(root)
input4.grid(row=4,column=1,pady=10)



field5=tk.Label(root,text="VILLAGE NAME")
field5.grid(row=5,column=0,pady=10)
input5=tk.Entry(root)
input5.grid(row=5,column=1,pady=10)


field6=tk.Label(root,text="COLLAGE")
field6.grid(row=6,column=0,pady=10)
input6=tk.Entry(root)
input6.grid(row=6,column=1,pady=10)


field7=tk.Label(root,text="BRANCH")
field7.grid(row=7,column=0,pady=10)
input7=tk.Entry(root)
input7.grid(row=7,column=1,pady=10)



field8=tk.Label(root,text="S.NO")
field8.grid(row=8,column=0,pady=10)
input8=tk.Entry(root)
input8.grid(row=8,column=1,pady=10)


field9=tk.Label(root,text="PHONE NUMBER")
field9.grid(row=9,column=0,pady=10)
input9=tk.Entry(root)
input9.grid(row=9,column=1,pady=10)


field10=tk.Label(root,text="FEEDBACK COMMENT")
field10.grid(row=10,column=0,pady=10)
input10=tk.Entry(root)
input10.grid(row=10,column=1,pady=10)


submit_btn=tk.Button(root,text="SUBMIT",bg="blue",fg="red")
submit_btn.grid(row=11, column=0, columnspan=30, pady=50)


tk.mainloop()