from tkinter import *
import time

class Kalkulator:
	def __init__(self, master):
		self.master = master
		master.title("Kalkulator")
		master.resizable(0,0)

		self.user = Entry(master, borderwidth=8, width=40, exportselection=0, font=("Arial", 15))
		self.user.grid(row=0, pady=10, padx=10, columnspan=4)

		self.TC = Button(master, text="C", font=("Arial", 12), width=12, height=3, command=lambda:self.HapusSemua())
		self.TC.grid(row=1, column=0, padx=2)

		self.TDel = Button(master, text="Del", font=("Arial", 12), width=12, height=3, command=lambda:self.Hapus())
		self.TDel.grid(row=1, column=1, padx=2)

		self.TPer = Button(master, text="%", font=("Arial", 12), width=12, height=3, command=lambda:self.Persen())
		self.TPer.grid(row=1, column=2, padx=2)

		self.TBagi = Button(master, text="/", font=("Arial", 12), width=12, height=3, command=lambda:self.num("/"))
		self.TBagi.grid(row=1, column=3, padx=2)		


		self.T7 = Button(master, text=7, font=("Arial", 12), width=12, height=3, command=lambda:self.num(7))
		self.T7.grid(row=2, column=0, padx=2)

		self.T8 = Button(master, text=8, font=("Arial", 12), width=12, height=3, command=lambda:self.num(8))
		self.T8.grid(row=2, column=1, padx=2)

		self.T9 = Button(master, text=9, font=("Arial", 12), width=12, height=3, command=lambda:self.num(9))
		self.T9.grid(row=2, column=2, padx=2)

		self.Tkali = Button(master, text="*", font=("Arial", 12), width=12, height=3, command=lambda:self.num("*"))
		self.Tkali.grid(row=2, column=3, padx=2)


		self.T4 = Button(master, text=4, font=("Arial", 12), width=12, height=3, command=lambda:self.num(4))
		self.T4.grid(row=3, column=0, padx=2)

		self.T5 = Button(master, text=5, font=("Arial", 12), width=12, height=3, command=lambda:self.num(5))
		self.T5.grid(row=3, column=1, padx=2)

		self.T6 = Button(master, text=6, font=("Arial", 12), width=12, height=3, command=lambda:self.num(6))
		self.T6.grid(row=3, column=2, padx=2)

		self.Tkur = Button(master, text="-", font=("Arial", 12), width=12, height=3, command=lambda:self.num("-"))
		self.Tkur.grid(row=3, column=3, padx=2)


		self.T1 = Button(master, text=1, font=("Arial", 12), width=12, height=3, command=lambda:self.num(1))
		self.T1.grid(row=4, column=0, padx=2)

		self.T2 = Button(master, text=2, font=("Arial", 12), width=12, height=3, command=lambda:self.num(2))
		self.T2.grid(row=4, column=1, padx=2)

		self.T3 = Button(master, text=3, font=("Arial", 12), width=12, height=3, command=lambda:self.num(3))
		self.T3.grid(row=4, column=2, padx=2)

		self.Ttam = Button(master, text="+", font=("Arial", 12), width=12, height=3, command=lambda:self.num("+"))
		self.Ttam.grid(row=4, column=3, padx=2)	


		self.Tkoma = Button(master, text=".", font=("Arial", 12), width=12, height=3, command=lambda:self.num("."))
		self.Tkoma.grid(row=5, column=0, padx=2)

		self.T0 = Button(master, text=0, font=("Arial", 12), width=12, height=3, command=lambda:self.num(0))
		self.T0.grid(row=5, column=1, padx=2)

		self.Tsd = Button(master, text="=", font=("Arial", 12), height=3, width=26, command=lambda:self.SamaDengan())
		self.Tsd.grid(row=5, column=2, columnspan=2)

	def num(self, number):
		err = "Error"
		if self.user.get() == err:
			self.user.delete(0, END)
		self.current = self.user.get()
		self.user.delete(0,END)
		self.user.insert(0, str(self.current) + str(number))

	def HapusSemua(self):
		self.user.delete(0,END)

	def Hapus(self):
		a = int(len(self.user.get()))
		self.user.delete(a-1)

	def SamaDengan(self):
		try:
			hasil = eval(self.user.get())
			self.user.delete(0, END)
			self.user.insert(0, hasil)
		except Exception:
			self.user.delete(0, END)
			self.user.insert(0, 'Error')

	def Persen(self):
		try:
			x = eval(self.user.get())
			hasil = x / 100
			self.user.delete(0, END)
			self.user.insert(0, hasil)
		except Exception:
			self.user.delete(0, END)
			self.user.insert(0, 'Error')

if __name__ == "__main__":
	root = Tk()
	gui = Kalkulator(root)
	root.mainloop()