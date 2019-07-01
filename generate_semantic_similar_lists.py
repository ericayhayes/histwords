#!/usr/bin/env python

# Constructs a list of neighbor words for each target term.

from representations.sequentialembedding import SequentialEmbedding
import pandas as pd
import numpy as np

save_as = "lingua_technica_neighbors.csv"
embedding_path = "embeddings/all-eng"

print("loading embeddings...")
embeddings = SequentialEmbedding.load(embedding_path, range(1850, 2000, 10))

# The set of target words to query neighbors for
targets = [
       "motor",
       "engine",
       "computer",
       "laser",
       "rocket",
       "radar",
       "microwave"
]

# The number of neighbors to query for each word
n = 100
# The start year for the range of decades to query
start_year = 1900
# The end year for the range of decades to query
end_year = 2000

# The range of decades to query
year_range = range(start_year, end_year, 10)

# Each list will contian the information to construct the final dataframe
years = []
neighbors = []
sims = []
target_term = []

print("querying neighbors by decade")
for target in targets:
    print "Current word: %s" % target
    for year in year_range:
        words = embeddings.get_seq_closest(target, year, n = n)
        neighbors.extend(words)
        years.extend([year] * n)
        target_term.extend([target] * n)

        for word in words:
            sim = (embeddings.get_embed(year).similarity(target, word))
            sims.append(sim)

print("constructing dataframe")
df = pd.DataFrame(
    {"year": years,
     "neighbor": neighbors,
     "similarity": sims,
     "target": target_term
    })


print(df.head())

df.to_csv(save_as, index = False, encoding = "utf-8")
print("done")
