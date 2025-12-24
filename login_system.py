def login_system(users,max_attempts):
    
attempts_log = []
    
username = input("ENTER USERNAME: ")
 

   while not username in users:
  
        username = input("INCORRECT USERNAME. RE-ENTER:")

    for x in range(max_attempts):
 
       password = input("ENTER PASSWORD: ")
 
       if users[username] == password:
 
           attempts_log.append("pass")
     
           return True , attempts_log
        else:
   
         attempts_log.append("fail")
  
  return False , attempts_log
 



 
users = {
    "umar": "umar123",
    "mohet": "mohet456",
    "ali": "ali789"
}

 
y , x = login system(users , 5)


if y == True:

     print(f"YOU ENTERED CORRECT PASSWORD ON {x} TRIES")
else:

     print("ATTEMPTS LIMIT REACHED. WRONG PASSWORD")