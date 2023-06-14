import time

start = time.time()

for i in range(10):
    i=i+1
print("the value of i is %2d",i)

end= time.time()
print("total time taken %d",(start))
print(f'the vlaue{end-start}')