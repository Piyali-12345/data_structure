NO_OF_CHARS = 256 

def badCharHeuristic(string, size):
    badChar = [-1] * NO_OF_CHARS
    for i in range(size):
        badChar[ord(string[i])] = i
    return badChar
 
def search(txt, pat):
    m = len(pat)
    n = len(txt)
    badChar = badCharHeuristic(pat, m)
    s = 0
    found = False  # To track if the pattern is found
    
    while s <= n - m:
        j = m - 1
        while j >= 0 and pat[j] == txt[s + j]:
            j -= 1
        if j < 0:
            print(f"Pattern occurs at shift = {s}")
            found = True
            s += (m - badChar[ord(txt[s + m])] if s + m < n else 1)
        else:
            s += max(1, j - badChar[ord(txt[s + j])])
    
    if not found:
        print("Pattern not found in the text.")

def main():
    txt = input("Enter the text: ")
    pat = input("Enter the pattern to search: ")
    search(txt, pat)

if __name__ == '__main__':
    main()





# output 1
# #Enter the text: this is test text
# Enter the pattern to search: test
# Pattern occurs at shift = 8

#output2
# Enter the text: this is test text
# Enter the pattern to search: tent
# Pattern not found in the text.