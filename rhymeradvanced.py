import nltk
from nltk.corpus import cmudict, wordnet

# Load the CMU Pronouncing Dictionary and WordNet corpus
nltk.download('cmudict')
nltk.download('wordnet')
cmu_dict = cmudict.dict()

def get_rhyming_words(word):
    # Get the pronunciation of the input word from the CMU Pronouncing Dictionary
    try:
        pronunciation = cmu_dict[word.lower()][0]
    except KeyError:
        print(f"Error: '{word}' not found in CMU Pronouncing Dictionary")
        return []

    # Get the last syllable of the word by finding the last vowel sound
    last_vowel_index = None
    for i, sound in reversed(list(enumerate(pronunciation))):
        if any(char.isdigit() for char in sound):
            last_vowel_index = i
            break
    if last_vowel_index is None:
        print(f"Error: no vowel sound found in '{word}'")
        return []
    last_syllable = pronunciation[last_vowel_index:]

    # Find all words in the CMU Pronouncing Dictionary and WordNet corpus that rhyme with the input word
    rhyming_words = []
    for other_word, pronunciations in cmu_dict.items():
        for other_pronunciation in pronunciations:
            if other_pronunciation[last_vowel_index:] == last_syllable and other_word != word:
                rhyming_words.append(other_word)
    for synset in wordnet.synsets(word):
        for lemma in synset.lemmas():
            if lemma.name() != word:
                rhyming_words.append(lemma.name())
    return list(set(rhyming_words))

def main():
    while True:
        word = input("Enter a word ('q' to quit): ")
        if word == 'q':
            break
        rhyming_words = get_rhyming_words(word)
        print(f"Rhyming words for '{word}': {', '.join(rhyming_words)}")

if __name__ == '__main__':
    main()
