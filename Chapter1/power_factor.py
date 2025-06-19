#!/usr/bin/env python3

def power_factor(num, pow):
    # This is test
    """
     this function will take 2 parameters and return power of that num 
     num : number 
     pow: power
     ex:
       power_factor(2, 3) , will return 8
    """
    return (num ** pow)

if __name__ == "__main__":
    print(power_factor(3,3))
    print(power_factor.__doc__)

