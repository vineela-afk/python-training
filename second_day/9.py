from string import Template

s1= input("Enter String 1 : ")
s2= input("Enter String 2 : ")
s3= s1[::-1]+ '$'+s2[::-1]
print(s3)
