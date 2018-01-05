#! /usr/bin/python
 
#a=raw_input()
#a=int (a)
#print type(a)
#b =a*a
#c=b*a
#print "the cube of " ,a, " is: "
#print c

#i=0
#while i*i*i < abs(a):
 #   i=i+1
#if i*i*i !=a:
 #   print a,"is not a perfect cube"
#elif a<0:
 #   i=-i
#else:
   # print "the cube root of ",a,"is",i

#for x in range(0,100):
 #   s=str(x)
  #  if x%3==0 or x%5==0:
   #    s=""
    #    if x%3==0:
     #       s= s+"fizz"
      #  if x%5==0:
       #     s=s+"buzz"
   # print s
x=raw_input("enter your birthday: ")
y=raw_input("enter current date: ")

sp=x.split(",")
print sp
day_birth=int(sp[0])
month_birth= int(sp[1])
year_birth=int(sp[2])
q=type(year_birth)
print q
print year_birth, "and" , month_birth
print year_birth %4
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
print days_birth_month        



sp1=y.split(",")
print sp1
day_curr=int(sp1[0])
month_curr= int(sp1[1])
year_curr=int(sp1[2])
q=type(year_curr)
print q
print year_curr, "and" , month_curr
print year_curr %4

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
print days_current_month



if year_birth<year_curr:
    day1=days_birth_month - day_birth + day_curr
    month1=12-
    
