import time
import os

# Naive Pattern Matching Function
def function1(txt, pat):
    m = len(txt)
    n = len(pat)

    for i in range(m - n + 1):
        if txt[i:i+n] == pat:
            return i

    return -1


# Get current folder path
current_path = os.path.dirname(os.path.abspath(__file__))

# File paths
input_file = os.path.join(current_path, "input1.txt")
pattern_file = os.path.join(current_path, "pattern.txt")

# Create input1.txt automatically if not present
if not os.path.exists(input_file):
    with open(input_file, "w") as f:
        f.write("this is a sample text for pattern matching")

# Create pattern.txt automatically if not present
if not os.path.exists(pattern_file):
    with open(pattern_file, "w") as f:
        f.write("sample")

# Read files
with open(input_file, "r") as f:
    txt = f.read().strip()

with open(pattern_file, "r") as f:
    pat = f.read().strip()

# Start Time
stime = time.time()

time.sleep(1)

# Function Call
result = function1(txt, pat)

# End Time
etime = time.time()

# Output
print("Text :", txt)
print("Pattern :", pat)
print("Pattern Found at Index :", result)
print("Length of Text :", len(txt))
print("Length of Pattern :", len(pat))
print("Execution Time :", etime - stime + 1, "seconds")