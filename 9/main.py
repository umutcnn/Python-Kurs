import mod

result=help(mod)
print(result)

result=help(mod.func)
print(result)

result=mod.number  
print(result)


result=mod.numbers  
print(result)

result=mod.person["name"]  
print(result)

result=mod.person["city"]  
print(result)

result=mod.person["age"]  
print(result)

p=mod.Person()
p.speak
print(result)