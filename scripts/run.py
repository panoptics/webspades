
def name(name):
    def dec(func):
        func.func_name = name
        return func
    return dec

@name('run')
def run(): 
    print("running")



class FatClass():
    def __init__(self):
        print("Thealien mosae are      reloaded")
    def tick():
        return
    def apply_script():
        print("APPLIED")
        return
      
f = FatClass()            
