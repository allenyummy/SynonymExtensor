# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Data Structure

import logging
from typing import NamedTuple
import torch

logger = logging.getLogger(__name__)

class SynStruct(NamedTuple):

    id: int
    synonym: str
    score: float
    embeddings: torch.tensor

    def __eq__(self, other):
        return self.synonym == other.synonym
    
    def __repr__(self):
        return (
            f"\n"
            f"[ID]: {self.id}\n"
            f"[SYNONYM]: {self.synonym}\n"
            f"[EMBEDDINGS]: {self.embeddings.size()}"
        )