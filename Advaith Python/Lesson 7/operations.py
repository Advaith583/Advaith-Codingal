a = ['Apple','Guava','Mango','Banana','Kiwi']

print("Lenght of List:",len(a))
print("First Element:",a[0])
print("Last Element:",a[-1])

a.append('Papaya')
print("Updated List :",a)

a.remove('Guava')
print("Updated List :",a)

a.sort()
print("Sorted List:", a)

a.pop(1)
print("Updated List :", a)

print("Multiplication on List :", a*2)

a = a[0:4]
print("sliced List :", a)

a.clear()
print("Updated List :", a)

