from sys import argv 

script, filename= argv #user is prompted to enter the filename

txt= open(filename) #txt opens the file mentioned by the user

print "Here's your file %r:" % filename 
print txt.read() #reads 'txt' which I directed to the sample text

print "Type the filename again:"
file_again= raw_input(">") #uses raw input instead of argv to get the same file and prints it again later

txt_again= open(file_again)

print txt_again.read()