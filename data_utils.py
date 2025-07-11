def flatten_list(nested_list):
    """Flatten a nested list."""
    return [item for sublist in nested_list for item in sublist]

def chunk_list(lst, size):
    """Chunk a list into smaller lists of given size."""
    return [lst[i:i+size] for i in range(0, len(lst), size)]

def unique_elements(lst):
    """Return unique elements from list."""
    return list(set(lst))
