age = input('Enter your age: ')
ageseconds = int(age) * 365.25 * 24 * 60 * 60
msg = "I have been alive for {seconds} seconds. That is {years} years!".format(seconds=ageseconds,years=age)
print(msg)
print("That is " + age + " years!")