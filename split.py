# Read the cleaned sequence
with open("preproinsulin-seq-clean.txt") as f:
    seq = f.read().strip()

# Save LSinsulin (1–24)
with open("lsinsulin-seq-clean.txt", "w") as f:
    f.write(seq[0:24])

# Save Binsulin (25–54)
with open("binsulin-seq-clean.txt", "w") as f:
    f.write(seq[24:54])

# Save Cinsulin (55–89)
with open("cinsulin-seq-clean.txt", "w") as f:
    f.write(seq[54:89])

# Save Ainsulin (90–110)
with open("ainsulin-seq-clean.txt", "w") as f:
    f.write(seq[89:])
