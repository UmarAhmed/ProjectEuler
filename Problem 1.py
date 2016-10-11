a = range(0,1000, 3)
b = range(0,1000, 5)    
print sum(a + list(set(b) - set(a)))

