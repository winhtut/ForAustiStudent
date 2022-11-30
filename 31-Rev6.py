data = input("Shall we begin y/n?")

if(data=='y'):
    number=0
    print("Please enter 3 numbers")
    for i in range(3):
        n = int(input("Enter a number:"))
        number = n+number
    print("The sum of the 3 numbers multiplied by 3 is:",number*3)    
else:
    print("See you later")