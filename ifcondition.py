print ("Enter your name")
name=input()
print ("Enter your age")
age=input()
print ("Hi "+name+" you're "+age+" years old" )
if int(age)<18:
    print ("you're not eligible for voting")
    diff=18-int(age)
    print ("you can vote after "+str(diff)+" years")
else:
    print ("you're eligible for voting")


