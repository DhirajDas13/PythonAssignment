user_input=input("Enter a character to count number of 'e'! \n -")
print ("you have entered:", user_input), 
count=0
for x in user_input:
	if x is "e":
		count += 1
if count >= 2:
    print ("Number of e :", count)
    print ("True")

else:
	print ("false")
 

