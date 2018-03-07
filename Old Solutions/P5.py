#P5, 4.15s 
import time
start_time = time.clock()

def small():
    for i in range(1000000,10000000000, 20):
        if i%11==0 and i%12==0 and i%13==0 and i%14==0 and i%16==0 and i%17==0 and i%18==0 and i%19==0:
            print(i)
            break

small()

print( time.clock() - start_time, "seconds")

