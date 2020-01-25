words = ["story","emergency","fly","Quality"]
for word in words:
    if word.index('y') == len(word)-1:
        print(word.replace('y','ies'))
