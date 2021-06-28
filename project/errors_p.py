a=10
b=0

try:
    res=a/b
    print(res)
except ZeroDivisionError:
    print("division by zero not possible")
except FileNotFoundError:
    print("no file with the specified name")
except Exception:
    print("something went wrong here!")

else:
    print("there was no exception here!!")
    res=res*10
    print(res)
finally:
    print("inside finally block, we are done with everything!")

print("done with the program")
    
try:
 if b==0:
        raise ValueError("invalid value")
    
