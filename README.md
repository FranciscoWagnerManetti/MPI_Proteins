# Protein Matching in Python using MPI
- This project highlights a program that matches specific patterns found in a protein sequence (proteins.csv)
- It compares the performance of the matching algorithm using a serial (serial-proteins.py) and a parallel version (mpi-proteins.py) of the program
- Through parallelism using MPI there was an observed speedup of 1.69 (Gustafson's law)

Below is a sample output using a proteins.csv file with 500,000 lines:
<br><img src="https://github.com/user-attachments/assets/1233db56-1ce6-4035-81bc-f6aa30cf75af" width="600">
<br><img src="https://github.com/user-attachments/assets/a2a7eb5b-9cfa-4dcb-aed3-c13025483c43" width="300">
<br>The x-axis shows the id of the protein sequence and y-axis shows the number of occurences of the pattern (in this case "ccb") in the protein sequence.

You can find more information in the Report.
