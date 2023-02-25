import tkinter as tk
import CriptRC5 as cript
import TextWindow as textWindow


ICON_2 = "D:\PythonProgects\pero.ico"
VERSION = "ALGORITM RC5/32/20"
TITLE = "CriptoRC5"
PASSWORD_LABLE = "Password"
IMPUT_FILE_LABLE ="Path:/file.txt"
FILD_COLOR = "#E6E6FA"
BG_COLOR ="#FFE4C4"

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(TITLE)
        self.iconbitmap(default = ICON_2)  
        self.geometry("280x280+530+220")
        self.resizable(False,False) 
        self.configure(background=BG_COLOR)
          

        self.passwordFrame = tk.Frame(borderwidth =3, relief="groove")
        self.imput_fileFrame = tk.Frame(borderwidth=3, relief="groove")
        self.resultFrame = tk.Frame(width=50,height=50, relief="groove")
        self.buttonsFrame = tk.Frame(width= 70)
        self.textwindow = None
        self.passwordVar = tk.StringVar()
        self.fileNameVar = tk.StringVar()
        self.result_text = tk.StringVar()                          
           
        self.app_lable = tk.Label(background=BG_COLOR,text = VERSION,font = 20).pack(pady=10)
        self.password_lable = tk.Label(master=self.passwordFrame,text=PASSWORD_LABLE).pack(anchor="nw") 
        self.password = tk.Entry(master=self.passwordFrame,textvariable=self.passwordVar,width=40,
                        background = FILD_COLOR,border = 3).pack(anchor="s")
        self.passwordFrame.pack(pady=5)
        self.imput_file_lable = tk.Label(master=self.imput_fileFrame,text=IMPUT_FILE_LABLE).pack(anchor="nw")   
        self.imput_file = tk.Entry(master=self.imput_fileFrame,textvariable=self.fileNameVar,width=40,
                          background =FILD_COLOR,border = 3).pack()
        self.imput_fileFrame.pack(pady=10)
        self.encript_button = tk.Button(master=self.buttonsFrame,text = "ENCRIPT",bg=BG_COLOR,width=17,
                       command = lambda:self.enriptFile(),state='disabled')
        self.encript_button.grid(row=0,column=0)              
        self.decript_button = tk.Button(master=self.buttonsFrame,text = "DECRIPT",bg=BG_COLOR,width=17,
                       command = lambda:self.decriptFile(),state='disabled')
        self.decript_button.grid(row=0,column=1)               
        self.buttonsFrame.pack(pady=10) 
        self.result_massage = tk.Label(master = self.resultFrame,
                                       textvariable=self.result_text,background=BG_COLOR).pack(anchor="c")
        self.resultFrame.pack(pady=10)

        self.passwordVar.trace_variable("w",self.checkButtons)
         
    def checkButtons(self,*args):
          _condision = len(self.passwordVar.get())>1 and len(self.fileNameVar.get())>5 
          if(_condision):
                self.encript_button.configure(state='normal',background="#FFB6C1")
                self.decript_button.configure(state='normal',background="#ADFF2F")
          else:  
                self.encript_button.configure(background="#F5DEB3",state='disabled')
                self.decript_button.configure(background="#F5DEB3",state='disabled')     

    def showResultFile(self,file_name,password,event):
          _condision = self.textwindow !=None and self.textwindow.IamIsActiv
          if(_condision):      
             self.textwindow.updateWindow(file_name,password,event)       
          else: 
              self.textwindow = textWindow.TextWindow(file_name,password,event)
                              
    def enriptFile(self):
           try:              
              _key = self.passwordVar.get()
              _input = self.fileNameVar.get()
              _correctInput = _input.replace('"',"")
              _cript = cript.Cripto(bytes(_key,"utf-8"))
              _cript.encryptFile(_correctInput) 
              self.showResultFile(_correctInput,_key,False)
              self.passwordVar.set("")             
              self.result_text.set("File is Encript!")
           except FileNotFoundError:   
            self.result_text.set("File not found in directory!") 
           except OSError:
            self.result_text.set("Not currect file type, use only .txt")           

    def decriptFile(self):
         try:         
            _key = self.passwordVar.get()
            _input = self.fileNameVar.get()
            _correctInput = _input.replace('"',"") 
            _cript = cript.Cripto(bytes(_key,"utf-8"))
            _cript.decryptFile(_correctInput)
            
            self.showResultFile(_correctInput,_key,True)
            self.passwordVar.set("")            
            self.result_text.set("File is Decript!") 
         except FileNotFoundError:
            self.result_text.set("File not found in directory!")  
         except OSError:
            self.result_text.set("Not currect file type, use only .txt")


App().mainloop()
