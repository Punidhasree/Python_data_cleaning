import re

with open("preproinsulin-seq.txt") as f:
    data = f.read()

# remove ORIGIN, //, numbers, spaces, and newlines
clean_seq = re.sub(r'[0-9\s/ORIGIN]+', '', data, flags=re.IGNORECASE)

with open("preproinsulin-seq-clean.txt", "w") as f:
    f.write(clean_seq)

print(clean_seq)

