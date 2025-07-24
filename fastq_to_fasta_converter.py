# fastq_to_fasta_converter.py

input_file = "X.txt"  # Replace with your actual filename if different
output_file = "X.fasta"

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for idx, line in enumerate(infile):
        parts = line.strip().split()
        if len(parts) == 3:
            filename, sequence, count = parts
            header = f">seq{idx+1}_count{count}"
            outfile.write(f"{header}\n{sequence}\n")

print(f"Conversion complete! FASTA file saved as: {output_file}")
