# --------------
#Code starts here

def palindrome(num):
    check_palindrome = lambda x : str(x) == str(x)[::-1]
    num += 1
    while(True):
        if check_palindrome(num):
            break 
        else:
            num += + 1
    return num
print(palindrome(123))
print(palindrome(1331))


# --------------
#Code starts here
def a_scramble(str_1, str_2):
    str_1 = str_1.lower()
    str_2 = str_2.lower()
    for i in str_2:
        print(i, str_1)
        if i in str_1:
            str_1 = str_1.replace(i, "", 1)
        else: 
            return False
    return True

print(a_scramble("baby shower","shows"))
# print(a_scramble("Tom Marvolo Riddle","Voldemort"))
#print(a_scramble("ticket","chat"))


# --------------
#Code starts here
def check_fib(num):
    a = 1
    b = 0
    while(num >= a):
        if a == num:
            return True
        else:
            c = a + b
            b = a 
            a = c
    return False

print(check_fib(145))
print("#########")
print(check_fib(377))


# --------------
#Code starts here

#Function to compress string
def compress(word):
    word=word.lower()
    mist=[]
    l=0
    while(l<len(word)):
        m=word[l]
        j=0
        while(l<len(word) and word[l]==m):
                 j=j+1
                 l=l+1    

        mist.append(m)
        mist.append(str(j))
    
    return ''.join(mist)

#Code ends here


# --------------
#Code starts here
def k_distinct(string, k):
    return len(set(string.lower())) == k


