print(" type '1' : addition \n type '2' : subtraction \n type '3' : multiplication \n type '4' : quotient  \n type '5' : remainder")

a = int(input("type:"))

if (a==1):
    no1 = int(input('enter no 1:'))
    no2 = int(input('enter no 2:'))
    sum = no1 + no2
    print(f'the sum is {sum}')
    
elif (a==2):
    no1 = int(input('enter no 1:'))
    no2 = int(input('enter no 2:'))
    diff = no1 - no2
    print(f'the difference is {diff}')
    

elif (a==3):
    no1 = int(input('enter no 1:'))
    no2 = int(input('enter no 2:'))
    product = no1 * no2
    print(f'the product is {product}')
    

elif (a==4):
    no1 = int(input('enter no 1:'))
    no2 = int(input('enter no 2:'))
    quo = int(no1 / no2)
    print(f'the quotient is {quo}')
    
elif (a==5):
    no1 = int(input('enter no 1:'))
    no2 = int(input('enter no 2:'))
    rem = no1 % no2
    print(f'the remainder is {rem}')
    
else :
    print('wrong choice')

    

