def vowelconsonant(c):
    if((c=='a' or c=='e' or c=='i' or c=='o' or c=='u') or (c=='A' or c=='E' or c=='I' or c=='O' or c=='U')):
        print("Vowel")
    else:
        print("Consonant")
c=input()
vowelconsonant(c)