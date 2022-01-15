# Contains functions to create the corpus and dictionary   
import re

def create_corpus(path):
    '''
    Creates a corpus from a given path
    '''
    corpus = {}
    with open(path, 'r') as f:
        for line in f:
            # Remove all punctuation from this line
            line = re.sub(r'[^\w\s]', '', line)
            # Split the line into words
            line = line.strip().split()
            # Add the words to the corpus
            for word in line:
                if word in corpus:
                    corpus[word] += 1
                else:
                    corpus[word] = 1
    return corpus


# Driver code to test the above functions
def main():
    file_path = './sample_corpus/file1.txt'
    corpus = create_corpus(file_path)
    print(corpus)

if __name__ == '__main__':
    main()