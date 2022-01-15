# Function to calculate the edit distance between two strings, allowing for insertions, deletions, transpositions and substitutions. 

def editDistance(s1, s2):
    # Initialize the matrix
    matrix = [[0 for i in range(len(s1) + 1)] for j in range(len(s2) + 1)]
    # Fill the first row and column
    for i in range(len(s1) + 1):
        matrix[0][i] = i
    for j in range(len(s2) + 1):
        matrix[j][0] = j
    # Fill the rest of the matrix
    for i in range(1, len(s2) + 1):
        for j in range(1, len(s1) + 1):
            if s1[j - 1] == s2[i - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                # Take the min cost of insertion, deletion and substitution
                matrix[i][j] = 1 + min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1])
            # Check if transposition is possible
            if i > 1 and j > 1 and s1[j - 1] == s2[i - 2] and s1[j - 2] == s2[i - 1]:
                matrix[i][j] = min(matrix[i][j], matrix[i - 2][j - 2] + 1)
    # Return the edit distance
    return matrix[len(s2)][len(s1)]

# Driver code to test this function
def main():
    s1 = "three"
    s2 = "there"
    print(editDistance(s1, s2))

if __name__ == "__main__":
    main()