#Search Element in Array
def search_element(A, X):
    for i in A:
        if i == X:
            return "Yes"
    return "No"

# Example
A = [1, 2, 3, 4, 5]
X = 3
print(search_element(A, X))