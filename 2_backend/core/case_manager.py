"""
case_manager.py

CRUD operations for case files in the AI CaseFiles system.
"""

class CaseManager:
    def __init__(self):
        self.cases = {}

    def create_case(self, case_id, case_data):
        if case_id in self.cases:
            raise ValueError("Case ID already exists.")
        self.cases[case_id] = case_data
        return True

    def read_case(self, case_id):
        return self.cases.get(case_id, None)

    def update_case(self, case_id, updated_data):
        if case_id not in self.cases:
            raise ValueError("Case ID does not exist.")
        self.cases[case_id].update(updated_data)
        return True

    def delete_case(self, case_id):
        if case_id in self.cases:
            del self.cases[case_id]
            return True
        return False
