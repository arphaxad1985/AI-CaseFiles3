"""
modus_operandi.py

Pattern recognition for modus operandi (MO) in AI CaseFiles system.
"""

def detect_mo_pattern(case_descriptions, pattern):
    """
    Detect if the given pattern exists in the list of case descriptions.
    """
    matches = [desc for desc in case_descriptions if pattern.lower() in desc.lower()]
    return matches

if __name__ == "__main__":
    # Example usage
    cases = [
        "Burglary at 123 Main St with forced entry",
        "Robbery at 456 Elm St with weapon",
        "Burglary at 789 Oak St with forced entry"
    ]
    pattern = "forced entry"
    matched_cases = detect_mo_pattern(cases, pattern)
    print(f"Cases matching pattern '{pattern}': {matched_cases}")
