"""
name_matching.py

Fuzzy name and alias detection for AI CaseFiles system.
"""

from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def is_name_match(name1, name2, threshold=0.8):
    similarity = similar(name1.lower(), name2.lower())
    return similarity >= threshold

if __name__ == "__main__":
    # Example usage
    name_a = "John Doe"
    name_b = "Jon Doe"
    print(f"Names match: {is_name_match(name_a, name_b)}")
