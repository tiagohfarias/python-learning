#Lesson contain
n1=int(input('Right one number:'))
n2=int(input('Right other number:'))
s= n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
r=n1%n2
e=n1**n2
print('The sum is {}, multiplication is {}, division is {:.3f},'.format (s,m,d) ,end=' and ')
print('entire divison is {}, rest is {}, and exponencial is {}'.format (di,r,e))
print('')

#Challenger005 - Predecessor and Sucessor
n1=int(input('Right a number:'))
pred=n1-1
suc=n1+1
print('The predecessor of {} is {}, and the sucessor is {}'.format(n1,pred, suc))
print('')
#Second form of 005 - Short form -
n1=int(input('Right a number:'))
print('The predecessor of {} is {}, and sucessor is {}'.format(n1, (n1-1),(n1+1)))

#Challenger006 - Double, Triple and Square Root
n1=int(input('Right a number:'))
double=n1*2
triple=n1*3
sr=n1**(1/2)
print('The double of this number are {}, the triple are {}, and square root are {:.3f}'.format(double,triple,sr))
print('')

#Challenger007 - Arithmetic mean
n1=float(input('Right your H1 note:'))
n2=float(input('Right your H2 note:'))
arithmeticmean=(n1+n2)/2
print('The arithmetic mean of {:.2f} and {:.2f} is {:.2f}'.format(n1,n2,arithmeticmean))
print('')

#Challenger008 - Meters, centimeters and milimeters
m=float(input('Right anything with meters:'))
cm=m*100
mm=m*1000
print('{} meters on centimeters is {}, and milimeters is {}'.format(m,cm,mm))
#one more of this
m=float(input('Right distance in meters: '))
dm=m*10
cm=m*100
mm=m*1000
dam=m/10
hm=m/100
km=m/1000
print('{} meters is the same thing that:')
print('{:.0f} dm'.format(dm))
print('{:.0f} cm'.format(cm))
print('{:.0f} mm'.format(mm))
print('{} dam'.format(dam))
print('{} hm'.format(hm))
print('{} km'.format(km))

#Challenger009 - Table multiplication
n=int(input('Choose one number for view your multiplication table: '))
print('='*15)
print('{} x {} = {}'.format(n,1,n*1))
print('{} x {} = {}'.format(n,2,n*2))
print('{} x {} = {}'.format(n,3,n*3))
print('{} x {} = {}'.format(n,4,n*4))
print('{} x {} = {}'.format(n,5,n*5))
print('{} x {} = {}'.format(n,6,n*6))
print('{} x {} = {}'.format(n,7,n*7))
print('{} x {} = {}'.format(n,8,n*8))
print('{} x {} = {}'.format(n,9,n*9))
print('{} x {} = {}'.format(n,10,n*10))
print('='*15)

#Challanger010 - Conversion reais to dollar
reais=float(input('How much money in reais do you have? '))
dollar=reais/5.33
euro=reais/6.05
iene=reais/0.033
print('So, if this money you can have buy {:.2f} dollars, {:.2f} euros and {:.2f} ienes'.format(dollar,euro,iene))

#Challanger011 - How many paint buckets needs to paint one wall
h=float(input('Enter a height for the closest wall of you: '))
w=float(input('Now enter a width for the same wall: '))
s=h*w
p=s/2
print('Your wall have {}x{} and your area is {}m².For paint this wall, y´ll need {:.2f}L bucket of paint'.format(h,w,s,p))


#Challanger012 - Discount of 5%
p=float(input('Whats the price of this product? R$'))
np=p-0.05*p
print('The old price was R${:.2f},but after the discount, the new price are R${:.2f}'.format(p,np))

#Challanger013 - Salary adjustment
s=float(input('What is your actual salary? R$'))
ns=s+0.15*s
print('Your new salary,with the adjustment, is R${:.2f}'.format(ns))

#Challanger014 - Celsius to Fahrenheit
c=float(input('Report the temperature in Celsius: '))
f=9*c/5+32
print('The temperature in Fahrenheit is {:.1f} F'.format(f))

#Challanger015 - Car rental
day= int(input('How many days you use the car? '))
km= float(input('How many kilometers do you use? '))
cost= (day*60) + (km*0.15)
print(f'The cost of your car is U${cost:.2f} dollars')


