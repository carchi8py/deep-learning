from collections import Counter

def bag_of_words(text):
    """
    By doing doing it this way vs a dictionary we keep the order of the words
    which is important.
    """
    return Counter(text.split())

test_text = 'the quick brown fox jumps over the lazy dog'

print(bag_of_words(test_text))
