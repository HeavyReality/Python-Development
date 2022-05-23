#3-1 - print a list of people on the guest list and sort that list in reverse order. Mess with case if you're bored
guestList = [ 'John', 'James', 'Jayne', 'Jerry', 'Jeremiah','Jacob']
guestList.sort()
guestList.reverse()
print(guestList[0].title())
print(guestList[1].upper())
print(guestList[2].lower())
print(guestList[3])
print(guestList[4])
print(guestList[5])

#3-2 - Add greetings to each person
greeting = f"Nice to see you [Name]!"
print(greeting.replace( "[Name]",f"{guestList[0]}"))
print(greeting.replace( "[Name]",f"{guestList[1]}"))
print(greeting.replace( "[Name]",f"{guestList[2]}"))
print(greeting.replace( "[Name]",f"{guestList[3]}"))
print(greeting.replace( "[Name]",f"{guestList[4]}"))
print(greeting.replace( "[Name]",f"{guestList[5]}"))