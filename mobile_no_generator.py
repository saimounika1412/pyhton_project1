#import module
import random as r

#A valid phone number contains 10 digits
ph_no=[]

#the first no may be 6 or 7 or 8 or 9 for indian phone numbers
ph_no.append(r.randint(6,9))

#the remaining 9 numbers can be in 0 to 9
for i in range(1,10):
    ph_no.append(r.randint(0,9))

#generating a phone number
for i in ph_no:
    print(i,end='')