def count_words(str_engesentence):
    sentence = str_engesentence.split()
    return len(sentence)

print(count_words('From Stettin in the Baltic to Trieste in the Adriatic an iron curtain has descended across the Continent.') == 18)