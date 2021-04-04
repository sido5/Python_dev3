''' If conditions demo2 '''


a=["salma",1,2,3,4,5.5,6,7]
b=5
c=7

'''if "salman" in a:
    print(True)
elif "salma1" in a:
    print(True)
else:
    print(False)'''

if "salma1" in a and 8 not in a:
    print("present")
elif "salma1" in a or b is 6:
    print(True)
elif 3 in a and 8 in a:
    print("in 2nd elif")
elif 5.5 in a and c is not 7:
    print("in thrd elif")
elif 8 in a and c is 7 or c is 8:
    print("in fourth elif")
else:
    print(False)







    
