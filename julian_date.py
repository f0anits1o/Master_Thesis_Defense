Question1= input('Did you use Julian Calendar or Gregorian Calendar?\n >> ')

def convertJD(D,M,Y):
    """
        convertJD is a function to convert
        Julian Date.
    """
    A = int(Y/100)
    
    if M == 1 or 2 :
        Y -=1
        M +=12
        
    if Question1=='Julian Calendar':
        B = 0
        JD = int(365.25*(Y + 4716)) + int(30.6001*(M +1)) + D + B -1524.5
        
    elif Question1=='Gregorian Calendar':
        B = 2- A + int(A/4)
        JD = int(365.25*(Y + 4716)) + int(30.6001*(M +1)) + D + B -1524.5
        
    else:
        print('Please :) write "Julian Calendar" or "Gregorian Calendar" ')
        
    print('The Julian Date of the 07 september 2023 at 09h0000 UT1 is: ', JD)    
    
convertJD(7.825, 9, 2023)

