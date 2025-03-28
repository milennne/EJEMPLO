def invest(word):
    if len(word)==0:
        return word
    else:
        return word[-1]+invest(word[:-1])
    
print(invest("Hola"))
print(invest("Milene"))
print(invest("Fuentes"))