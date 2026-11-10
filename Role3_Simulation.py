# Role 3 Simulator:

def run_simulation(seq, trials, mode="any"):
    """Mutate the ORIGINAL seq `trials` times, translate and classify each result,
        and return a dictionary of counts, e.g. {"silent": 241, "missense": 690, ...}.
        mode="substitution" uses only substitute(); mode="any" uses random_mutation()."""
    counts = {"silent": 0, "missense": 0, "nonsense": 0, "frameshift": 0}

def run_simulation(sew, trials, mode="any"):
    counts = {"silent": 0, "missense": 0, "nonsense": 0, "frameshift": 0}

originnal_protein = translate(seq)

for i in range(trials):

    if mode == "substitution":
        mutated_seq, position = substitute(seq)
        kind = "substitution"
    else:
        mutated_seq, kind, position = random_mutation(seq)

    mutated_protein = translate(mutated_seq)

    effect = classify(original_protein, mutated_protein, kind)

    counts[effect] += 1
    
return counts
