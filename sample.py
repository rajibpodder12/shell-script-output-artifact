#!/usr/bin/env python3
def func(*args):
    result = str(sum(args))
    print(result)
    with open('result.txt','w+') as my_file:
        my_file.write(result)

func(1,2,3,4,5,6,7,8,9,10)
