import datetime
import sys

class Date:


    user_date_list=[]
    user_time_list=[]
    # initialization or constructor method of
    def __init__(self):    

        num_data=int(input('How much data do you want to enter? '))
        
        for i in range(num_data):
            
            self.user_date = input('Please enter a date(DD-MM-YYYY)')
            
            try:
                datetime.datetime.strptime(self.user_date,  "%d-%m-%Y")
                
                Date.user_date_list.append(self.user_date)
                
            except ValueError:
                    
                print("Sorry, that is in the incorrect format. Should be DD-MM-YYYY Try again!")
                sys.exit()
                
            
            self.user_time = input('Please enter a time(HH:MM) ')
            
                        
            try:
                datetime.datetime.strptime(self.user_time,  "%H:%M")
                Date.user_time_list.append(self.user_time)
                
            except ValueError:
                    
                print("Sorry, that is in the incorrect format. Should be HH-MM Try again!")
                sys.exit()
            
            
            
            print('')
            
        print('')
        print('Thank you very much. I will notify them!', "\n")
        print('...', "\n")
        
    # displayStudent method of class Student
    def displayDate(self): 
        for i in range(len(Date.user_date_list)):
            print('The' , str(i+1) + '.', 'date has been reached!','(' + str(Date.user_date_list[i]) ,'-',str(Date.user_time_list[i]) +')', "\n")
        
        
if __name__ == '__main__':
    date = Date().displayDate()     
