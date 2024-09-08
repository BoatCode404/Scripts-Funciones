word=input('digite una palabra :')
wordLower=word.lower()
if len(wordLower)>= 3 and wordLower==wordLower[::-1]:
    print(f"{wordLower} Es un palindromo")
