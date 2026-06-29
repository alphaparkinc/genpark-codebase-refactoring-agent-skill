import sys
import json
from refactoring_agent import CodebaseRefactoringClient

def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
        
    print("=== Codebase Refactoring Agent Example ===")
    client = CodebaseRefactoringClient()
    
    dirty_code = (
        "from math import *\n"
        "def compute_area(r):\n"
        "    return pi * r * r\n"
    )
    
    rules = ["Avoid wildcard imports", "Add docstrings to functions"]
    
    result = client.audit_and_refactor("geometry.py", dirty_code, rules)
    print("\n--- Lint Issues Detected ---")
    print(json.dumps(result["issues_detected"], indent=2))
    
    print("\n--- Refactored Code Proposal ---")
    print(result["refactored_content"])

if __name__ == "__main__":
    main()
