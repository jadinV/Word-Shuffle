import random

def letterShuffle(word):
    """
    Shuffles the letters within a given word.

    Args:
        word (str): The input word to be shuffled.

    Returns:
        str: The shuffled word.
    """
    characters = list(word)
    random.shuffle(characters)
    shuffled_word = "".join(characters)
    return shuffled_word

def mixMidle (phrase):
    """
    Shuffles the letters in the middle of every word in a phrase
    leaving the first and last letters in place.

    Args:
        phrase (str): The input phrase to be scrambled.

    Returns:
        str: The shuffled phrase.
    """
    if (phrase == ""):
        phrase = input("Enter a phrase: ")
    
    print(phrase)
    newWords = []

    words = phrase.split(" ")
    for (i) in words:
        if (len(i) > 3):
            print(i)
            first = i[0]
            last = i[len(i) - 1]

            j = 1
            k = -1
            if (not first.isalpha()):
                first = first + i[1]
                j = 2

            if (not last.isalpha()):
                last = i[len(i) - 2] + last
                k = -2

            newWord = i[j:k]
            print(newWord)

            newWord = letterShuffle(newWord)
            print(newWord)

            fullWord = [first, newWord, last]
            newWord = "".join(fullWord)
            newWords.append(newWord)
        else:
            newWords.append(i)

    phrase = " ".join(newWords)
    print(phrase)
    return phrase

mixMidle("")