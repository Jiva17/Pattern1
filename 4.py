import time

def rabin_karp(text, pattern, d=256, q=101):  # d = number of characters in input alphabet, q = a prime number
    n = len(text)
    m = len(pattern)
    if m == 0:
        return list(range(n + 1))
    h = pow(d, m-1) % q  # value of d^(m-1)
    p = 0  # hash value for pattern
    t = 0  # hash value for text
    result = []

    # Preprocessing: calculate hash value for pattern and first window of text
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    # Slide the pattern over text one by one
    for s in range(n - m + 1):
        if p == t:
            # Check for characters one by one (spurious hits are possible)
            if text[s:s+m] == pattern:
                result.append(s)
        
        if s < n - m:
            t = (d * (t - ord(text[s]) * h) + ord(text[s + m])) % q
            if t < 0:
                t += q

    return result

# ----------- DEMO -----------
if __name__ == "__main__":
    sample_text = (
        "this is a simple example to demonstrate rabin karp algorithm. "
        "rabin karp is a string searching algorithm that uses hashing."
    )
    pattern = "rabin karp"
    start = time.time()
    matches = rabin_karp(sample_text, pattern)
    elapsed = time.time() - start

    if matches:
        print(f"Pattern found at positions: {matches}")
    else:
        print("Pattern not found.")

    print(f"Search took {elapsed:.6f} seconds.")