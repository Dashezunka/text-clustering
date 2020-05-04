# Text tokenization and hierarchical clustering
Hierarchical clustering algorithm bases on the following string similarity metrics:
1. Hamming distance;
2. Levenshtein distance;
3. Damerau-levenshtein distance;
4. Jaccard similarity.

##Description
Algorithm works in the following way:
- Extracts text from the input file in `.txt` format.
- Tokenizes the text using regexps.
- Performs hierarchical clustering using one of the proposed metrics.
- Builds a dendrogram based on the results of clustering.


##Install and configure
You need to install dependencies from `requirements.txt` using
`pip3 install -r requirements.txt`   

If you want to change the standard cost of the **insert**, **delete**, **replace** and **swap** operations 
for *Levenshtein* и *Damerau-levenshtein* distances, set the values to the appropriate params in `options.py`.   
The cost is 1 by default.

##Running command
Try `python3 text-clustering.py <filepath>.txt` in the project directory.  
Choose a string similarity metrics in interactive mode.
