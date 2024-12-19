def remove(L,word):
    n = []   
    for i in L:
        
        if not(i == word):
            n.append(i.strip(word))
    return n
L = ["Shaktiman","Superman","batman","Spiderman","harsh","man"]

print(remove(L,'man'))