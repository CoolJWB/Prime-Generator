#
# Copyright 2019 CoolJWB
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
for x in range(20000):
    siffsum = (sum(map(float, str(x))))
    if (siffsum / 3).is_integer() or (siffsum / 9).is_integer() or (x % 2) == 0 or ((x % 100) / 4).is_integer() or (x % 10) == 0 or (x % 10) == 5 or ((x % 1000) / 8).is_integer():
        continue;
    
    isPrime = True
    for z in range(x + 1):
        if x != 0 and z != 0:
            if (float(x) / float(z)).is_integer() and z != 1 and z != x:
                isPrime = False
    if(isPrime and x != 0 and x != 1):
        print(x)
