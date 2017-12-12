import os

def snippet(fname, string, snippet_k = 6):
    f = open(fname, "r")
    f_string = f.read()
    f_words = f_string.split()
    query_words = string.split()
    query_l = len(query_words)
    f_l = len(f_words)
    i = 0
    maxscore = 0
    