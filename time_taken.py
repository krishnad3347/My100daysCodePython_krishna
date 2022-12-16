import time

start = time.time

for i in range(10):
    i=i+1
print("the value of i is %d",i)

end= time.time
print("total time taken",start-end)