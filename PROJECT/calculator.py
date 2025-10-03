import math
while True:                      
    operesions = input("enter the operation:")
    if operesions == "+":
        num = int(input("enter the number:"))
        num1= int(input("enter the number:"))
        print(f"addisition:{num}+{num1}={num + num1}")
    elif operesions == "-":
        num = int(input("enter the number:"))
        num1= int(input("enter the number:"))
        print(f"subraction:{num}-{num1}={num-num1}")
    elif operesions == "*":
        num = int(input("enter the number:"))
        num1= int(input("enter the number:"))
        print(f"multipilication:{num}*{num1}={num*num1}")
    elif operesions == "/":
        num = int(input("enter the number:"))
        num1= int(input("enter the number:"))
        print(f"division:{num}/{num1}={num/num1}")
    elif operesions == "//":
        num = int(input("enter the number:"))
        num1= int(input("enter the number:"))
        print(f"floordivisition:{num}//{num1}={num//num1}")
    elif operesions == "squr":
        num = int(input("enter the value:"))
        print(f"aquare of {num} is = : {num^2}")
    elif operesions == "trig":
        angle = float(input("enter the angle:"))
        opera = input("enter the operation(sin/cos/tan):")
        radision = math.radians(angle)
        if opera == "sin":
            print(f"angle:{angle} = sin:{math.sin(radision)}")
        elif opera == "cos":
            print(f"angle:{angle} = cos{math.cos(radision)}")
        elif opera == "tan":
            print(f"angle:{angle} = tan:{math.tan(radision)}")
        else:
            print("invalid syntex")
    elif operesions == "log":
        num = int(input("enter the value:"))
        print(f"lod {num} is = {math.log10(num)}") 
    elif operesions == "exit":
        print("thak you for using culatore!")
        break
##end the code




