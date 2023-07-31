def best_score(a_dictionary):
    if not a_dictionary:
        return None

    best_key = max(a_dictionary, key=a_dictionary.get)
    return best_key

# Test the function
'''scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95}
result = best_score(scores)
print(result)  # Output: 'David' '''
