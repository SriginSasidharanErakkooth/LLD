
#method 1
#single thread
class Singleton:
    __instance = None #class variable

    @staticmethod
    def get_instance():
        if Singleton.__instance is None: #if the instance is not created
           Singleton()                   #it will create the instance (execute the __init__ method)
        return Singleton.__instance
    
    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self
             
s1= Singleton.get_instance()
s2= Singleton.get_instance()
print(s1 is s2) # this will return true
             
s1 = Singleton()
s2 = Singleton() #this will raise an exception


#multithread safe code using locking 

import threading

class Singleton:
    __instance = None  # class variable
    __lock = threading.Lock()  # lock for thread-safety

    @staticmethod
    def get_instance():
        # Ensure that only one thread can access this block at a time
        with Singleton.__lock:
            if Singleton.__instance is None:  # if the instance is not created
                Singleton()  # it will create the instance (execute the __init__ method)
        return Singleton.__instance

    def __init__(self):
        with Singleton.__lock:  # lock to ensure only one instance is created
            if Singleton.__instance is not None:
                raise Exception("This class is a singleton!")
            else:
                Singleton.__instance = self




