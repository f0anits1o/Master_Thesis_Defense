Question1= input('Did you use Julian Calendar or Gregorian Calendar?\n >> ')

def convertJD(year,month,days,hour,minute,second):

    """
        convertJD is a function design to Calculates the Julian date
        for a given date and time.

    Args:
        year: The year.
        month: The month.
        day: The day.
        hour: The hour.
        minute: The minute.
        second: The second.

    Returns:
        The Julian date
    """

    A = int(year/100)
    C = int(365.25*(year + 4716))
    E = int(30.6001*(month +1))
    fractional_part_of_day = (hour + minute / 60.0 + second / 3600.0) / 24.0

    if month == 1 or 2 :
        year -=1
        month +=12
        
    if Question1=='Julian Calendar':
        B = 0
        JD = C + E + days + B + fractional_part_of_day -1524.5
        return JD
    
    elif Question1=='Gregorian Calendar':
        B = 2- A + int(A/4)
        JD = C + E + days + B + fractional_part_of_day -1524.5
        return JD
   
    else:
        print('Please :) write "Julian Calendar" or "Gregorian Calendar" ')
    
        
    
# Example usage:

year = 2023
month = 9
day = 7
hour = 9
minute = 0
second = 0

Julian_date = convertJD(year, month, day, hour, minute, second)

print('The Julian date of the given date is :', Julian_date)