#Binary search algorithm:
    # This algorithm Reduces Time Complexity
#CONCEPT OF THE ALGORITHM:

lst=[10,15,20,25,30,35,40,45,50]
#   low                     upper

# Steps :

#Step1==> Sort the list in ascending order

#Step2==> Set low=0 (always 0)
              #upper=len(listname)-1 #from above example , upper = 10 - 1 = 9

#Step3==> Calculate mid
          # mid=(low+upper)//2            (floor division is done to get integer value)

#Step4==> Check conditions :
            #1. search_element>lst[mid]
                  #low=mid+1
            #2. search_element<lst[mid]
                  #upper=mid-1
            #3. search_element==lst[mid]
                  #element found