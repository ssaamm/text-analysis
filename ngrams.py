#!/usr/bin/python

# Usage: ./ngrams.py textToAnalyze.txt N
# N puts the n in n-gram. In other words, N = 2 for bigrams.

import sys, itertools, re

def get_ngrams(text, n):
    ngrams = {}
    for i in xrange(len(text) - n):
        key = " ".join(text[i:i+n])
        if key not in ngrams:
            ngrams[key] = 0
        ngrams[key] += 1
    return ngrams

def combine_ngrams(ng1, ng2):
    for k, v in ng2.iteritems():
        if k not in ng1:
            ng1[k] = v
        else:
            ng1[k] += v

def make_ngrams_from_file(fn, n):
    ngrams = {}
    with open(fn, "r") as f:
        for para in [re.sub(r"[^\w\s]+", "", s).lower().split() for s in f]:
            combine_ngrams(ngrams, get_ngrams(para, n))
    return ngrams

if __name__ == "__main__":
    ngrams = make_ngrams_from_file(sys.argv[1], int(sys.argv[2]))

    for k in sorted({k : ngrams[k] for k in ngrams if ngrams[k] > 1},
            key = ngrams.get, reverse = True):
        print ngrams[k], "|", k
