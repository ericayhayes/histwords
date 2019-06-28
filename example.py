from representations.sequentialembedding import SequentialEmbedding

"""
Example showing how to load a series of historical embeddings and compute similarities over time.
Warning that loading all the embeddings into main memory can take a lot of RAM
"""

if __name__ == "__main__":
    fiction_embeddings = SequentialEmbedding.load("embeddings/eng-fiction-all_sgns", range(1850, 2000, 10))
    time_sims = fiction_embeddings.get_time_sims("body", "engine")
    print "Similarity between gay and lesbian drastically increases from 1950s to the 1990s:"
    for year, sim in time_sims.iteritems():
        print "{year:d}, cosine similarity={sim:0.2f}".format(year=year,sim=sim)


    nearest1950 = fiction_embeddings.get_seq_closest("motor", 1950, n = 20)
    nearest1960 = fiction_embeddings.get_seq_closest("motor", 1960, n = 20)
    nearest1970 = fiction_embeddings.get_seq_closest("motor", 1970, n = 20)
    nearest1980 = fiction_embeddings.get_seq_closest("motor", 1980, n = 20)
    nearest1990 = fiction_embeddings.get_seq_closest("motor", 1990, n = 20)
    print "-------"
    print nearest1950
    print "-------"
    print nearest1960
    print "-------"
    print nearest1970
    print "-------"
    print nearest1980
    print "-------"
    print nearest1990
