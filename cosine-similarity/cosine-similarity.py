import numpy as np
import math

def cosine_similarity(a: list, b: list) -> float:
    dot = sum(a[i]*b[i] for i in range(len(a)))
    norm_a = math.sqrt(sum(x*x for x in a))
    norm_b = math.sqrt(sum(x*x for x in b))

    if norm_a == 0 or norm_b == 0 :
        return 0.0
   
    return dot/(norm_a * norm_b)
    
    """
    Returns the cosine similarity as a Python float.
    """
