from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO
import pandas as pd
import time
import sys

###########################################################################################################
#(Program):                                                                                               #
#  A program that parses live data of confimred cases and deaths of a state in the U.S and displays it on #
#  16x2 LCD screen with scrolling text, using python libraries and github                                 #
#                                                                                                         #
# - First clone covid_19 live data type 'git clone https://github.com/nytimes/covid-19-data' then         #
#   change directory to live and insert this script there                                                 #
#                                                                                                         #
# - Run Program type in terminal 'python3 covid_display.py'                                               #
# - Type 'git pull origin master' to update clone repository for updated live covid-19 data               #
#                                                                                                         #
#(Refrence):                                                                                              #
# -Covid-19 Github live data: https://github.com/nytimes/covid-19-data                                    #
#                                                                                                         #
# -RPLCD Library scrolling text: https://blog.dbrgn.ch/2014/4/20/scrolling-text-with-rplcd/               #
#                                                                                                         #
# -Pandas Library parse file: http://pandas.pydata.org                                                    #
#                                                                                                         #
# -RPLCD Library connect and set up  16x2 LCD to Raspberry PI: https://pypi.org/project/RPLCD/0.3.0/      #
###########################################################################################################

#Functions to scroll text and display on LCD screen from RPLCD Library
def write_to_lcd(lcd, framebuffer,num_cols):
  lcd.home()

  for row in framebuffer:
   lcd.write_string(row.ljust(num_cols)[:num_cols])
   lcd.write_string('\r\n')


def loop_string(string, lcd, framebuffer, row,num_cols,delay,state_string):
  count=0
  padding= ' '*num_cols
  s= padding + string + padding

  for i in range(len(s)-num_cols+1):
    framebuffer[row]=s[i:i+num_cols]
    write_to_lcd(lcd,framebuffer,num_cols)

   #Display state on LCD screen on top of state data on 16x2 LCD screen
    lcd.cursor_pos=(0,0)
    lcd.cursor_mode='hide'
    lcd.write_string(state_string)


    time.sleep(delay)



#Created dimensional list to represent rows and coloumns of LCD screen manipulate text displayed  
framebuffer=[
    '',
    '',

]
 

#Setting up LCD Screnn to Raspberry PI
lcd=CharLCD(numbering_mode=GPIO.BOARD,cols=16, rows=2, pin_rs=37,pin_e=35, pins_data=[33,31,29,23])

lcd.clear()

#Using Pandas to import csv_file
data=pd.read_csv("us-states.csv",index_col="state")

#Update live covid data from git repository 
input("Please type 'git pull origin master' to update and obtain the most recent data or press Enter: ")

#Users input to choose a U.S state
united_state_input=input ("Enter U.S State (ex:New York, Illinois, Colorado, etc..):"+" " )

#Retrieving data as a string from csv file using Pandas library
try:
 state_case_data=data.loc[united_state_input,"confirmed_cases"].astype(str)
 state_death_data=data.loc[united_state_input,"confirmed_deaths"].astype(str)
except:
 print("\n")
 print("Please enter U.S state in the correct format (ex:New York, Illinois, Colorado, etc..), Please Re-Run Program ")
 sys.exit(1)

#Print covid-19 data to terminal
print("\n")

print("State:")
print(united_state_input)

print("Confirmed Cases:")
print(state_case_data)

print("Confirmed Deaths:")
print(state_death_data)

print("\n")

#String to quit program
print("Please press/hold 'ctrl-z' to quit program")

#String to print user choice with data to LCD screen 
covid_data="Confirmed_Cases:"+" "+state_case_data +","+ " "+"Confirmed_Deaths:"+" "+ state_death_data


#Call function to display data on LCD Screen with scrolling text
while True:
 loop_string(covid_data,lcd,framebuffer,1,16,0.3,united_state_input)


GPIO.cleanup()
