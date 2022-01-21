# Program to demonstrate the efficient edit distance calculation using tries
import re
import time

# Class to implement a trie
class TrieNode:
    # Constructor
    def __init__(self):
        self.children = {}
        self.is_word = False

    # Inserts a word in the trie
    def insert(self, word):
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True


def correct_word_using_trie(word, trie, depth=0, word_yet='', parent_info=None, min_dist=float('inf')):
    '''
    Returns the correct word from the trie
    '''
    node = trie

    # Get the edit distance with each branch of the trie
    if parent_info == None:
        parent_row = [i for i in range(len(word) + 1)]
    else:
        parent_row = parent_info['parents']
        parent_char = parent_info['parent_char']

    current_row = [float('inf') for i in range(len(word) + 1)]
    distance_found = float('inf')
    closest_found_yet = ''
    # For every branch, DFS manner
    for char in node.children:
        word_yet += char
        # Prepare current row by edit distance
        current_row[0] = depth + 1
        for i in range(1, len(word) + 1):
            current_row[i] = min(current_row[i - 1] + 1, parent_row[i] + 1,
                                 parent_row[i-1]+(1 if word[i-1] != char else 0))
            # Check if transposition is possible
            if depth > 1 and word[i-1] == parent_char and word[i-2] == char:
                current_row[i] = min(
                    current_row[i], parent_info['grandparents'][i-2] + 1)
        # Check if this node terminates a word
        if node.children[char].is_word:
            distance_found = current_row[len(word)]
            if distance_found < min_dist:
                closest_found_yet = word_yet
                min_dist = distance_found
        # Call the function recursively, increasing depth by 1
        min_word, min_distance_found = correct_word_using_trie(
            word, node.children[char], depth + 1, word_yet, {'parents': current_row, 'parent_char': char, 'grandparents': parent_row}, min_dist)
        if min_distance_found < min_dist:
            min_dist = min_distance_found
            closest_found_yet = min_word
        word_yet = word_yet[:-1]
    return closest_found_yet, min_dist


def create_trie(path):
    '''
    Creates a trie from a given path
    '''
    trie = TrieNode()
    with open(path, 'r') as f:
        for line in f:
            # Remove all punctuation from this line
            line = re.sub(r'[^\w\s]', '', line)
            # Split the line into words
            line = line.strip().split()
            # Add the words to the trie
            for word in line:
                trie.insert(word)
    return trie

# Driver code
def main():
    file_path = './sample_corpus/words.txt'
    trie = create_trie(file_path)
    # print(trie)
    word = input('Enter a word: ')
    before = time.time()
    print(correct_word_using_trie(word, trie))
    after = time.time()
    print('Time taken(s): ', after - before)


if __name__ == '__main__':
    main()
