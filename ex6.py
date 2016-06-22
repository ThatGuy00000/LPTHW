x= "There are %d types of people." % 10 #var that prints a string
binary= "binary" #another var string
do_not= "don't" #^^^
y= "Those who know %s and those who %s." % (binary, do_not) #another var with a list

print x
print y

print "I said %r." % x #prints a string that calls a var defined above
print "I also said: '%s'." % y #^^^

hilarious= False #defining a var for a TorF
joke_evaluation= "Isn't that joke so funny!? %r" #%r prints no matter what 

print joke_evaluation % hilarious #prints the previous joke var and prints false after it as defined in the 'hilarious' var

w= "This is the left side of..."
e= "a string with a right side."

print w+e #prints both the 'w' and 'e' vars next to eachother because it just uses print so they stay on the same line.