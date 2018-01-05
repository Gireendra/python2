#! /usr/bin/python
x=raw_input("enter your birthday: ")
y=raw_input("enter current date: ")

sp=x.split(",")
#print sp
day_birth=int(sp[0])
month_birth= int(sp[1])
year_birth=int(sp[2])
q=type(year_birth)
#print q
#print year_birth, "and" , month_birth
#print year_birth %4

#no. of days in birth month
month=['jan','feb','mar','apr','may','june','july','aug','sept','oct','nov','dec']
if year_birth % 4 != 0:
    if month_birth==1 or month_birth==3 or month_birth==5 or month_birth==7 or month_birth==8 or month_birth==10 or month_birth==12:
        days_birth_month=31
    elif month_birth==4 or month_birth==6 or month_birth==9 or month_birth==11:
        days_birth_month=30
    else:
        days_birth_month=28
else:
    if month_birth==1 or month_birth==3 or month_birth==5 or month_birth==7 or month_birth==8 or month_birth==10 or month_birth==12:
        days_birth_month=31
    elif month_birth==4 or month_birth==6 or month_birth==9 or month_birth==11:
        days_birth_month=30
    else:
        days_birth_month=29
#print days_birth_month        
#no. of days in birth month

print "no. of days in birth month (whole)" , days_birth_month
print "days in birth month to count",days_birth_month-day_birth

#no. of days in current month
sp1=y.split(",")
#print sp1
day_curr=int(sp1[0])
month_curr= int(sp1[1])
year_curr=int(sp1[2])
q=type(year_curr)
#print q
#print year_curr, "and" , month_curr
#print year_curr %4

if year_curr % 4 != 0:
    if month_curr==1 or month_curr==3 or month_curr==5 or month_curr==7 or month_curr==8 or month_curr==10 or month_curr==12:
        days_current_month=31
    elif month_curr==4 or month_curr==6 or month_curr==9 or month_curr==11:
        days_current_month=30
    else:
        days_current_month=28
else:
    if month_curr==1 or month_curr==3 or month_curr==5 or month_curr==7 or month_curr==8 or month_curr==10 or month_curr==12:
        days_current_month=31
    elif month_curr==4 or month_curr==6 or month_curr==9 or month_curr==11:
        days_current_month=30
    else:
        days_current_month=29
#print days_current_month
#no. of days in current month

print "no. of days in current month" , days_current_month
print "no. of days in whole current month + whole birth month" , days_current_month + days_birth_month


print "no. of days in current month",day_curr

if year_birth<year_curr:
    day1=days_birth_month - day_birth + day_curr   #no. of days in birth month+current month
    print "no. of days in birth month+current month",day1	
    month1=12-month_birth
    if month1>0:
        day2=0
        for i in range(month1):
            month_birth=month_birth+1

    

            if year_birth % 4 != 0:
                if month_birth==1 or month_birth==3 or month_birth==5 or month_birth==7 or month_birth==8 or month_birth==10 or month_birth==12:
                    days=31
                elif month_birth==4 or month_birth==6 or month_birth==9 or month_birth==11:
                    days=30
                else:
                    days=28
            else:
                if month_birth==1 or month_birth==3 or month_birth==5 or month_birth==7 or month_birth==8 or month_birth==10 or month_birth==12:
                    days=31
                elif month_birth==4 or month_birth==6 or month_birth==9 or month_birth==11:
                    days=30
                else:
                    days=29
            day2=day2+days
        d_i_b_y = day2+days_birth_month-day_birth
        print "no. of days in birth year" ,  d_i_b_y
    else:
        d_i_b_y=days_birth_month-day_birth
        print "no. of days in birth year" , d_i_b_y


    month2=month_curr
    if month2!=1:
        day_curr_year=0
        for j in range(month2-1):
            month2=month2-1
            if year_curr % 4 != 0:
                if month_curr==1 or month_curr==3 or month_curr==5 or month_curr==7 or month_curr==8 or month_curr==10 or month_curr==12:
                    days_current_month=31
                elif month_curr==4 or month_curr==6 or month_curr==9 or month_curr==11:
                    days_current_month=30
                else:
                    days_current_month=28
            else:
                if month_curr==1 or month_curr==3 or month_curr==5 or month_curr==7 or month_curr==8 or month_curr==10 or month_curr==12:
                    days_current_month=31
                elif month_curr==4 or month_curr==6 or month_curr==9 or month_curr==11:
                    days_current_month=30
                else:
                    days_current_month=29
                
            day_curr_year = day_curr_year+ days
        days_in_current_year=day_curr_year+day_curr
        print "no. of days in current year" ,days_in_current_year
    else:
        days_in_current_year=day_curr
        print "days in current year", days_in_current_year

    d_i_bo_y=d_i_b_y+days_in_current_year
    print "no. of days in birth year + current year", d_i_bo_y
    
    year_days=0
    mid_year_days=0
    for x in range(year_curr - year_birth -1):
        year_birth=year_birth+1
        if year_birth % 4!=0:
            month_birth=0
            day3=0
            for x in range(12):
                month_birth=month_birth+1
                if month_birth==1 or month_birth==3 or month_birth==5 or month_birth==7 or month_birth==8 or month_birth==10 or month_birth==12:
                    days=31
                elif month_birth==4 or month_birth==6 or month_birth==9 or month_birth==11:
                    days=30
                else:
                    days=28
                day3=day3+days
                day4=day3
            print "days in years if...",day4
        else:
            month_birth=0
            day3=0
            for x in range(12):
                month_birth=month_birth+1
                if month_birth==1 or month_birth==3 or month_birth==5 or month_birth==7 or month_birth==8 or month_birth==10 or month_birth==12:
                    days=31
                elif month_birth==4 or month_birth==6 or month_birth==9 or month_birth==11:
                    days=30
                else:
                    days=29
                day3=day3+days
                day4=day3
            print "days in years else...",day4
                    







        year_days=year_days+day4
        mid_year_days=year_days
    total_days = mid_year_days+d_i_bo_y
    print "no.of days in middle years",mid_year_days
    print "no. of days total",total_days
else:
    print "paida hue nhi aur programm chalana shuru"
    

