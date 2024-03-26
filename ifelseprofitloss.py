cp = int(input("Enter the cost price:"))
sp = int(input("Enter the selling price:"))
if sp > cp:
    print("Profit has occured")
    print("Amount of profir is:",sp-cp)
elif sp < cp:
    print("Loss has occured")
    print("Amount of loss is:", cp-sp)
else:
    print("We have no profit no loss")

   
        