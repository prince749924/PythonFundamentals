
# 3.N students take k apples and distribute them among each student evenly.
# The remaining parts remain in the basket.
# How many apples will each single student get?
# How many apples will remain will in the basket?The programs read the numbers N and K.

N=int(input("enter the number of in class: "))
K=int(input("enter the number of in apples: "))
apples_get =K//N
remaining_apples=K%N
print(f"each student got {apples_get}")
print(f"The remaining apples are {remaining_apples}")
