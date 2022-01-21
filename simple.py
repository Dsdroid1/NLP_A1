# Program to demonstrate the use of edit distance in a simple dictionary based corpus, comparing given word with the complete vocabulary.
import time
from editDistance import editDistance
from corpus import create_corpus

def main():
    # Initialize the corpus
    corpus = create_corpus('./sample_corpus/words.txt')
    # Get the word to be searched
    word = input("Enter the word to be searched: ")
    # Initialize the minimum edit distance
    min_distance = float('inf')
    # Initialize the closest word
    closest_word = ''
    # Initialize the frequency of the closest word [In case of tie between two words, the word with the highest frequency is selected]
    frequency = 0
    before = time.time()
    # Iterate over the corpus
    for key in corpus:
        # Calculate the edit distance between the word and the current key
        distance = editDistance(word, key)
        # If the edit distance is less than the current minimum, update the minimum and closest word
        if distance < min_distance:
            min_distance = distance
            closest_word = key
            frequency = corpus[key]
        if distance == min_distance:
            # If the edit distance is equal to the current minimum, check if the current key has a higher frequency
            if corpus[key] > frequency:
                closest_word = key
                frequency = corpus[key]
    after = time.time()
    # Print the closest word
    print(f"The closest word is {closest_word}, with an edit distance of {min_distance}")
    print(f"Time taken(s): {after - before}")

if __name__ == '__main__':
    main()