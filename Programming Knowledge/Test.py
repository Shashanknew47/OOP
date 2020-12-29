s1 = {1,3,4,5,6,7,}
s2 = {2,4,6,8,10}
s3 = {1,3,4}
s4 = {2,4,9}

print('s1: ',s1)
print('s1: ',s2)
print('union: ', (s1|s2))
print('intersactin: ', (s1&s2))
print('diffrence s1-s2 :', (s1-s2))
print('diffrence s2-s1 :', (s2-s1))
print('assymetric difference s1^s2: ',(s1^s2))
print('s3<=s1 issubset :', (s3<=s1))
print('s2<=s4 issuperset :', (s2 <= s4))

print('-------------------------------------------')

# print(id(s1))
# s1 = s1|s2
# print(id(s1),s1)

# print('-------------------------------------------')
# print(id(s1))
# s1  |= s2
# print(id(s1), s1)

print(id(s2))
s2 =  s2&s1
print(id(s2), s2)


print('-------------------------------------------')
print('-------------------------------------------')

def combine(string,target):
    target.update(string.split())

result = set()

combine('This is my',result)
combine('future, which is bringht',result)
print(result)

def cleanup(combined):
    words = {'my','and','a','is','or'}
    combined -=words

cleanup(result)    
print(result)



