# SynonymExtensor
開發中...

Input: Sentence(Tokenized), Word, K
Core: annoy search
Output: K synonyms  (maybe K related words)
---

Internal Database
* ckip transformers model A as Tokenizer
(Gensim phrase: new word discovery, dynamic n-gram)

* ckip transformers model B as Word Embeddings Extractor

* Prepare Wiki Corpus >> Tokenization >> Get Word Embeddings of each token >> Clustering >> Output File Or A Tree Data Structure