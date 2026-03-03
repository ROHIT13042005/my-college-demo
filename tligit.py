 # trafic light code


colour = input("enter the colour:")
if(colour == "green"):
    print(" you go now")
elif(colour == "red"):
    print(" you can be not go")
elif(colour == "yellow"):
    print("look")
else:
    print("light is broken")




    # GRADE OF STUDENT
     
marks =int(input("enter the marks:"))
if(marks>=90 and marks>=80):
    print("grade A")
elif(marks>=80 and marks>=70):
    print("grade B")
elif(marks>=70 and marks>=60):
    print("grade C")
else:
    print("grade D ")


    # eligible for vote or not

age = int(input("enter the age:"))
if(age>= 18):
    print("eligible for vote")
elif(age<18):
    print(" you not eligible for vote")
elif(age==18):
    print(" you are adult")
else:
    print("election is cancel")