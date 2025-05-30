"""
chain_of_custody.py

Blockchain/RFID evidence tracker for AI CaseFiles system.
"""

class ChainOfCustodyTracker:
    def __init__(self):
        self.evidence_log = []

    def log_evidence(self, evidence_id, location, handler, timestamp):
        entry = {
            "evidence_id": evidence_id,
            "location": location,
            "handler": handler,
            "timestamp": timestamp
        }
        self.evidence_log.append(entry)
        # In a real implementation, this would be recorded on a blockchain or secure ledger
        return True

    def get_evidence_log(self, evidence_id):
        return [entry for entry in self.evidence_log if entry["evidence_id"] == evidence_id]
