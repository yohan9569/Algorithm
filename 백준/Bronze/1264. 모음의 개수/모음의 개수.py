vowels = ["a", "e", "i", "o", "u"]
while(True) :
    cnt_vowels = 0
    s = input()
    if s == "#": break
    
    s = s.lower()
    for c in s:
        if c in vowels: 
            cnt_vowels+=1
    
    print(cnt_vowels)