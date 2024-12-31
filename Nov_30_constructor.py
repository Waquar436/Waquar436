from dotenv import load_dotenv
import os
# load_dotenv()
# email = os.getenv("EMAIL")
# pwd = os.getenv("PASSWORD")
# print(email)
# print(pwd)

class Car:
    def __init__(self):
        self.password = "Ahmad"
        self.__password_secure = "pass123"

    def change_pwd(self):
        print(self.password)

object_ref = Car()
print(object_ref.password)
# print(object_ref.__password_secure)
print(object_ref.change_pwd())
