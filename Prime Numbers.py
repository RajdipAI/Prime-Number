import math

print("__________        .__                                     ___.                         ") 
print("\______   \_______|__| _____   ____     ____  __ __  _____\_ |__   ___________  ______ ")
print(" |     ___/\_  __ \  |/     \_/ __ \   /    \|  |  \/     \| __ \_/ __ \_  __ \/  ___/ ") 
print(" |    |     |  | \/  |  Y Y  \  ___/  |   |  \  |  /  Y Y  \ \_\ \  ___/|  | \/\___ \  ")
print(" |____|     |__|  |__|__|_|  /\___  > |___|  /____/|__|_|  /___  /\___  >__|  /____  > ")
print("                           \/     \/       \/            \/    \/     \/           \/  ")  
 
print("Hello! I will help you to find prime numbers")
print("First enter the first number ")
n=int(input(":"))
print("Now enter the second number ")
r=int(input(":"))
x=n-1
def numbers (first,second):
    while True:
     if first < second:
         first=first+1
         c1=math.remainder(first,2)
         c2=math.remainder(first,3)
         c3=math.remainder(first,5)
         c4=math.remainder(first,7)
         if first==2:
               print(first)
         if first==3:
               print(first)
         if first==5:
               print(first)
         if first==7:
               print(first)
         if ((c1!=0.0) and (c2!=0.0) and (c3!=0.0) and (c4!=0.0)):
             print(first)
         
numbers(x,r)
    
        
 


