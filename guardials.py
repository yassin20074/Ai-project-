import re

# class is responsiple for protecting the ai agent from malicios attempts
class AISecurityManager:
    # method definition
    def init(self):
#a list of suspicios text patterns
        self.malicious_patterns = [
            r"(?i)ignore documents", r"(?i)system override",
            r"(?i)delete all", r"(?i)sudo", r"(?i)hack"
        ]
#check the validity of any request submitted by the user
    def scan_query(self, query: str):
        for pattern in self.malicious_patterns:
            if re.search(pattern, query):
                return False, "⚠️ Pattern-based Injection Detected"
        if len(query) > 500:
            return False, "⚠️ Query too long (Potential Buffer/DoS)"
        return True, "Safe"
# protects against any information leaks
    def sanitize_output(self, output: str):
        hidden_pattern = r"(sk-[a-zA-Z0-9]{20,})"
        return re.sub(hidden_pattern, "[REDACTED]", output)