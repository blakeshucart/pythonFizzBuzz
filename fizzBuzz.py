

def fizzbuzz():
    num1=int(input("First number in the list:"))
    num2=int(input("Last number in the list:"))
    while num1 <= num2:
        if num1% 3 == 0 and num1% 5 == 0:
            if num1<0:
              print("-fizzbuzz")  
            else:
               print("fizzbuzz") 
            num1+=1
            continue
            
        elif num1% 3 == 0:
            if num1<0:
              print("-fizz")  
            else:
               print("fizz") 
            num1+=1
            continue
            
        elif num1% 5 == 0:
            if num1<0:
              print("-buzz")  
            else:
               print("buzz") 
            num1+=1
            continue
            
        else:
            print(num1)
            num1+=1
            continue
        
fizzbuzz()
    
