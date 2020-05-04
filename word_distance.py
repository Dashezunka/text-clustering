from options import *
import numpy as np

def hamming_dist(str1, str2):
    dist = abs(len(str1)-len(str2))
    for i, j in zip(str1, str2):
        if i != j:
            dist+=1
    return dist / max(len(str1), len(str2))

def levenshtein_dist(str1, str2, delete_cost=DELETE_COST, insert_cost=INSERT_COST, replace_cost=REPLACE_COST):
    size_x = len(str1) + 1
    size_y = len(str2) + 1
    matrix = np.zeros ((size_x, size_y))
    for i in range(size_x):
        matrix [i, 0] = i*delete_cost
    for j in range(size_y):
        matrix [0, j] = j*insert_cost

    for i in range(1, size_x):
        for j in range(1, size_y):
            m = 0 if str1[i-1] == str2[j-1] else replace_cost
            matrix [i,j] = min(
                matrix[i-1,j] + delete_cost,
                matrix[i-1,j-1] + m,
                matrix[i,j-1] + insert_cost
            )
    return matrix[size_x - 1, size_y - 1]

def damerau_levenshtein_dist(str1, str2, delete_cost=DELETE_COST, insert_cost=INSERT_COST,
                             replace_cost=REPLACE_COST, swap_cost=SWAP_COST):
    size_x = len(str1) + 1
    size_y = len(str2) + 1
    matrix = np.zeros ((size_x, size_y))
    for i in range(size_x):
        matrix [i, 0] = i*delete_cost
    for j in range(size_y):
        matrix [0, j] = j*insert_cost

    for i in range(1, size_x):
        for j in range(1, size_y):
            m = 0 if str1[i-1] == str2[j-1] else replace_cost
            if i > 1 and j > 1 and str1[i - 1] == str2[j - 2] and str1[i - 2] == str2[j - 1]:
                matrix [i,j] = min(
                    matrix[i-1,j] + delete_cost,
                    matrix[i-1,j-1] + m,
                    matrix[i,j-1] + insert_cost,
                    matrix[i - 2, j - 2] + swap_cost
                )
            else:
                matrix[i, j] = min(
                    matrix[i - 1, j] + delete_cost,
                    matrix[i - 1, j - 1] + m,
                    matrix[i, j - 1] + insert_cost,
                )
    return matrix[size_x - 1, size_y - 1]

def make_ngrams(str, n):
  str = (n - 1) * "*" + str + (n - 1) * '$'
  return [str[i:i+n] for i in range(len(str)-n+1)]

def jaccard_similarity(str1,str2):
    set_str1 = set(make_ngrams(str1,3))
    set_str2 = set(make_ngrams(str2,3))
    return len(list(set.intersection(set_str1, set_str2)))/len(list(set.union(set_str1, set_str2)))
