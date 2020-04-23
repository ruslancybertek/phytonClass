num = int(input("Enter a number "))

print((num%5==0 and num%3==0 and "Clarusway") or (num%5==0 and "Way") or (num%3==0 and "Clarus") or (num%3!=0 and num%5!=0 and num))
