# Protein Matching in Python using MPI
- This project highlights a program that matches specific patterns found in a protein sequence (proteins.csv)
- It compares the performance of the matching algorithm using a serial (serial-proteins.py) and a parallel version (mpi-proteins.py) of the program
- Through parallelism using MPI there was an observed speedup of 1.69 (Gustafson's law)

Below is a sample output using a proteins.csv file with 500,000 lines
![image](https://github.com/user-attachments/assets/1233db56-1ce6-4035-81bc-f6aa30cf75af)
![ccb](https://github.com/user-attachments/assets/a3777e15-b715-4075-84fd-c4f860a243a0)

The x-axis shows the id of the protein sequence and y-axis shows the number of occurences of the pattern (in this case "CCB") in the protein sequence

* You can find more information in the Report
