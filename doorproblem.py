doors = [0]*100
for i in range(100):
    for j in range(0,100,i+1):
        if(doors[j]==0):
            doors[j]=1
        else:
            doors[j]=0 