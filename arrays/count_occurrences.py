# Count Occurrences
def count_occurrences(A, X):
    count = 0
    for num in A:
        if num == X:
            count +=1
    return count

A = [1, 2, 3, 2, 2, 4]
print(count_occurrences(A, 2))
    
