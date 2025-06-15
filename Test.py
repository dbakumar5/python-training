hours = int(input("Enter number of hours:\n"))
if hours >= 0:
    if hours >= 24:
        def cal_hours(str1,hours, str2):
         days= hours/24
         print(str1,hours,str2, days)
        cal_hours("Number of days for", hours, "hours is" )
    else:
       print("Enter value above 24")
else:
    print("please provide value greater than 0")
def cal_min():
   min= hours*60
   cal_min()
