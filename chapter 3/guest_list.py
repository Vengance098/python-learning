guest=['elon','tata','tesla','adi shankracharya']
print(f"I would like to meet and invite {guest[0]},{guest[1]},{guest[2]},{guest[3]}")
guest[0]='Ram ji'
print(f"I would like to meet and invite {guest[0]},{guest[1]},{guest[2]},{guest[3]}")
guest.insert(0,'optimus prime')
guest.insert(3,'Dr doom')
guest.append('god')
print(f"I would like to invite {guest[0]}, {guest[1]}, {guest[2]}, {guest[3]}, {guest[4]}, {guest[5]}, {guest[6]} to dinner!")

remove=guest.pop()
print(f"sorry,{remove.title()}")

remove2=guest.pop()
print(f"sorry,{remove2.title()}")

remove3=guest.pop()
print(f"sorry,{remove3.title()}")

remove4=guest.pop()
print(f"sorry,{remove4.title()}")

print(f"you're still invited {guest[0].title()},{guest[1].title()}")

del guest[2]
del guest[1]
del guest[0]

print(guest)