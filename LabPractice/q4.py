'''
Given the integer N - the number of minutes that is passed since midnight - how many hours and minutes are
displayed on the 24h gigital clock?
The program should print two number: the number of hours (between 0 and 23) and the number of minutes
between 0 and 59).
'''

N=int(input("Enter the minutes passed since midnight: "))
hours=N//60
minutes=N%60
print(f"{hours}hours and {minutes}has passed")