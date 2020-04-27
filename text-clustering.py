import word_distance, hierarchical_clustering
import sys

if len(sys.argv) < 2:
    print('Synopsis: text-clustering.py file.txt')
    exit()
with open(sys.argv[1], 'r') as file:
    text = file.read()
    print(text)
    word_dist_method = input("""To choose word distance metrics enter
    1 in case of hamming distance,
    2 in case of levenshtein distance,
    3 in case of damerau-levenshtein distance,
    4 in case of jaccard similarity:
    """)
    if word_dist_method == "1":
        hierarchical_clustering.hierarchical_clustering(text, word_distance.hamming_dist)
    elif word_dist_method == "2":
        hierarchical_clustering.hierarchical_clustering(text, word_distance.levenshtein_dist)
    elif word_dist_method == "3":
        hierarchical_clustering.hierarchical_clustering(text, word_distance.damerau_levenshtein_dist)
    elif word_dist_method == "4":
        hierarchical_clustering.hierarchical_clustering(text, word_distance.jaccard_similarity)
    else:
        print("Error! Chosen method doesn't exist, try again.")

