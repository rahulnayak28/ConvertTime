#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 16:31:15 2021
Mainly the CLI will convert IST timezone to CET time. The objective for this script is to primarily convert only time from CET to IST. Hence the relevance of Date is ignored.

@author: rahul
"""
#import libraries
from datetime import datetime, timedelta
from pytz import timezone

format = "%Y-%m-%d %H:%M:%S"

#current time in India (IST)
ist_time = datetime.now(timezone('Asia/Kolkata'))
print("\n Local time (IST) now is :  {}" .format(ist_time.strftime(format)))

cet_time = ist_time.astimezone(timezone('CET'))
print("\n CET Time now is : {}".format(cet_time.strftime(format)))

user_input = input("\n Do you have a new date time for which you need to see conversion? (y or yes for yes, n or no for no:) " ).lower().strip()

def convertTime():
    if user_input == 'y' or user_input == 'yes' or user_input == 'sure' or user_input == 'yo':
        user_input2 = input("\n Enter the time in CET in %H:%M:%S -> ").strip()
        new_input_time = datetime.strptime(user_input2, '%H:%M:%S' )
        
        #extracting only time from datetime
        new_input_time = new_input_time.strftime('%H:%M:%S')
        
        #print(new_input_time)
        #user_input3 = input("Enter Date in yyyy-mm-dd -> ").strip()
        
        #dummy date
        user_input3 = '2021-06-28'
        new_cet_time = user_input3 + " " + user_input2
        
        #converting variable from type str to type Datetime
        new_cet_time2 = datetime.strptime(new_cet_time, '%Y-%m-%d %H:%M:%S')
        
        #new_cet_time3 = new_cet_time2.astimezone('CET')
        new_ist_time = new_cet_time2 + timedelta(hours=3, minutes=30)
        #new_ist_time = new_cet_time2.astimezone(timezone('Asia/Kolkata'))
        print("\n New CET Time -> {}" .format(new_cet_time2.strftime('%H:%M:%S')))
        print("\n New Local Time (IST) -> {} " .format(new_ist_time.strftime('%H:%M:%S')))
        
    else:
        print("Alright, See you, Bye...")
        

convertTime()
        
    
    
    
    
    
    



   
    
    

