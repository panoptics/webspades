from core.connection import conn



class MidClass():
    def __init__(self):
        print("The MidClass is loaded")
    def __exit__(self, type, value, traceback):
        print( "midclass remove")
        self.package_obj.cleanup()
    def __del__(self):
        print 'died'
mid = MidClass()  
conn.onConnectCallback((mid))
     