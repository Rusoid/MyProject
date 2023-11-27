from tkinter import *
root = Tk()
btn = Button(root, text= 'Кнопочка', width=10, height=2,
             bg='white', fg='black', font='Liberation 14')
lab = Label(root, text='Ваша фамилия:', font='Arial 14')
Edit = Entry (root, width=20)
btn.pack()
lab.pack()
Edit.pack()
root.mainloop()
