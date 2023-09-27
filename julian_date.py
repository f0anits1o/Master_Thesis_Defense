#coding style: intermezzo

###############################################################################
#                                FUNCTION                                     #
###############################################################################

#1-----------------------------------------------------------------------------
def convert_jd(y, m, d):

    """
        convert_jd is a function design to convert a Gregorian date to a Julian
        date using the book astronomycal algorithm writing by Jean Meeus in
        1998 at the page 59.
        

    Parameters:
    -----------
        y: The year,
        m: The month
        d: The day.
    
    Returns:
    -------
        JD:The Julian date
    
    """
    
    
    if m == 1 or m == 2 :
        y -=1
        m +=12
    else:
        y = y
        m = m
        
        
    if y >= 1582:
        A = int(y / 100)
        B = 2 - A + int(A / 4)
    else:
        B = 0
    
    JD = int(365.25 * (y + 4716)) + int(30.6001 * (m + 1)) + d + B - 1524.5
    
    return JD
   
#2-----------------------------------------------------------------------------
def decimal_day(day, hour, minute, second):
    """
    decimal_day is a function design to convert an integer day to a decimal 
    day.

    Parameters
    ----------
    day : integer or a float number
        it must be between 1 to 31
    hour : integer
        It must be between 0 to 23
    minute : integer
        It must be between 0 to 59
    second : integer
        It must be between 0 to 59

    Returns
    -------
    d_day : decimal day

    """
    
    if hour >= 0:
        d_day = day + hour/24 + minute/(60 * 24) + second/(3600 * 24)
    
    return d_day
            

###############################################################################
#                          TRY AND EXCEPTION                                  #
###############################################################################


my_year = 0
my_month = 0
my_day = 0.0
my_hour = 0
my_min = 0
my_sec = 0

#1-----------------------------------------------------------------------------
while True:
    try:
        my_year = int(input('Please enter the year (-4712 to 9999):\n>> '))
        if -4712 <= my_year <= 9999:    
            #Historical Julian date starts -4713 and 9999 max year in python
            
            break
        else:
            print('Year out of range,it must between -4712 and 9999')
    except ValueError:
        print('Year must be numeric and a whole number between -4712 and 9999')
 
#2----------------------------------------------------------------------------

while True:
    try:
        my_month = int(input('Please enter the digit month (1 - 12):\n>> '))
        if 1 <= my_month <= 12:
            break
        else:
            print('Month out of range,it must between 1 and 12 ')
    except ValueError:
        print(' Month must be numeric and a whole number between 1 and 12 ')
        
#3----------------------------------------------------------------------------


while True:
    try:
        my_day = float(input('Please enter the  day:\n>> '))
        if 1.0 <= my_day <=31:
            break
        else:
            print('Day out of range,it must be between 1 and 31 ')
    except ValueError:
        print('Day must be an integer or a float number')
 
    
#4-----------------------------------------------------------------------------  
    
if my_day > int(my_day):
    my_day = my_day
    greg2jul = convert_jd(my_year, my_month, my_day)
else:
    print('\nEnter the Greenwich UTC time')
    
    #4-1---------------------------------------------------------------------------    
    while True:
        
        try:
            my_hour = int(input('Enter the hour (24 hour clock):\n>> '))
            if 0 <= my_hour <= 23:
                break
            else:
                print('Hour out of range,it must be between 0 and 23 ')
        except ValueError:
            print('Hour must be numeric and a whole number between 0 and 23 ')
       
                
    #4-2---------------------------------------------------------------------------    
        
    while True:
         
        try:
            my_min = int(input('Enter the number of minutes:\n>> '))
            if 0 <= my_min <= 59:
                break
            else:
                print('Minute out of range,it must be between 0 and 59 ')
        except ValueError:
            print('Minute must be numeric and a whole number between 0 and 59 ')
    
    #my_min = my minute
    
    #4-3---------------------------------------------------------------------------
    
    while True:
         
        try:
            my_sec = int(input('Enter the number of seconds:\n>> '))
            if 0 <= my_sec <= 59:
                break
            else:
                print('Second out of range,it must be between 0 and 59 ')
        except ValueError:
            print('Second must be numeric and a whole number between 0 and 59 ')
        
        # my_sec = my second
#------------------------------------------------------------------------------

    dec_day = decimal_day(my_day, my_hour, my_min, my_sec)

    greg2jul = convert_jd(my_year, my_month, dec_day)
    
""" 
gre2jul = Gregorian calendar to the Julian day number or julian date

"""
    


print('The Julian Day Number of the given date is :', greg2jul)
