import time
import matplotlib.pyplot as plt
import pandas as pd

def read_proteins(filename):
    """Read the entire CSV file containing protein sequences and return (protein_id, sequence) list."""
    chunk = pd.read_csv(filename)
    proteins = list(zip(chunk.iloc[:, 0], chunk.iloc[:, 1]))
    return proteins

def search_pattern(proteins, pattern):
    """Find occurrences of a pattern in each protein sequence and return (protein_id, count) list."""
    occurrences = []
    for protein_id, sequence in proteins:
        count = sequence.count(pattern)
        if count > 0:
            occurrences.append((protein_id, count))
    return occurrences

def plot_top_occurrences(occurrences):
    """Plot bar chart of top 10 proteins with the most pattern matches."""
    top_occurrences = sorted(occurrences, key=lambda x: x[1], reverse=True)[:10]
    max_occurrence_protein = top_occurrences[0]
    protein_ids, counts = zip(*top_occurrences)
    protein_ids = [format(id, 'd') for id in protein_ids]
    print("Protein ID with maximum occurrences:", max_occurrence_protein[0])
    plt.bar(protein_ids, counts)
    plt.xlabel('Protein ID')
    plt.ylabel('Number of Occurrences')
    plt.title('Top 10 Proteins with Most Pattern Matches')
    plt.xticks(rotation=45)
    plt.show()

def main():
    """Main function to execute the pattern search."""
    pattern = input("Enter the pattern to search for: ").strip().upper()
    start_time = time.time()
    filename = 'proteins.csv'
    proteins = read_proteins(filename)
    occurrences = search_pattern(proteins, pattern)
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.2f} seconds")
    if occurrences:
        plot_top_occurrences(occurrences)
    else:
        print("No occurrences found.")

if __name__ == '__main__':
    main()