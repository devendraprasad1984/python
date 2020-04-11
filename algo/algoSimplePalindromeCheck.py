# any word like mom,dad,abcba are palindrome, reading from any side, they make same words

def isPalindrome(word):
    if len(word)<=1:
        return True
    else:
        left=0
        right=len(word)-1
        while left<right:
            if word[left]==word[right]:
                left+=1
                right-=1
            else:
                return False
        return True

def isPalindrom2(word):
    if len(word)<=1:
        return True
    else:
        if word[0]==word[-1]:
            new_word=word[1:-1]
            return isPalindrom2(new_word)
        else:
            return False

def isPalindrom3(word):
    return word==''.join(reversed(word))

def isPalindrom4(word):
    return word==word[::-1]

def main_palindrome():
    words=['mom','dad','dada','abcba','zbybs']
    print("words are:",words)
    print("palindrom using methond1")
    for ex in words:
        if isPalindrome(ex):
            print(ex)

    print("palindrom using methond2")
    for ex in words:
        if isPalindrom2(ex):
            print(ex)

    print("palindrom using methond3")
    for ex in words:
        if isPalindrom3(ex):
            print(ex)

    print("palindrom using methond4")
    for ex in words:
        if isPalindrom4(ex):
            print(ex)

if __name__ == '__main__':
    main_palindrome()
