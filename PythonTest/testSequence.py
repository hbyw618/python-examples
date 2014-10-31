names = ('Faye', 'Leanna', 'Daylen')
# print names[4] #ERROR

print names[1]


s = 'abcdefgh'

print s[::-1]
print s[::2]

print s[:0]

s = 'abcde'

for i in [None] + range(-1, -len(s), -1):
    print s[:i]



