#write a python program to calculate a simple interest
#This program was written by Ashok Chodipalli Fullstack Developer
#The simple formula for simple interest is I = P * T * R / 100
#------------------------------------------------------------------------
# I = Interest
# P = Principal amount
# T = Time Period
# R = Rate of Interest
# take R = 10%

#inputs are taken here
principal_amount = int(input())
time_period = int(input())
rate_of_interest = 10/100

#Interest is calculated here
interest = principal_amount * time_period * rate_of_interest

#printing the out as shown below
print("The simple interest is : " + str(interest))
