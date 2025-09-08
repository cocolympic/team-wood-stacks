
from typing import List, Dict

def total_scores(scores: Dict[str, List[int]]) -> Dict[str, int]:
    return {name: sum(points) for name, points in scores.items()}