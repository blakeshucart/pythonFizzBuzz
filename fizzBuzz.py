

def fizzbuzz():
    num1=int(input("First number in the list:"))
    num2=int(input("Last number in the list:"))
    while num1 <= num2:
        if num1% 3 == 0 and num1% 5 == 0:
            print("fizzbuzz")
            num1+=1
            continue
            
        elif num1% 3 == 0:
            print("fizz")
            num1+=1
            continue
        elif num1% 5 == 0:
            print("buzz")
            num1+=1
            continue
        else:
            print(num1)
            num1+=1
            continue
        
fizzbuzz()
    
