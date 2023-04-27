sample = open('fixtures/flat_resalt.txt')
l = sample.read()
print(l)

for el in l.split('\n'):
    print(el)
