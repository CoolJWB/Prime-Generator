#*******************
#                  *
# Made by CoolJWB. *
#                  *
#*******************
#
# Runs 1 million primes in 6.8 seconds.
#

import math;
import time;
end = 1000000; # The largest prime value to generate.
millis = int(round(time.time() * 1000))
primes = [2, 3, 5, 7, 11, 13];

for x in range(15, 1000000, 2):
    if (x + 1) % 6 != 0 and (x - 1) % 6 != 0:
        continue
    for prime in primes:
        if x % prime == 0:
            break;
        elif prime > math.sqrt(x):
            primes.append(x); # Add more primes to later re-use them.
            break;
print(int(round(time.time() * 1000)) - millis); # The total runtime.
    
