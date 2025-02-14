import time
import matplotlib.pyplot as plt
from mpi4py import MPI
import pandas as pd

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def read_proteins(filename):
    """Read a CSV chunk based on MPI rank and return (protein_id, sequence) list."""
    with open(filename, 'rb') as file:
        num_lines = sum(1 for line in file) - 1
    # Divide lines among processes
    chunk_size = num_lines // size
    # Last rank reads the remainder number of processes
    if rank == size - 1:
        remainder = num_lines % size
        chunk = pd.read_csv(filename, skiprows=chunk_size * rank, nrows=chunk_size + remainder)
    # Each rank reads its appropriate chunk
    else:
        chunk = pd.read_csv(filename, skiprows=chunk_size * rank, nrows=chunk_size)
    return list(zip(chunk.iloc[:, 0], chunk.iloc[:, 1]))

def search_pattern(proteins, pattern):
    """Count pattern occurrences in protein sequences and return list of (protein_id, count)."""
    occurrences = []
    for protein_id, sequence in proteins:
        count = sequence.count(pattern)
        if count > 0:
            occurrences.append((protein_id, count))
    return occurrences

def plot_top_occurrences(occurrences):
    """Plot bar chart of top 10 proteins."""
    top_occurrences = sorted(occurrences, key=lambda x: x[1], reverse=True)[:10]
    protein_ids, counts = zip(*top_occurrences)
    protein_ids = [str(pid) for pid in protein_ids]
    print("Protein ID with max occurrences:", top_occurrences[0][0])
    plt.bar(protein_ids, counts)
    plt.xlabel('Protein ID')
    plt.ylabel('Occurrences')
    plt.title('Top 10 Pattern Matches')
    plt.xticks(rotation=45)
    plt.show()

def main():
    # Root process gets pattern input
    if rank == 0:
        pattern = input("Enter the pattern to search for: ").strip().upper()
    else:
        pattern = None
    # Broadcast pattern to all processes
    pattern = comm.bcast(pattern, root=0)

    if rank == 0:
        start_time = time.time()
    filename = 'proteins.csv'
    # Each process reads its appropriate chunk based on read_proteins
    proteins = read_proteins(filename)
    # Find pattern matches and counts
    occurrences = search_pattern(proteins, pattern)
    # Get local top 10 occurences to reduce data being gathered
    local_top = sorted(occurrences, key=lambda x: x[1], reverse=True)[:10]
    # Gather top occurences in root
    total_occurrences = comm.gather(local_top, root=0)

    if rank == 0:
        total_occurrences = [item for sublist in total_occurrences for item in sublist] # Flatten list
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.2f} seconds")
        if total_occurrences:
            plot_top_occurrences(total_occurrences)
        else:
            print("No occurrences found.")

if __name__ == '__main__':
    main()
