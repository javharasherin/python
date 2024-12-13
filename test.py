a=int(input("enter a no"))
b=int(input("enter a no "))
for i in range(5):
   print("the options are 1.addition\n 2.substraction\n 3.multiplication\n 4.division\n 5.exit\n" )
   op=int(input("enter the option "))
   if(op==1):
      sum=a+b
      print("a+b=",sum)
   elif(op==2):
      difference=a-b
      print("a-b",difference)
   elif(op==3):
      product=a*b
      print("a*b",product)
   elif(op==4):
      if(b!=0):
         quotient=a/b
         print("a\b",quotient)
      else:
         print("division is not possible")
   elif(op==5):
      exit()
   else:
      print("invalid option")


