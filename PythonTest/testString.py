aString = 'Hello World!'   #using single quotes
anotherString = 'Python is cool!' #double quotes

print aString               # print, no quotes!
print anotherString

s = str(range(4))     # turn list to string
print s


aString = 'Hello World!'
print aString[0]
print aString[1:5]
print aString[6:]


aString = 'Hello World'
print aString[0]
print aString[1:5]
print aString[6:]

aString = aString[:6] + 'Python'
print aString
aString = 'different string altogether'
print aString



# to remove Character
aString = 'Hello World'
aString = aString[:3] + aString[4:]
print aString

aString = ''
print aString

del aString



#string compare
str1 = 'abc'
str2 = 'lmn'
str3 = 'xyz'
print str1 < str2

print str2 != str3

print str1 < str3 and str2 == 'xyz'


#sequence operator
aString = 'abcd'
len(aString)
final_index = len(aString) -1
print final_index

print aString[0]
print aString[1:3]
print aString[2:4]
# print aString[4] error

print aString[-1]
print aString[-3:-1]
print aString[-4]

print aString[2:]
print aString[1:]
print aString[:-1]
print aString[:]


print 'bc' in 'abcd'

print 'n' in 'abcd'
print 'nm' not in 'abcd'

import string
print string.uppercase
print string.lowercase
print string.letters
print string.digits

alphas = string.ascii_letters + '_'
nums = string.digits

print "Welcome to the Identifier Checker v 1.0"
print 'Testees must be at least 2 chars long.'
myInput = raw_input('Identifier to test?')


if len(myInput) > 1 :
    if myInput[0] not in alphas:
        print '''Invalid: first symbol must be alphabetic'''
    else:
        for otherChar in myInput[1:]:
            if otherChar not in alphas + nums:
                print """Invalid: remaining 
                    symbols must be alphabetic"""
                break
            else:
                print "Okay as an identifier"
                
                

s= 'Spanish' + ' Inquisition' + 'Made Easy'
print s
print string.upper(s[:3] + s[20]) #alphac (see below) 
                
print '%s %s' % ('Spanish','Inquisition')
s = ' '.join(('Spanish', 'Inquisition', 'Made Easy'))
print s             

('%s%s' % (s[:3], s[20])).upper()

#Compile-Time Concatenation
foo = "Hello" 'World'
print foo

# Coercion to Unicode
s = 'Hello' + u' ' + 'World' + u'!'
print s

print 'Ni!' * 3
