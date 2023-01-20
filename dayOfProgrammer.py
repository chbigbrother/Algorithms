#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#
def leapYear(year):
    leapYear = 28
    if (year / 400) == int(year / 400) or ((year / 4) == int(year / 4)  and (year / 100) != int(year / 100)):
        leapYear = 29
    if year < 1918:
        if ((year / 4) == int(year / 4)  and (year / 100) == int(year / 100)):
            leapYear = 29
    if year == 1918:
        leapYear = -15
        
    return leapYear;
        
def dayOfProgrammer(year):
    # Write your code here
    months = [31, leapYear(year), 31, 30, 31, 30, 31, 31, 30]
    days = 0
    cnt = 1
    for i in months:
        if days + i > 256:
            break;
        else:
            days += i    
            cnt += 1       
    
    dof = 256 - days
    if dof < 10:
        dof = "0" + str(dof)
    else:
        dof = str(dof)
    if cnt < 10:
        cnt = "0" + str(cnt)
    elif year == 1918:
        cnt = "0" + str(cnt - 1)
    else:
        cnt = str(cnt)
    
    ymd = dof + "." + cnt + "." + str(year)
    
    return ymd;
