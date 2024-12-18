
#    BACBABABAABCBAB
#     ABABACA



def compute_prefix_function(P):
    m = len(P)  # Length of the pattern
    pi = [0] * m  # Initialize the prefix function array
    
    k = 0  # Length of the previous longest prefix suffix
    
    # Loop through the pattern from index 1 to m-1
    for q in range(1, m):
        while k > 0 and P[k] != P[q]:
            k = pi[k - 1]  # Use the prefix function to avoid unnecessary comparisons
            
        if P[k] == P[q]:
            k += 1
        
        pi[q] = k  # Set the prefix function value for the current index
    
    return pi

def kmp_string_matcher(T, P):
    n = len(T)  # Length of text
    m = len(P)  # Length of pattern
    pi = compute_prefix_function(P)  # Get the prefix function for the pattern
    
    q = 0  # Number of characters matched so far
    match_found = False  # Flag to track if a match is found
    
    # Search for the pattern in the text
    for i in range(n):
        while q > 0 and P[q] != T[i]:
            q = pi[q - 1]  # Use the prefix function to skip characters
        
        if P[q] == T[i]:
            q += 1
        
        # If we have matched all characters of the pattern, print the position
        if q == m:
            print(f"Pattern occurs at shift {i - m + 1}")
            q = pi[q - 1]  # Reset q to the value from the prefix function
            match_found = True
    
    # If no match was found, print that the pattern was not found
    if not match_found:
        print("Pattern not found in the text")

if __name__ == "__main__":
    text = input("Enter the text: ")
    pattern = input("Enter the pattern to search: ")
    print("\nSearching for the pattern...")
    kmp_string_matcher(text, pattern)
