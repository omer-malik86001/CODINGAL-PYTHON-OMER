numbers=(1,2,3,3,2,1)
start=0
end=len(numbers)-1

isPalindrome=True
while start<end:
    if numbers[start]!=numbers[end]:
        isPalindrome=False
    start=start+1
    end=end-1
if isPalindrome==True:
    print("it is a palindrome!")
else:
    print("it is not a palindrome")
