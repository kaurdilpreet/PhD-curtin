count = 0
while (count<100):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))


for i in range(1,100):
    if (i%10==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition") 
