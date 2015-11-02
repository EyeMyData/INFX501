## Exercise 5: Use the following Python code that stores a string. Use the find
## method and string slicing to extract the portion of the string after the colon
## character and then use the float function to convert the extracted string into a
## floating point number. Print the number.

initialstr = 'X-DSPAM-Confidence:  0.8475'
len1 = len(initialstr)
len2 = initialstr.find(':')
finalstr = initialstr[len2+1:len1]
print(float(finalstr))

