email=input("Enter email address: ")
if ('@' in email)&(email[-4:]==".com")&(email[-5]!="@")&(email[0]!='@'):
    print("Valid Email") #if in format : example@domain.com
else:
    print("Invalid Email")