#Exercise 2 shopping cart program

item = input("what item would you like to buy?: ")
price = float(input("what is the price?:" ))
quantity = int(input("How mant would you like?: "))
total = price * quantity

print(f"you have bought {quantity} x {item}/s")
print(f"your total is: {total}")