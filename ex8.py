#Formatter var has 4 %r's in qoutes so in the print statements it prints all the 4 strings, for the one that prints 'formatter' it prints the %e*4*4 because it uses the variable to print the variable

formatter= "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
		"I had this thing.",
		"That you could type up right.",
		"But it didn't sing.",
		"So I said goodnight."
		)