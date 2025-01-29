
class Singleton:
    _instance=None

    def __new__(cls): # __new__ will create the instance of the class and allocate the memory. and it will be called before __init__
        if not cls._instance:
            print("run ___new___")
            cls._instance=super().__new__(cls)
            cls._instance._initialize_()
            return cls._instance
        print("run ___new___")
        return cls._instance
    
    def _initialize_(self): # __init__ will initialize the instance of the class
            print("run initialize")
            self.password="password"
            self.username="admin"
            self.port="8080"
            self.host="localhost"
        


sing1=Singleton()
sing2=Singleton()

    










# #method 1
# #single thread
# class Singleton:
#     __instance = None #class variable

#     @staticmethod
#     def get_instance():
#         if Singleton.__instance is None: #if the instance is not created
#            Singleton()                   #it will create the instance (execute the __init__ method)
#         return Singleton.__instance
    
#     def __init__(self):
#         if Singleton.__instance is not None:
#             raise Exception("This class is a singleton!")
#         else:
#             Singleton.__instance = self
             
# s1= Singleton.get_instance()
# s2= Singleton.get_instance()
# print(s1 is s2) # this will return true
             
# s1 = Singleton()
# s2 = Singleton() #this will raise an exception


# #multithread safe code using locking 

# import threading

# class Singleton:
#     __instance = None  # class variable
#     __lock = threading.Lock()  # lock for thread-safety

#     @staticmethod
#     def get_instance():
#         # Ensure that only one thread can access this block at a time
#         with Singleton.__lock:
#             if Singleton.__instance is None:  # if the instance is not created
#                 Singleton()  # it will create the instance (execute the __init__ method)
#         return Singleton.__instance

#     def __init__(self):
#         with Singleton.__lock:  # lock to ensure only one instance is created
#             if Singleton.__instance is not None:
#                 raise Exception("This class is a singleton!")
#             else:
#                 Singleton.__instance = self




# #other one

# import psycopg2
# from psycopg2 import pool
# from threading import Lock

# class Database:
#     _instance = None
#     _lock = Lock()  # Thread-safety

#     def __new__(cls, db_config=None):
#         with cls._lock:
#             if cls._instance is None:
#                 if db_config is None:
#                     raise ValueError("Database configuration must be provided for the first initialization.")

#                 cls._instance = super(Database, cls).__new__(cls)
#                 cls._instance._initialize(db_config)
#         return cls._instance

#     def _initialize(self, db_config):
#         try:
#             self.connection_pool = psycopg2.pool.SimpleConnectionPool(
#                 minconn=1, maxconn=5,  # Connection pool settings
#                 database=db_config["database"],
#                 user=db_config["user"],
#                 password=db_config["password"],
#                 host=db_config["host"],
#                 port=db_config["port"]
#             )
#         except Exception as e:
#             raise Exception(f"Database connection failed: {e}")

#     def execute_query(self, query, params=None, fetch_one=False, fetch_all=False):
#         connection = None
#         try:
#             connection = self.connection_pool.getconn()
#             cursor = connection.cursor()
#             cursor.execute(query, params)

#             if fetch_one:
#                 result = cursor.fetchone()
#             elif fetch_all:
#                 result = cursor.fetchall()
#             else:
#                 connection.commit()
#                 result = None

#             cursor.close()
#             return result

#         except Exception as e:
#             raise Exception(f"Query execution failed: {e}")
#         finally:
#             if connection:
#                 self.connection_pool.putconn(connection)

#     def close_pool(self):
#         if self.connection_pool:
#             self.connection_pool.closeall()
