


a = [1,2,3,4]
b = [1,1,1,1]
print(id(a),id(b))

a[:] = b[:]
print(a==b)
print(id(a),id(b))


a = [1,2,3,4]
b = [1,1,1,1]
print(id(a),id(b))

a[:] = b
print(a==b)
print(id(a),id(b))


a = [1,2,3,4]
b = [1,1,1,1]
print(id(a),id(b))

a = b[:]
print(a==b)
print(id(a),id(b))

a = [1,2,3,4]
b = [1,1,1,1]
print(id(a),id(b))

a = b
print(a==b)
print(id(a),id(b))



