


a = {}

l = ['a','s','d']

a.update({k: v for k, v in enumerate(l)})
print(a)