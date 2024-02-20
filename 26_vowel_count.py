def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}

        >>> vowel_count('HOW ARE YOU? i am great!')
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    lower_phrase = phrase.lower()
    vowels = set("aeiou")
    count_vowel = {}

    for ltr in lower_phrase:
        if ltr in vowels:
            count_vowel[ltr] = count_vowel.get(ltr, 0) + 1
    return count_vowel





