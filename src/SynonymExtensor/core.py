# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: SynonymExtensor

import logging
import os
from typing import List, Tuple, Union, Optional
import torch
from flair.data import Sentence
from flair.embeddings import TransformerWordEmbeddings

logger = logging.getLogger(__name__)


class SynonymExtensor:
    def __init__(self, embedding_method_or_model: str):

        self.word_embed_model = TransformerWordEmbeddings(embedding_method_or_model)

    def get_synonyms(self, word: str, top_n: Optional[int] = 5):

        """ Get Word Embeddings """
        word_embeddings = self._get_word_embeddings(word)

        """ Evaluate """

        """ Postprocess """

        raise NotImplemented

    def _get_word_embeddings(self, text: str):
        word = Sentence(text)
        self.word_embed_model.embed(word)
        return word[0].embedding