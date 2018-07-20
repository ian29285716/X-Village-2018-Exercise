import re

class AuthSystem:
    
    def __init__(self):

        self.username_regex = re.compile(r'Tommy7410')
        self.password_regex = re.compile(r'tom7410')
    
    def _check_username(self, username):

        if self.username_regex.search(username) is not None:
            return True
        else: 
            return False
        
    def _check_password(self, password):
  
        if self.password_regex.search(password) is not None:
            return True
        else:
            return False
        
    def authenticate(self, username, password):
        username_count=len(username)
        if username_count<6 or username_count>12:
            print("Username length error! Your username length is ",username_count)
        password_count=len(password)
        if password_count<6:
            print("Password length error! Your password length is ",password_count)
  
        pattern_username = r'(^[A-Z])'
        match_username=re.search(pattern_username,username)
        if match_username is not None:
            print(end='')
        else:
            print("Username format error! Your username is",username)

        pattern_password = r'([A-Z]+)'
        match_password = re.search(pattern_password,password)
        if match_password is not None:
            print("Password format error!") 
        else:
            print(end='')

        if not self._check_username(username):
            return
        
        if not self._check_password(password):
            return
        
        print("Welcome, Tommy7410!")

    
# Construct a object of type AuthSystem
auth = AuthSystem()

# authenticate the user's credentials
auth.authenticate("Tommy7410","tom7410")
auth.authenticate("Amy8520","amy85")
auth.authenticate("tim9630","tim9630")
auth.authenticate("Yen5566123456","yen0054321")