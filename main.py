#8.1~8.5

e2f = {"dog": "chien", "cat": "chat", "walrus": "morse"}  #8.1
print(e2f, type(e2f))
print(e2f["walrus"])  #8.2

f2e = {a: b for b, a in e2f.items()}  #8.3
print(f2e)

print(f2e['chien'])  #8.4

print(list(e2f))  #8.5

