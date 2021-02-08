from tkinter import *



class App:


	def __init__(self):

		#color background and font
		self.bg = '#19456b'
		self.color= "#11698e"
		self.colorFont = "#16c79a"

		#init tkinter and config
		self.root = Tk()
		self.root.title('Générateur de password')
		self.root.geometry("1080x720")
		self.root.minsize(720, 480)
		self.root.config(background=self.bg)
		self.frame = Frame(self.root, bg=self.bg)
		
		self.frame.grid_columnconfigure(0, weight=1)
		self.frame.grid_columnconfigure(1, weight=1)
		self.frame.grid_columnconfigure(2, weight=1)
		self.frame.grid_columnconfigure(3, weight=1)

		#Create widgets
		self.create_widgets()
		self.frame.pack(fill="x")

		#Title top
		self.label = Label(self.frame, text="Gestionnaire de mot de passe",font=("Helvetica", 40,"bold"), bg=self.bg, fg=self.colorFont)
		self.label.grid(row=0,column=1, columnspan=2)

	def create_widgets(self):
		#self.create_button(text="Générer un mot de passe")
		self.create_left_widget()
		#return True


	def create_left_widget(self):

		self.entry_password = Text(self.frame, bd=0,width=50, height=1, font=("Helvetica", 20), pady=15, fg=self.color)
		self.entry_password .grid(row=2, column=1, columnspan=2,pady=10)

		self.button_generate = Button(self.frame, text="Générer un mot de passe", bd=0, fg=self.color, font=("Helvetica", 15,"bold"), width=50,pady=20)
		self.button_generate.grid(row=3, column=1, columnspan=2, pady=10)
		#self.entry.insert(INSERT,"salut ça va ")

myapp = App()
myapp.root.mainloop()


		
		