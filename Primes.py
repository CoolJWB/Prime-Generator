import math
import time
millis = int(round(time.time() * 1000)) # Store current time in ms before run.
primes = [2, 3, 5, 7, 11, 13]
for x in range(15, 1000000, 2):
    if ((x - 1) % 6 != 0 and (x + 1) % 6 != 0) or x % 5 == 0:
        continue
    xsqrt = x ** .5
    for prime in primes: # Iterates over all primes.
        if x % prime == 0:
            break
        elif prime > xsqrt:
            primes.append(x)
            break
print("Duration: " + str(int(round(time.time() * 1000)) - millis) + "ms") # Print time difference in ms after run.
