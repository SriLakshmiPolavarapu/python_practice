class User:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        
class UserData:
    def __init__(self):
        self.users={} 
        
    def createUser(self,name,age):
        if name not in self.users:
            self.users[name] = User(name,age)
            return "created"
        else:
            return False
        
    def getUser(self, age):
        return self.users.get(age)
    
    def update_user(self, name, age, new_name=None, new_age=None):
        user = self.users.get(name)
        user = self.users.get(age)
        if user:
            if new_name:
                user.name = new_name
            if new_age:
                user.age = new_age
            return "data updated"
        else:
            return "not updated"  
        
        
    def deleteUser(self, age):
        if age in self.users:
            del self.users[age]
            return True
        else:
            return False
        
        
user_obj = UserData()

created1 = user_obj.createUser('sri',23)
created2 =user_obj.createUser('Vinay',28)

print(created1)
print(created2)

get = user_obj.getUser(24)
print(get)

update = user_obj.update_user('sri',23, new_name='lakshmi',new_age=25)
print(update)

delete = user_obj.deleteUser(23)
print(user_obj.getUser(24))
print(user_obj.getUser(28))


        
                
            
            
                      