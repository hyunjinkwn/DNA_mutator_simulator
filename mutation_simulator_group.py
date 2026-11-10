"""
Fill in every function marked TODO. Keep the function names and
return values exactly as described so the group's parts fit together.

Randomly mutates a DNA sequence, translates the original and mutated
versions, and classifies the effect on the protein.
"""

import random

# ---------------------------------------------------------------------------
# Provided code: codon table and translator
# ---------------------------------------------------------------------------

CODON_TABLE = {
    "TTT": "Phe", "TTC": "Phe", "TTA": "Leu", "TTG": "Leu",
    "CTT": "Leu", "CTC": "Leu", "CTA": "Leu", "CTG": "Leu",
    "ATT": "Ile", "ATC": "Ile", "ATA": "Ile", "ATG": "Met",
    "GTT": "Val", "GTC": "Val", "GTA": "Val", "GTG": "Val",
    "TCT": "Ser", "TCC": "Ser", "TCA": "Ser", "TCG": "Ser",
    "CCT": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
    "ACT": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
    "GCT": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
    "TAT": "Tyr", "TAC": "Tyr", "TAA": "Stop", "TAG": "Stop",
    "CAT": "His", "CAC": "His", "CAA": "Gln", "CAG": "Gln",
    "AAT": "Asn", "AAC": "Asn", "AAA": "Lys", "AAG": "Lys",
    "GAT": "Asp", "GAC": "Asp", "GAA": "Glu", "GAG": "Glu",
    "TGT": "Cys", "TGC": "Cys", "TGA": "Stop", "TGG": "Trp",
    "CGT": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
    "AGT": "Ser", "AGC": "Ser", "AGA": "Arg", "AGG": "Arg",
    "GGT": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly",
}

BASES = "ACGT"

# A test gene: 20 codons, starts with ATG, ends with a stop codon,
# and has no stop codons in the middle.
TEST_SEQUENCE = (
    "ATGGCCTTTAAAGGCTGGCTCGAGAAACCC"
    "GGGTACCATCGTAGCGATCAAATTGTGTAG"
)


def translate(seq):
    protein = []
    for i in range(0, len(seq) - 2, 3):
        amino_acid = CODON_TABLE[seq[i:i + 3]]
        if amino_acid == "Stop":
            break
        protein.append(amino_acid)
    return protein


# ---------------------------------------------------------------------------
# Role 1: Mutator
# ---------------------------------------------------------------------------

import random
BASES = "ACGT"

def substitute(seq):
    pos = random.randrange(len(seq))
    new_base = random.choice([b for b in BASES if b != seq[pos]])
    return seq[:pos] + new_base + seq[pos + 1:], pos


def insert(seq):
    pos = random.randrange(len(seq) + 1)
    new_base = random.choice(BASES)
    return seq[:pos] + new_base + seq[pos:], pos


def delete(seq):
    pos = random.randrange(len(seq))
    return seq[:pos] + seq[pos + 1:], pos

def random_mutation(seq):
    kind, func = random.choice([
        ("substitution", substitute),
        ("insertion", insert),
        ("deletion", delete)
    ])
    new_seq, pos = func(seq)
    return new_seq, kind, pos

print(random_mutation(TEST_SEQUENCE))

# ---------------------------------------------------------------------------
# Role 2: Classifier
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
# ---------------------------------------------------------------------------
# Role 3: Simulator
# ---------------------------------------------------------------------------

def run_simulation(seq, trials, mode="any"):
    counts = {"silent": 0, "missense": 0, "nonsense": 0, "frameshift": 0}
    original_protein = translate(seq)

    for _ in range(trials):
        if mode == "substitution":
            mutated_seq, _position = substitute(seq)
            kind = "substitution"

        else:
            mutated_seq, kind, _position = random_mutation(seq)

    mutated_protein = translate(mutated_seq)

    effect = classify(original_protein, mutated_protein, kind)
    counts[effect] += 1

    return counts

# ---------------------------------------------------------------------------
# Role 4: Reporter
# ---------------------------------------------------------------------------

def print_report(counts):
    """Print each category with its count and its percentage of all trials."""
    total_trials = sum(counts.values())
    print(f"{'Effect Category':<15} | {'Count':<8} | {'Percentage':<10}")

    for category, count in counts.items():
        percentage = (count / total_trials) * 100 if total_trials > 0 else 0
        print(f"{category.capitalize():<15} | {count:<8} | {percentage:6.2f}%")

    print(f"{'Total Trials':<15} | {total_trials:<8} | 100.00%\n")


def plot_results(counts, title="Effects of random mutations"):
    """Draw a bar chart of the counts."""
    import matplotlib.pyplot as plt

    plt.bar(list(counts.keys()), list(counts.values()))
    plt.title(title)
    plt.xlabel("Effect on protein")
    plt.ylabel("Number of mutations")
    plt.show()


def demo_one_mutation(seq):
    """Show one mutation step by step: original DNA and protein, the mutation,
    mutated DNA and protein, and the classification."""
    orig_protein = translate(seq)

    print("=== Demo: Single Mutation Step ===")
    print(f"Original DNA:     {seq}")
    print(f"Original Protein: {orig_protein}")
    print("-" * 50)

    new_seq, kind, pos = random_mutation(seq)
    mut_protein = translate(new_seq)
    result = classify(orig_protein, mut_protein, kind)

    print(f"Mutation Type:    {kind.capitalize()} at position {pos}")
    print(f"Mutated DNA:      {new_seq}")
    print(f"Mutated Protein:  {mut_protein}")
    print(f"Classification:   {result.upper()}")
    print("=" * 50 + "\n")
# ---------------------------------------------------------------------------
# Quick tests - uncomment these as your functions are ready
# ---------------------------------------------------------------------------

# print(translate("ATGGCCTTTAAATAG"))       # ['Met', 'Ala', 'Phe', 'Lys']
# print(substitute("ATGGCC"))               # e.g. ('ATGACC', 3)
# print(classify(["Met", "Ala"], ["Met", "Ala"], "substitution"))  # silent
# print(classify(["Met", "Ala"], ["Met", "Asp"], "substitution"))  # missense
# print(classify(["Met", "Ala"], ["Met"], "substitution"))         # nonsense
# print(classify(["Met", "Ala"], ["Met", "Cys"], "insertion"))     # frameshift

# ---------------------------------------------------------------------------
# Main program - run this once everything is connected
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    demo_one_mutation(TEST_SEQUENCE)

    print("=== Substitutions only ===")
    sub_counts = run_simulation(TEST_SEQUENCE, 1000, mode="substitution")
    print_report(sub_counts)

    print("=== All mutation types ===")
    all_counts = run_simulation(TEST_SEQUENCE, 1000, mode="any")
    print_report(all_counts)

    plot_results(sub_counts, "Effects of 1,000 random substitutions")