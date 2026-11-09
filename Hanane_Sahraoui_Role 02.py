Role 2: Classifier
# ---------------------------------------------------------------------------

def classify(original_protein, mutated_protein, kind):
    """Return "silent", "missense", "nonsense" or "frameshift".
    - insertions and deletions are always "frameshift"
    - identical proteins mean "silent"
    - a shorter mutated protein means "nonsense"
    - anything else is "missense"
    """
    if kind in ["insertion", "deletion"]:
        return "frameshift"
    
    if original_protein == mutated_protein:
        return "silent"
    
    if len(mutated_protein) < len(original_protein):
        return "nonsense"
    
    return "missense"
