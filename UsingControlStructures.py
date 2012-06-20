theInput = raw_input("Enter an integer:")
#Your Code here
c = int(float(theInput))
if c % 2 == 0:
    print c, ' is even.'
else:
    print c, 'is odd.'

print "----------"

pSchoolAge = 4
votingAge = 18
presidentialAge = 59
retirementAge = 60
personsAge = input('Enter an age:')

if personsAge < pSchoolAge and personsAge < votingAge:
        print 'Too young'
    else:
       if personsAge >= votingAge:
            print 'Remember to vote'
        else:
           if personsAge > presidentialAge:
                print 'Vote for me!'
            elif personsAge < presidentialAge:
                print 'You cannot be president'
            else:
               if personsAge >= retirementAge:
                    print 'Too old'

                


print "-----------"

i = 40
while i>0:
	i-=1
	if i%3 == 0:
		print i

print "-----------"

for i in range(6, 30, 1):
	if i%2 != 0 and i%3 !=0 and i%5 !=0:
		print i

print "-----------"

i=0
r=0
while i != 1:
        r+=1
	t = r*79
	
	if t%97 == 1 :
		i = t%97
		print r, 'is the smallest positive integer'
