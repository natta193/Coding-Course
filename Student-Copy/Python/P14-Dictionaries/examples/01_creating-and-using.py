ages = {"Ana": 13, "Ben": 15, "Cai": 12}

print(ages["Ben"])        # 15
ages["Dev"] = 14          # add
ages["Ana"] = 14          # update
del ages["Cai"]           # delete
print(ages)
print("Ben" in ages)      # True (checks keys)
print(len(ages))          # 3

print(ages["Zoe"])        # KeyError!
print(ages.get("Zoe"))    # None – no crash
print(ages.get("Zoe", 0)) # 0 – your default
