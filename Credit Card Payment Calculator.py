# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 14:07:38 2020

@author: Nate Bush

This program takes user input to determine the static monthly payment required
to pay down a credit card debt in the length of time specified. The user inputs
their current balance, APR, and debt-free goal measured in months and receives
a payment amount rounded to the nearest penny.
"""

# setting initial state to run
runAgain = 'y'

def goalIter(lowestPayment, newBalance):
    """
    Parameters
    ----------
    lowestPayment : a float representing the current monthly payment to test
    newBalance : a float representing the beginning account balance
    
    Returns
    -------
    newBalance : a float representing the account balance after 1 year
    """
    for i in range(goalMonths):
        unpaidBalance = newBalance - lowestPayment
        newBalance = unpaidBalance + (monthlyInterest * unpaidBalance)
    return newBalance

def getBalance():
    """
    Returns
    -------
    A value tested float representing the user's credit card balance
    """
    while True:
        try:
            balance = float(input('Enter your current balance (e.g. 9999.99): '))
            return round(balance, 2)
            break;
        except ValueError:
            print()    
            print('Invalid input, please try again.')

def getAPR():
    """
    Returns
    -------
    A value tested float representing the user's APR
    """
    while True:
        try:
            APR = float(input('Enter your current APR (e.g. 23.09): '))/100
            return round(APR, 2)
            break;
        except ValueError:
            print()
            print('Invalid input, please try again.')

def getGoal():
    """
    Returns
    -------
    A value tested integer representing the user's pay down goal in months
    """
    while True:
        try:
            goalMonths = int(input('In how many months would you like to be debt-free? '))
            return goalMonths
            break;
        except ValueError:
            print()
            print('Please enter a whole number (e.g. 12)')
                

# Loop allowing user to run calcs multiple times without program ending
while runAgain == 'y':    
    
    # prompt user for data
    balance = getBalance()
    APR = getAPR()
    goalMonths = getGoal()
    
    # initialize variables
    monthlyInterest = APR/12
    newBalance = balance
    monLower = balance/goalMonths
    monUpper = (balance * (1 + monthlyInterest)**12)/goalMonths
    epsilon = 0.01
    
    # Loop to calculate data based on user specifications. Stops when payment found.
    while abs(monLower-monUpper) > epsilon:
        
        # re-initialize newBalance for each iteration through for loop
        newBalance = balance
       
        # Calculate new payment to test with bisection
        lowestPayment = (monLower + monUpper)/2
        
        # call function goalIter() to perform calcs for specified length
        newBalance = goalIter(lowestPayment, newBalance)
        
        # set new range of possible payments
        if newBalance > 0.00:
            monLower = lowestPayment
        elif newBalance < 0.00:
            monUpper = lowestPayment
        else:
            break
    
    # print results to user and prompt for another run
    print()
    print('If you pay $', round(lowestPayment,  2), '/month and stop using', ' your'
          + ' card for new purchases, you will be DEBT-FREE in ', goalMonths, 
          'months! YOU CAN DO IT!')
    print()
    runAgain = str.lower(input('Would you like to run the numbers again? Enter(y/n): '))
    
