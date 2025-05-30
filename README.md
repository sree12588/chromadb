Using this project to learn chromadb and ollama AI.

Prerequisite: 
=============
1. Run Ollama - llama 3.2
2. install chromadb.

Basically, a xls file which has list of defects is given as input (defect_dataset.csv). This was generate with generate-defects.py.

chromadb-with-local-defect - works.ipynb is the junyper notebook with actual functionality.

1. It creates a collection,
2. takes the csv file as input,
3. Uses local Ollama - llama 3.2 to create the embeddings.
4. Add it to the chromadb collection.
5. creates a query string and generates embedding for it.
6. Finally call collection.query() to compare the query's embeddings with the collecttion's embedding and return 10 matches.


   This works for some query but does not work for some others. May need to tweak/update llama to check more.

   Advantages : We are using only the local running AI to generate embeddings and generate response.
