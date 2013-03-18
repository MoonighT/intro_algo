import sys
import random
#input a list of number
l =  range(10)
random.shuffle(l)
#use binary thought to find the peak
#if left > middle, peak exist on left side
#if right > middle, peak exist on right side
#middle element is peak
print l
def find_peak(num,left,right):
    middle = (right+left-1)/2
    if left == right: 
        return num[left] 
    elif middle == right or middle == left:
        return num[middle]
    else:
        if num[middle-1] > num[middle]:
            return find_peak(num,left,middle-1)
        elif num[middle+1] > num[middle]:
            return find_peak(num,middle+1,right)
        else:
            return num[middle]

def test():
    for i in range(100):
        random.shuffle(l)
        if find_peak(l,0,len(l)-1)<0:
            print "fuck"

test()
