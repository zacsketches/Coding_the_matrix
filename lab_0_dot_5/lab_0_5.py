# Demonstration of basic Python functions beginning on page 16
#
# Basic addition
x =44+11*4-6/11
print(x)

m = 60*24*7
print("Number of minutes in a week: ", m)

times = 2304811//47		#Integer division
remainder = 2304811 - (times*47)
print("Remainder of 2304811 divided by 47 without using modulo: ", remainder)
print(2304811%47)

#Inequalities
print(5==4)		#False
print(4==4)		#True
print(True and not(5==4))	#True

#Conditional Expressions
x = -9
y = 1/2
val = 2**(y+1/2) if x*10<0 else 2**(y-1/2)	#val == 2
print("val is: ", val)

#Sets don't duplicate values
s1 = {1+2, 3, 'a'}
print(s1)		# {3, 'a'}

#Setd don't retain the order they were entered in
s2 = {3, 2, 1}
print(s2)		# likely result is {1, 2, 3}

#Cardinality is the length of the set acquired using len
print(len(s1)) 		# 2

#sum a set using sum()
print(sum(s2))		# 6

#sum starting at a value other than zero
print(sum(s2, 10))	# 16

