#!/bin/bash

# This example downloads the English fiction embeddings and tests the
# performance of the 1990s embeddings on the Bruni MEN similarity tast

mkdir embeddings
cd embeddings
curl -o all-eng.zip http://snap.stanford.edu/historical_embeddings/eng-all_sgns.zip
unzip all-eng.zip
mv sgns all-eng
cd ..
python -m vecanalysis.ws_eval embeddings/all-eng/1990 vecanalysis/simtestsets/ws/bruni_men.txt --type SGNS
