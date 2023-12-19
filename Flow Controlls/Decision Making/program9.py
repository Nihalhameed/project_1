#Problem to obtain marks of a student

#sub1
#sub2
#sub3
#sub4

#totalmarks

#180marks A+
#160-179 A
#140-159 B+
#120-139 B
#100-119 C+
#80-99 C
#FAIL


sub1=int(input("Enter the marks of first subject: "))
sub2=int(input("Enter the marks of second subject: "))
sub3=int(input("Enter the marks of third subject: "))
sub4=int(input("Enter the marks of fourth subject: "))
total_marks=sub1+sub2+sub3+sub4
print("Total marks is",total_marks)

if(total_marks>=180):
    print("Grade is A+")
elif(total_marks>=160)&(total_marks<=179): #elif(160<=total_marks<=179)
    print("Grade is A")
elif(total_marks>=140)&(total_marks<=159):
    print("Grade is B+")
elif(total_marks>=120)&(total_marks<=139):
    print("Grade is B")
elif(total_marks>=100)&(total_marks<=119):
    print("Grade is C+")
elif(total_marks>=80)&(total_marks<=99):
    print("Grade is C")
else:
    print("FAIL")