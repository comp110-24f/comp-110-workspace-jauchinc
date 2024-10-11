"""Practice with for...in...loops"""

my_list: list[str] = ["hello", "world"]
new_list: list[str] = []
for elem in my_list:
    new_list.append(elem)
print(new_list)


pets: list[str] = ["Louie", "Bo", "Bear"]
for good_boys in pets:
    print(f"Good boy, {good_boys}!")


names: list[str] = ["Alessa", "Janet", "Vrinda"]
for name in range(0, len(names)):
    print(str(name) + ": " + names[name])
