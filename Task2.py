# 2.	Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

def multi(N):
  list=[]
  devider=2
  while devider<=N:
    if N%devider==0:
      list.append(devider)
      N=N/devider
    else:
      devider+=1
  return list
print(multi(20))
