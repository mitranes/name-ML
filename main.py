import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def getPair(word):
    word_list = []
    word = "." + word + "."
    for i in range(0, len(word) - 1):
        l = (word[i], word[i + 1])
        word_list.append(l)
    return word_list


def getPairs(s):
    mydict = {}
    for word in s:
        l = getPair(word)
        for x in l:
            if x not in mydict:
                mydict[x] = 1
            else:
                mydict[x] += 1
    print(mydict)


def stringToInt(c, matrix_map):
    return matrix_map[c]


def intToString(i, matrix_map):
    return matrix_map[i]


def createNumberMatrix(s):
    matrix_map = mapUniqueCharToNum(getUniqueSortedLetters(s))
    matrix = np.zeros((len(matrix_map), len(matrix_map)))
    for word in s:
        l = getPair(word)
        for x in l:
            row_int = stringToInt(x[0], matrix_map)
            column_int = stringToInt(x[1], matrix_map)
            matrix[row_int][column_int] += 1
    return matrix


def getRowSumMatrix(num_matrix):
    row_sum = num_matrix.sum(axis=1)
    return row_sum


# below gets you the unique characters from the file
def getUniqueSortedLetters(s):
    my_set = set(())
    for word in s:
        word = "." + word + "."
        for c in word:
            my_set.add(c)
    return sorted(my_set)


# below gives you the dictionary map of {'.':0,'a':1, 'b':2, etc}
def mapUniqueCharToNum(my_set):
    lst = list(my_set)
    stoi = {s:i for i, s in enumerate(lst)}
    print('===>>>>', stoi)
    return stoi


def mapUniqueNumToChar(stoi):
    itos = {s:i for i, s in stoi.items()}
    print(f'==>>> {itos}')
    return itos


def createProbabilityMatrix(w):
    orig_matrix = createNumberMatrix(w)
    row_sum_matrix = getRowSumMatrix(orig_matrix)
    for i in range(0, len(orig_matrix)):
        for j in range(0, len(orig_matrix)):
            orig_matrix[i][j] = orig_matrix[i][j]/row_sum_matrix[i]
    showMatrix(orig_matrix, w)
    return orig_matrix


def showMatrix(matrix, w):
    print(pd.DataFrame(matrix))
    itos = mapUniqueNumToChar(mapUniqueCharToNum(getUniqueSortedLetters(w)))

    plt.figure(figsize=(16, 16))
    plt.imshow(matrix, cmap='Blues')
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            c_label = itos[i] + itos[j]
            num = "{:.2f}".format(matrix[i, j])
            plt.text(j, i, c_label, ha="center", va="bottom", color='gray')
            plt.text(j, i, num, ha="center", va="top", color='gray')
    plt.show()


def getRandomNextChar(i, prob_matrix):
    selected = np.random.choice(len(prob_matrix), p=prob_matrix[i])
    print(f"NEXT CHAR -----> {selected}")
    return selected


def produceName(prob_matrix, itos):
    produced_name = ''
    next_char_num = getRandomNextChar(0, prob_matrix)
    while itos[next_char_num] != '.':
        print("selected character --> ", itos[next_char_num])
        produced_name = produced_name + itos[next_char_num]
        print("NAME SO FAR --- ", produced_name)
        next_char_num = getRandomNextChar(next_char_num, prob_matrix)
    return produced_name


if __name__ == '__main__':
    nameFile = open(r"src/names.txt", "r")
    s = nameFile.read().split()
    new_matrix = createProbabilityMatrix(s)
    itos = mapUniqueNumToChar(mapUniqueCharToNum(getUniqueSortedLetters(s)))
    print("*******************************")
    print(produceName(new_matrix, itos))





