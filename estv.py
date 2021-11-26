def estv(words):
    f = open('bigramm.txt', 'r')  
    dataset = {}
    for line in f:
        for i in range(676):
            s = line.split('\t')
            dataset[s[0]] = float(s[1][:-1])*10
    let = open('letters.txt', 'r')  
    letter_dataset = {}
    for lines in let:
        for i in range(26):
            q = lines.split(',')
            letter_dataset[q[0]] = float(q[1][:-1])
    estesvennost = []
    for word in words:
        estestvennost_slova = 1
        for i in range(len(word)-1):
            estestvennost_slova *= dataset[word[i+1]+word[i]]
        estesvennost.append(estestvennost_slova)
    return(estesvennost)
