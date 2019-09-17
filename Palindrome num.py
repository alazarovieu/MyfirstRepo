read=123454321
temp=read
new_number=0
while read>0:
    digit=read%10
    new_number=new_number*10+digit
    read=read//10

if(new_number==temp):
    print("Palindrome")
else:
    print("Not palindrome")

