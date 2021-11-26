def words_into_vector(words, estestv):
    letters = 'abcdefghijklmnopqrstuvwxyz0123456789'
    dataset = []
    i = 0
    for word in words:
        s = []
        for letter in letters:
            s.append(word.count(letter))
        s.append(estestv[i])
        s.append(len(word))
        i += 1
        dataset.append(s)
    return dataset
