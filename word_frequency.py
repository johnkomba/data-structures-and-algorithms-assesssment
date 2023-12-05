import string

def word_frequency(sentence):
    words = sentence.split()
    cleaned_words = [word.strip(string.punctuation).lower() for word in words]

    frequency_dict = {}
    for word in cleaned_words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1

    return frequency_dict
