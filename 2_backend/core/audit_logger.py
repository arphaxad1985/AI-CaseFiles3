"""
audit_logger.py

Immutable activity records logger for AI CaseFiles system.
"""

import hashlib
import time

class AuditLogger:
    def __init__(self):
        self.records = []
        self.last_hash = None

    def log_activity(self, activity):
        timestamp = time.time()
        record = {
            "activity": activity,
            "timestamp": timestamp,
            "prev_hash": self.last_hash
        }
        record_str = f"{activity}{timestamp}{self.last_hash}"
        record_hash = hashlib.sha256(record_str.encode()).hexdigest()
        record["hash"] = record_hash
        self.records.append(record)
        self.last_hash = record_hash
        return record_hash

    def get_records(self):
        return self.records
