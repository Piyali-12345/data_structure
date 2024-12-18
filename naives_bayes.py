

# #   ABABDABACDABABCABAB  stirng
# #     ABAB     pattern




def naive_string_matcher(T, P):
    n = len(T)  # Length of text
    m = len(P)  # Length of pattern
    
    # Iterate through every position where the pattern could fit in the text
    found = False  # Flag to check if pattern is found at least once
    for s in range(n - m + 1):
        j = 0
        while j < m:
            if T[s + j] != P[j]:  # If characters don't match, break the loop
                break
            j += 1
        
        # If we have matched all characters of the pattern, print the position
        if j == m:
            print(f"Pattern occurs at shift {s}")
            found = True
    
    if not found:
        print("Pattern not found")

if __name__ == "__main__":
    text = input("Enter the text: ")
    pattern = input("Enter the pattern to search: ")
    print("\nSearching for the pattern...")
    naive_string_matcher(text, pattern)
