from tkinter import *
import math
import parser
import tkinter.messagebox

root = Tk()
root.title("Scientific Calculator")
root.configure(background="black")
root.resizable(width=False, height=False)
root.geometry("480x568+0+0")

calculator = Frame(root)
calculator.grid()

class calc():
	def __init__(self):
		self.total =0
		self.current = ""
		self.input_value = True
		self.check_sum =False
		self.op =""
		self.result = False
		
	def numberEnter(self, num):
		self.result =False
		firstnum = txtDisplay.get()
		secondnum = str(num)
		if self.input_value:
			self.current = secondnum
			self.input_value = False
		else:
			if secondnum == '.':
				if secondnum in firstnum:
					return
			self.current = firstnum + secondnum
		self.display(self.current)
		
	def sum_of_total(self):
		self.result = True
		self.current = float(self.current)
		if self.check_sum == False:
			self.valid_function()
		else:
			self.total = float(txtDisplay.get())
			
	def display(self, value):
		txtDisplay.delete(0, END)
		txtDisplay.insert(0, value)
		
	def valid_function(self):
		if self.op == "add": 
			self.total += self.current
		if self.op == "sub":
			self.total -= self.current
		if self.op == "multi":
			self.total *= self.current
		if self.op == "divide":
			self.total /= self.current
		if self.op == "mod":
			self.total %= self.current
		self.input_value = True
		self.check_sum = False
		self.display(self.total)
		
	def operation(self, op):
		self.current = float(self.current)
		if self.check_sum:
			self.valid_function()
		elif not self.result:
			self.total = self.current
			self.input_value = True
		self.total = True
		self.op = op
		self.result = False
			
	def Clear_Entry(self):
		self.result = False
		self.current = "0"
		self.display(0)
		self.input_value = True
		
	def all_Clear_Entry(self):
		self.Clear_Entry()
		self.total = 0
		
	def mathsPM(self):
		self.result = False
		self.current = -(float(txtDisplay.get()))
		self.display(self.current)
		
	def squared(self):
		self.result = False 
		self.current = math.sqrt(float(txtDisplay.get()))
		self.display(self.current)
		
	def cos(self):
		self.result = False
		self.current = math.cos(math.radians(float(txtDisplay.get())))
		self.display(self.current)
	
	def pi(self):
		self.result = False
		self.current = math.pi
		self.display(self.current)
		
	def tau(self):
		self.result = False
		self.current = math.tau
		self.display(self.current)
		
	def e(self):
		self.result = False
		self.current = math.e
		self.display(self.current)
	
	def tan(self):
		self.result = False
		self.current = math.tan(math.radians(float(txtDisplay.get())))
		self.display(self.current)
		
	def sin(self):
		self.result = False
		self.current = math.sin(math.radians(float(txtDisplay.get())))
		self.display(self.current)
		
	def cosh(self):
		self.result = False
		self.current = math.cosh(math.radians(float(txtDisplay.get())))
		self.display(self.current)
		
	def tanh(self):
		self.result = False
		self.current = math.tanh(math.radians(float(txtDisplay.get())))
		self.display(self.current)
		
		
	def e(self):
		self.result = False
		self.current = math.e
		self.display(self.current)
		
	def sinh(self):
		self.result = False 
		self.current = math.sinh(math.radians(float(txtDisplay.get())))
		self.display(self.current)
		
	def acosh(self):
		self.result = False 
		self.current = math.acosh(float(txtDisplay.get()))
		self.display(self.current)
		
	def log(self):
		self.result = False
		self.current = math.log(float(txtDisplay.get()))
		self.display(self.current)

	def exp(self):
		self.result = False 
		self.current = math.exp(float(txtDisplay.get()))
		self.display(self.current)
				
	def asinh(self):
		self.result = False 
		self.current = math.asinh(float(txtDisplay.get()))
		self.display(self.current)
			
	def expml(self):
		self.result = False 
		self.current = math.expml(float(txtDisplay.get()))
		self.display(self.current)
		
	def lgamma(self):
		self.result = False 
		self.current = math.lgamma(float(txtDisplay.get()))
		self.display(self.current)
		
	def degrees(self):
		self.result = False 
		self.current = math.degrees(float(txtDisplay.get()))
		self.display(self.current)
		
	def log2(self):
		self.result = False 
		self.current = math.log2(float(txtDisplay.get()))
		self.display(self.current)
		
	def log10(self):
		self.result = False 
		self.current = math.log10(float(txtDisplay.get()))
		self.display(self.current)
		
	def log1p(self):
		self.result = False 
		self.current = math.log1p(float(txtDisplay.get()))
		self.display(self.current)
		
added_value = calc()
	
txtDisplay = Entry(calculator, font=('arial', 20, 'bold'), bd=30, width=28, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")

numberpad = "789456123"
i = 0
btn = []
for j in range(2,5):
	for k in range(3):
		btn.append(Button(calculator, width=6, height=2, font=('arial', 20, 'bold'), bd = 4, text = numberpad[i]))
		btn[i].grid(row = j, column =k, pady=1)
		btn[i] ["command"] = lambda x = numberpad [i]: added_value.numberEnter(x)
		i +=1
#==================================#======================#====================
btnClear = Button(calculator, text=chr(67), width=6, height=2, font=('arial', 20, 'bold'), bd = 4, 
			bg="powder blue",command = added_value.Clear_Entry).grid(row=1, column=0, pady= 1)
btnAllClear = Button(calculator, text=chr(67) + chr(69), width=6, height=2, font=('arial', 20, 'bold'), bd = 4, 
			bg="powder blue", command = added_value.all_Clear_Entry).grid(row=1, column=1, pady= 1)
			
btnSq = Button(calculator, text="√", width=6, height=2, font=('arial', 20, 'bold'), bd = 4,
			bg="powder blue", command =added_value.squared).grid(row=1, column=2, pady= 1)
btnAdd = Button(calculator, text="+", width=6, height=2, font=('arial', 20, 'bold'), bd = 4, bg="powder blue",
			command = lambda: added_value.operation("add")).grid(row=1, column=3, pady= 1)			
btnSub = Button(calculator, text="-", width=6, height=2, font=('arial', 20, 'bold'), bd = 4,bg="powder blue", 
			command = lambda: added_value.operation("sub")).grid(row=2, column=3, pady= 1)
btnMulti = Button(calculator, text="*", width=6, height=2, font=('arial', 20, 'bold'), bd = 4, bg="powder blue",
			command = lambda: added_value.operation("multi")).grid(row=3, column=3, pady= 1)			
btnDiv = Button(calculator, text=chr(247), width=6, height=2, font=('arial', 20, 'bold'), bd = 4, bg="powder blue",
			command = lambda: added_value.operation("divide ")).grid(row=4, column=3, pady= 1)
btnZero = Button(calculator, text="0", width=6, height=2, font=('arial', 20, 'bold'), bd = 4, 
			bg="powder blue",command = lambda: added_value.numberEnter(0)).grid(row=5, column=0, pady= 1)
			
btnDot = Button(calculator, text=".", width=6, height=2, font=('arial', 20, 'bold'), bd = 4,
			bg="powder blue",command = lambda: added_value.operation(".")).grid(row=5, column=1, pady= 1)
btnPM = Button(calculator, text=chr(177), width=6, height=2, font=('arial', 20, 'bold'), bd = 4, 
			bg="powder blue",command =added_value.mathsPM).grid(row=5, column=2, pady= 1)			
btnEquals = Button(calculator, text="=", width=6, height=2, font=('arial', 20, 'bold'), bd = 4, 
			bg="powder blue", command = added_value.sum_of_total).grid(row=5, column=3, pady= 1)
#=================================Scientific Calculator========================
btnPi = Button(calculator, text="π", width=6, height=2, font=('arial', 20, 'bold'), bd = 4, 
			bg="dark blue", command =added_value.pi).grid(row=1, column=4, pady= 1)			
btnCos = Button(calculator, text="Cos", width=6, height=2, font=('arial', 20, 'bold'), bd = 4, 
			bg="dark blue", command =added_value.cos).grid(row=1, column=5, pady= 1)
btnTan = Button(calculator, text="Tan", width=6, height=2, font=('arial', 20, 'bold'), bd = 4, 
			bg="dark blue", command =added_value.tan).grid(row=1, column=6, pady= 1)			
btnSin = Button(calculator, text="Sin", width=6, height=2, font=('arial', 20, 'bold'), bd = 4,
			bg="dark blue", command =added_value.sin).grid(row=1, column=7, pady= 1)
#==============================================================================
btn2Pi = Button(calculator, text="2π", width=6, height=2, font=('arial', 20, 'bold'), bd = 4, 
			bg="dark blue",command =added_value.tau).grid(row=2, column=4, pady= 1)			
btnCosh = Button(calculator, text="Cos", width=6, height=2, font=('arial', 20, 'bold'), bd = 4, 
			bg="dark blue", command =added_value.cosh).grid(row=2, column=5, pady= 1)
btnTanh = Button(calculator, text="Tan", width=6, height=2, font=('arial', 20, 'bold'), bd = 4, 
			bg="dark blue", command =added_value.tanh).grid(row=2, column=6, pady= 1)			
btnSinh = Button(calculator, text="Sin", width=6, height=2, font=('arial', 20, 'bold'), bd = 4,
			bg="dark blue", command =added_value.sinh).grid(row=2, column=7, pady= 1)
#===============================================================================
btnLog = Button(calculator, text="Log", width=6, height=2, font=('arial', 20, 'bold'), bd = 4, 
			bg="dark blue", command =added_value.log).grid(row=3, column=4, pady= 1)			
btnExp = Button(calculator, text="Exp", width=6, height=2, font=('arial', 20, 'bold'), bd = 4, 
			bg="dark blue", command =added_value.exp).grid(row=3, column=5, pady= 1)
btnMod = Button(calculator, text="Mod", width=6, height=2, font=('arial', 20, 'bold'), bd = 4, 
			bg="dark blue", command = lambda: added_value.operation("mod")).grid(row=3, column=6, pady= 1)			
btnE = Button(calculator, text="e", width=6, height=2, font=('arial', 20, 'bold'), bd = 4,
			bg="dark blue",command =added_value.e).grid(row=3, column=7, pady= 1)
#==============================================================================
btnLog2 = Button(calculator, text="Log2", width=6, height=2, font=('arial', 20, 'bold'), bd = 4, 
			bg="dark blue", command =added_value.log2).grid(row=4, column=4, pady= 1)			
btnaDeg = Button(calculator, text="aCosh", width=6, height=2, font=('arial', 20, 'bold'), bd = 4, 
			bg="dark blue", command =added_value.degrees).grid(row=4, column=5, pady= 1)
btnacosh = Button(calculator, text="acosh", width=6, height=2, font=('arial', 20, 'bold'), bd = 4, 
			bg="dark blue", command =added_value.acosh).grid(row=4, column=6, pady= 1)			
btnasinh = Button(calculator, text="asinh", width=6, height=2, font=('arial', 20, 'bold'), bd = 4,
			bg="dark blue", command =added_value.asinh).grid(row=4, column=7, pady= 1)
#==============================================================================
btnLog10 = Button(calculator, text="Log10", width=6, height=2, font=('arial', 20, 'bold'), bd = 4, 
			bg="dark blue", command =added_value.log10).grid(row=5, column=4, pady= 1)			
btnCos = Button(calculator, text="Cos", width=6, height=2, font=('arial', 20, 'bold'), bd = 4, 
			bg="dark blue", command =added_value.log1p).grid(row=5, column=5, pady= 1)
btnExpml = Button(calculator, text="Expml", width=6, height=2, font=('arial', 20, 'bold'), bd = 4, 
			bg="dark blue", command =added_value.expml).grid(row=5, column=6, pady= 1)			
btnlgamma = Button(calculator, text="lgamma", width=6, height=2, font=('arial', 20, 'bold'), bd = 4,
			bg="dark blue", command =added_value.lgamma).grid(row=5, column=7, pady= 1)
			
			
			
			

lblDisplay = Label(calculator, text = "Scientific Calculator", font = ('gabriola', 20, 'bold'), justify = CENTER)
lblDisplay.grid(row = 0, column = 4, columnspan = 4)
#================================Menu and function=============================

def donothing():
   x = 0

def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return  
def Help_access():
    Help_access = tkinter.messagebox.askyesno("You don't really need help ", "Confirm to go back please" )
    if Help_access > 0:
        return
    else:
        root.destroy()
        print("You wanted to use help, bye then!")

def Scientific():
	root.resizable(width=False, height=False)
	root.geometry("944x568+0+0")

def Standard():
	root.resizable(width=False, height=False)
	root.geometry("480x568+0+0")


menubar = Menu(calculator)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Standard", command = Standard)
filemenu.add_separator()
filemenu.add_command(label="Scientific", command = Scientific)
filemenu.add_separator()
filemenu.add_command(label="Exit", command = iExit)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Cut", command = donothing)
editmenu.add_separator()
editmenu.add_command(label="Copy", command = donothing)

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Access Help", command = Help_access)
    

root.config(menu=menubar)
root.mainloop()
