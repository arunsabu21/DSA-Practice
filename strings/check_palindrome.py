# Function to check palindrome
def is_palindrome(text):
    # Remove spaces and convert to lowercase
    cleaned_text = text.replace(" ", "").lower()
    
    # Compare with its reverse
    return cleaned_text == cleaned_text[::-1]

# Test examples
print(is_palindrome("madam"))    
print(is_palindrome("Racecar"))  
print(is_palindrome("hello"))    
print(is_palindrome("nurses run")) 

    