# for i in range(5):
#     for j in range(5):
#         print("*", end="")
#     print()   




# for i in range(5):
#     for j in range(i+1):
#         print("*", end = "")
#     print()  




# for i in range(5):
#     for j in range(5):
#         if(j<=i or j>=(5-1-i)):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()    




# for i in range(8):
#     for j in range(8):
#         if(j==i or j==(8-1-i)):
#             if(j==i):
#                 print('\\', end='')
#             else:
#                 print('/', end='')
#         else:
#             print("*", end='')            
#     print()
            


for i in range(4):
    for j in range(4):
        if(i==0 or i==3):
            print("*", end='')
        else:
            if(j==0 or j==3):
                print("*", end="")
            else:
                print(" ", end="")   
    print()        


