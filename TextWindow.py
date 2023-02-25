import tkinter as tk
import Reader as reader
import CriptRC5 as cript


ENCODING_LIST = ["utf-16","utf-8","utf-32","cp1252", "cp437"]
BG_COLOR ="#FFE4C4"

class TextWindow(tk.Tk):
    def __init__(self,file_name,password,event):
        super().__init__()
        self.title(file_name)
        self.geometry("690x520+820+220")
        self.resizable(False,False)
        self.configure(background=BG_COLOR)
        self.IamIsActiv = True 
        self.passwordVar = tk.StringVar(self,password)
        self.fileNameVar = tk.StringVar(self,file_name)
        self.eventVar = tk.BooleanVar(self,event)
        self.reader = reader.Reader(filename = file_name)
        file_text = self.reader.read()   
        self._text_view = tk.Text(self,width=60,height=19,border=3,font=1)
        self._text_view.insert("1.0",file_text)
        self.encript_button = tk.Button(self,text="ENCRIPT",background="#F4A460",
                                        borderwidth=1,disabledforeground=BG_COLOR,
                                        command=lambda:self.__encriptFile())
        self.encript_button.pack(padx=10,pady=10,anchor="nw")
        if(event==False):self.encript_button.configure(background=BG_COLOR,borderwidth=0
                                                       ,state='disabled')
        self._text_view.pack(anchor = "c")
        self.protocol("WM_DELETE_WINDOW",self.on_closed)
            
    def on_closed(self):
         self.IamIsActiv = False
         self.destroy()

    def updateWindow(self,file_name,password,event):
        self.fileNameVar.set(file_name)
        self.passwordVar.set(password)
        self.eventVar.set(event)
        self.__updateWindowInside()

    def __updateWindowInside(self):
        self.title(self.fileNameVar.get())
        self.reader.setFileName(self.fileNameVar.get())
        if(self.eventVar.get()==True):self.encript_button.configure(background = "#FFB6C1",
                                                                    borderwidth = 1,state = 'normal') 
        else: self.encript_button.configure(background=BG_COLOR,borderwidth=0,state = 'disabled') 
        _newText = self.reader.read() 
        self._text_view.delete("1.0","end")
        self._text_view.insert("1.0",_newText)          

    def __encriptFile(self):
            _password = self.passwordVar.get()
            _fileName = self.fileNameVar.get()
            _cript = cript.Cripto(bytes(_password,"utf-8"))
            _cript.encryptFile(_fileName)
            self.eventVar.set(False)
            self.__updateWindowInside()
