def passcheck():
    
password = "umarbilal07"
    
entpass = input("ENTER PASS (minimun lenght 6 characters) : ")
    

    while (len(entpass) < 6 or entpass != password):
       

            
        entpass = input("INVALID PASSWORD. ENTER AGAIN: ")
        
            
            
    
return "CORRECT PASSWORD. ACCSSESS GRANTED."

x =passcheck()
print(x)          