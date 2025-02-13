# Uses python3
import sys

def edit_distance(s, t):
   
    columns_count = len(s) + 1
    rows_count = len(t) + 1
    match = 0
    mu = 1
    sigma = 1

    D = []
    D.append([c for c in range(columns_count)])
        
    for r in range(1, rows_count, 1):
        D.append([(r if c == 0 else 0) for c in range(columns_count)])

    for r in range(1, rows_count, 1):
        for c in range(1, columns_count, 1):
            match_or_substitution = D[r - 1][c - 1] + (match if s[c - 1] == t[r - 1] else mu)
            deletion = D[r][c-1] + sigma
            insertion = D[r-1][c] + sigma
            D[r][c] = min(match_or_substitution, deletion, insertion)

    return D[len(t)][len(s)]

if __name__ == "__main__":

    print(edit_distance(input(), input()))