def anagrams(word, words):
    word_sort = sorted(list(word))
    odp = []
    for i in words:
        if sorted(list(i)) == word_sort:
            odp.append(i)
    return odp
