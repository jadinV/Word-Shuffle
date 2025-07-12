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

def mixMidle ():
    phrase = input("Enter a phrase: ")
    print(phrase)
    newWords = []

    words = phrase.split(" ")
    for (i) in words:
        if (len(i) > 3):
            print(i)
            first = i[0]
            last = i[len(i) - 1]

            newWord = i[1:-1]
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

mixMidle()