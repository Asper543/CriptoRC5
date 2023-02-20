import tkinter as tk
import CriptRC5 as cript

ICON = "D:\PythonProgects\Cripto_Inon.ico"
VERSION = "ALGORITM RC5/32/20"
TITLE = "CriptoRC5"
PASSWORD_LABLE = "Password"
IMPUT_FILE_LABLE ="Path:/file.txt"
FILD_COLOR = "#E6E6FA"

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(TITLE)
        self.passwordFrame = tk.Frame(borderwidth=3, relief="groove")
        self.imput_fileFrame = tk.Frame(borderwidth=3, relief="groove")
        self.resultFrame = tk.Frame(width=50,height=50, relief="groove")
        self.buttonsFrame = tk.Frame(width= 70)
        self.key_value = tk.StringVar()
        self.input = tk.StringVar()
        self.result_text = tk.StringVar()              
        
        self.iconbitmap(default = ICON)  
        self.geometry("280x280")
        self.resizable(False,False)      
        self.app_lable = tk.Label(text = VERSION,font = 20).pack(pady=10)
        self.password_lable = tk.Label(master=self.passwordFrame,text=PASSWORD_LABLE).pack(anchor="nw") 
        self.password = tk.Entry(master=self.passwordFrame,textvariable=self.key_value,width=40,
                        background = FILD_COLOR,border = 3).pack(anchor="s")
        self.passwordFrame.pack(pady=5)
        self.imput_file_lable = tk.Label(master=self.imput_fileFrame,text=IMPUT_FILE_LABLE).pack(anchor="nw")   
        self.imput_file = tk.Entry(master=self.imput_fileFrame,textvariable=self.input,width=40,
                          background =FILD_COLOR,border = 3).pack()
        self.imput_fileFrame.pack(pady=10)
        self.encript = tk.Button(master=self.buttonsFrame,text = "ENCRIPT",bg="#FFB6C1",width=17,
                       command = lambda:self.enriptFile()).grid(row=0,column=0)
        self.decript = tk.Button(master=self.buttonsFrame,text = "DECRIPT",bg="#ADFF2F",width=17,
                       command = lambda:self.decriptFile()).grid(row=0,column=1)
        self.buttonsFrame.pack(pady=10) 
        self.result_massage = tk.Label(master = self.resultFrame,textvariable=self.result_text,
                              ).pack(anchor="c")
        self.resultFrame.pack(pady=10) 

    def enriptFile(self):
           try:              
              _key = self.key_value.get()
              _input = self.input.get()
              _correctInput = _input.replace('"',"")
              _cript = cript.Cripto(bytes(_key,"utf-8"))
              _cript.encryptFile(_correctInput)             
              self.result_text.set("File is Encript!")
           except FileNotFoundError:   
            self.result_text.set("File not found in directory!") 
           except OSError:
            self.result_text.set("Not currect file type, use only .txt")           

    def decriptFile(self):
         try:         
            _key = self.key_value.get()
            _input = self.input.get()
            _correctInput = _input.replace('"',"") 

           _cript = cript.Cripto(bytes(_key,"utf-8"))
            _cript.decryptFile(_correctInput)          
            self.result_text.set("File is Decript!") 
         except FileNotFoundError:
            self.result_text.set("File not found in directory!")  
         except OSError:
            self.result_text.set("Not currect file type, use only .txt")

app = App()
app.mainloop()
