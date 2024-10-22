price = int(input())

# 500 <- 100 <- 50 <- 10 <- 5 <- 1 Greedy Ok
m = 1000
remain = m - price

coin500 = 0
coin100 = 0
coin50 = 0
coin10 = 0
coin5 = 0
coin1 = 0

coin500 = remain//500
remain = remain-500*coin500

coin100 = remain//100
remain = remain-100*coin100

coin50 = remain//50
remain = remain-50*coin50

coin10 = remain//10
remain = remain-10*coin10

coin5 = remain//5
remain = remain-5*coin5

coin1 = remain//1
remain = remain-1*coin1

#print(f"500 n :{coin500} ")
#print(f"100 n :{coin100} ")
#print(f"50 n :{coin50} ")
#print(f"10 n :{coin10} ")
#print(f"5 n :{coin5} ")
#print(f"1 n :{coin1} ")
print(f"{coin500+coin100+coin50+coin10+coin5+coin1}")
