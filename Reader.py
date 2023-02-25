ENCODING_LIST = ["utf-16","utf-8","utf-32","cp1252", "cp437"]

class Reader:

    def __init__(self,filename):
        self.file = filename 
        self.encode = ENCODING_LIST[0]

    def setFileName(self,file_name):
        self.file = file_name

    def read(self): 
        _result = "Have't codec!!!"
        for encoder in ENCODING_LIST:
            try:
                _inp =  open(self.file,encoding=encoder)                
                _result = _inp.read()
                break
            except UnicodeError:
              continue
        return _result 
