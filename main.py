
print("Welcome to Icecream App!")
size = input("What size of Icecream do you want? S, M, or L ")
add_biscuit= input("Do you want a nuts on the Icecream? Y or N ")

price=0
if size== "S" and add_biscuit =="N":
   price+=4
   print(f"Price is {price} euro")
elif size== "S" and add_biscuit =="Y":
   price+=7
   print(f"Price is {price} euro")

elif size== "M" and add_biscuit =="N":
   price+=5
   print(f"Price is {price} euro")
elif size== "M" and add_biscuit =="Y":
   price+=8
   print(f"Price is {price} euro")

elif size== "L" and add_biscuit =="N":
   price+=8
   print(f"Price is {price} euro")
elif size== "L" and add_biscuit =="Y":
   price+=10
   print(f"Price is {price} euro")


  




