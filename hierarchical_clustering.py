import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from tokenizer import tokenize_word, tokenize_sentence

def hierarchical_clustering(text, word_distance_method):
    words = list(set(map(str.lower, tokenize_word(text))))
    X = [list(map(lambda w: word_distance_method(i, w), words)) for i in words]
    dendrogram = sch.dendrogram(sch.linkage(X,  method  = "single"), labels=words)
    plt.title('Dendrogram')
    plt.xlabel('Words')
    plt.ylabel('Word distances')
    plt.show()