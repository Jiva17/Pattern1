import time

def rabin_karp(text, pattern, d=256, q=101):
    n = len(text)
    m = len(pattern)

    h = pow(d, m-1) % q

    p = 0
    t = 0

    result = []

    # Calculate initial hash values
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    # Slide pattern over text
    for s in range(n - m + 1):

        # If hash values match
        if p == t:

            # Check characters one by one
            if text[s:s+m] == pattern:
                result.append(s)

        # Calculate next window hash
        if s < n - m:
            t = (d * (t - ord(text[s]) * h) + ord(text[s + m])) % q

            if t < 0:
                t += q

    return result


# Main Program
text = "AABAACAADAABAABA"
pattern = "AABA"

start = time.time()

matches = rabin_karp(text, pattern)

end = time.time()

print("Text :", text)
print("Pattern :", pattern)
print("Pattern found at indices :", matches)
print("Execution Time :", end - start, "seconds")