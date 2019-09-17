print()
print("This is a net income calculator. ")
print()

try:
    gross=input("Please enter gross amount: ")
    children=input("Please enter number of children: ")
    gross=int(gross)
    children+int(children)
except:
    ValueError("Please enter proper numbers: ")

percentage=0
if gross<1000:
    percentage = 10-children

if gross<2000:
    percentage=12-children

if gross<4000:
    percentage=14-children*0.5

else:
    percentage=18-float(children)*0.5

net=((100-percentage)/100)*gross
print("Your net income is: ", net)


