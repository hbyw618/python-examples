class C:
    def __nonzero__(self):
        return False

c=C()

print bool(c)
print bool(C)

True,False = False,True

print True,False

from decimal import Decimal
dec = Decimal(.1)
print dec

dec = Decimal('.1')
print dec

# Throw Exception
# dec + 1.0
# 
# print dec 

dec += Decimal('1.0')
print dec

print `dec`
