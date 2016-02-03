import Tkinter
import tkMessageBox
top = Tkinter.Tk()
top.geometry('325x350')
global s
s = 1

def checkwinner():
	if (MyButton1["text"]=="X" and MyButton2["text"]=="X" and MyButton3["text"]=="X") or (MyButton1["text"]=="X" and MyButton4["text"]=="X" and MyButton7["text"]=="X") or (MyButton1["text"]=="X" and MyButton5["text"]=="X" and MyButton9["text"]=="X") or (MyButton2["text"]=="X" and MyButton5["text"]=="X" and MyButton8["text"]=="X") or (MyButton3["text"]=="X" and MyButton6["text"]=="X" and MyButton9["text"]=="X") or (MyButton3["text"]=="X" and MyButton5["text"]=="X" and MyButton7["text"]=="X") or (MyButton4["text"]=="X" and MyButton5["text"]=="X" and MyButton6["text"]=="X") or (MyButton7["text"]=="X" and MyButton8["text"]=="X" and MyButton9["text"]=="X"):
		tkMessageBox.showinfo("X wins!", "X Wins!")
		top.quit()
	
	elif (MyButton1["text"]=="O" and MyButton2["text"]=="O" and MyButton3["text"]=="O") or (MyButton1["text"]=="O" and MyButton4["text"]=="O" and MyButton7["text"]=="O") or (MyButton1["text"]=="O" and MyButton5["text"]=="O" and MyButton9["text"]=="O") or (MyButton2["text"]=="O" and MyButton5["text"]=="O" and MyButton8["text"]=="O") or (MyButton3["text"]=="O" and MyButton6["text"]=="O" and MyButton9["text"]=="O") or (MyButton3["text"]=="O" and MyButton5["text"]=="O" and MyButton7["text"]=="O") or (MyButton4["text"]=="O" and MyButton5["text"]=="O" and MyButton6["text"]=="O") or (MyButton7["text"]=="O" and MyButton8["text"]=="O" and MyButton9["text"]=="O"):
		tkMessageBox.showinfo("O wins!", "O Wins!")
		top.quit()
	elif s==10:
		tkMessageBox.showinfo("Drawn", "Match Drawn!")
		top.quit()
def pr1():
	if MyButton1["text"]==" ":
		global s
		if s == 1 or s == 3 or s==5 or s==7 or s==9:
			MyButton1.config(text='X')
			MyButton1.config(state='disabled')
			s = s + 1
			checkwinner()
		elif s == 2 or s == 4 or s==6 or s==8:
			MyButton1.config(text='O')
			MyButton1.config(state='disabled')
			s = s + 1
			checkwinner()
def pr2():
	if MyButton2["text"]==" ":
		global s
		if s == 1 or s == 3 or s==5 or s==7 or s==9:
			MyButton2.config(text='X')
			MyButton2.config(state='disabled')
			s = s + 1
			checkwinner()
		elif s == 2 or s == 4 or s==6 or s==8:
			MyButton2.config(text='O')
			MyButton2.config(state='disabled')
			s = s + 1
			checkwinner()
def pr3():
	if MyButton3["text"]==" ":
		global s
		if s == 1 or s == 3 or s==5 or s==7 or s==9:
			MyButton3.config(text='X')
			MyButton3.config(state='disabled')
			s = s + 1
			checkwinner()
		elif s == 2 or s == 4 or s==6 or s==8:
			MyButton3.config(text='O')
			MyButton3.config(state='disabled')
			s = s + 1
			checkwinner()

def pr4():
	if MyButton4["text"]==" ":
		global s
		if s == 1 or s == 3 or s==5 or s==7 or s==9:
			MyButton4.config(text='X')
			MyButton4.config(state='disabled')
			s = s + 1
			checkwinner()
		elif s == 2 or s == 4 or s==6 or s==8:
			MyButton4.config(text='O')
			MyButton4.config(state='disabled')
			s = s + 1
			checkwinner()

def pr5():
	if MyButton5["text"]==" ":
		global s
		if s == 1 or s == 3 or s==5 or s==7 or s==9:
			MyButton5.config(text='X')
			MyButton5.config(state='disabled')
			s = s + 1
			checkwinner()
		elif s == 2 or s == 4 or s==6 or s==8:
			MyButton5.config(text='O')
			MyButton5.config(state='disabled')
			s = s + 1
			checkwinner()

def pr6():
	if MyButton6["text"]==" ":
		global s
		if s == 1 or s == 3 or s==5 or s==7 or s==9:
			MyButton6.config(text='X')
			MyButton6.config(state='disabled')
			s = s + 1
			checkwinner()
		elif s == 2 or s == 4 or s==6 or s==8:
			MyButton6.config(text='O')
			MyButton6.config(state='disabled')
			s = s + 1
			checkwinner()

def pr7():
	if MyButton7["text"]==" ":
		global s
		if s == 1 or s == 3 or s==5 or s==7 or s==9:
			MyButton7.config(text='X')
			MyButton7.config(state='disabled')
			s = s + 1
			checkwinner()
		elif s == 2 or s == 4 or s==6 or s==8:
			MyButton7.config(text='O')
			MyButton7.config(state='disabled')
			s = s + 1
			checkwinner()

def pr8():
	if MyButton8["text"]==" ":
		global s
		if s == 1 or s == 3 or s==5 or s==7 or s==9:
			MyButton8.config(text='X')
			MyButton8.config(state='disabled')
			s = s + 1
			checkwinner()
		elif s == 2 or s == 4 or s==6 or s==8:
			MyButton8.config(text='O')
			MyButton8.config(state='disabled')
			s = s + 1
			checkwinner()

def pr9():
	if MyButton9["text"]==" ":
		global s
		if s == 1 or s == 3 or s==5 or s==7 or s==9:
			MyButton9.config(text='X')
			MyButton9.config(state='disabled')
			s = s + 1
			checkwinner()
		elif s == 2 or s == 4 or s==6 or s==8:
			MyButton9.config(text='O')
			MyButton9.config(state='disabled')
			s = s + 1
			checkwinner()

MyButton1 = Tkinter.Button(top, text=" ", width=10, height=6, command=pr1)
MyButton1.grid(row=0, column=0)
MyButton2 = Tkinter.Button(top, text=" ", width=10, height=6, command=pr2)
MyButton2.grid(row=0, column=1)
MyButton3 = Tkinter.Button(top, text=" ", width=10, height=6, command=pr3)
MyButton3.grid(row=0, column=2)
MyButton4 = Tkinter.Button(top, text=" ", width=10, height=6, command=pr4)
MyButton4.grid(row=1, column=0)
MyButton5 = Tkinter.Button(top, text=" ", width=10, height=6, command=pr5)
MyButton5.grid(row=1, column=1)
MyButton6 = Tkinter.Button(top, text=" ", width=10, height=6, command=pr6)
MyButton6.grid(row=1, column=2)
MyButton7 = Tkinter.Button(top, text=" ", width=10, height=6, command=pr7)
MyButton7.grid(row=2, column=0)
MyButton8 = Tkinter.Button(top, text=" ", width=10, height=6, command=pr8)
MyButton8.grid(row=2, column=1)
MyButton9 = Tkinter.Button(top, text=" ", width=10, height=6, command=pr9)
MyButton9.grid(row=2, column=2)
w = Tkinter.Label(top, text="Tic-Tac-Toe", font=("Helvetica", 13), fg="red")
w.grid(row = 3, column=1)

top.mainloop()
