"""
This module provides a usage example for the data_encoding task.
It demonstrates payload generation, compression, and integrity verification.
"""
import sys
from chuck.tasks.data_encoding.task import generate, solve

def run_example():
    """
    Generates a test payload, executes the encoding solver, 
    and verifies the round-trip integrity of the data.
    """
    payload = generate(8192, 42)
    results = solve(payload)

    print("--- Chuck Data Encoding Report ---")
    print(f"Original:   {results['input_bytes']} bytes")
    print(f"Compressed: {results['compressed_bytes']} bytes")
    print(f"Ratio:      {results['ratio']}")
    
    status = "SUCCESS" if results["roundtrip"] else "FAILED"
    print(f"Integrity Check: {status}")

    
    if not results["roundtrip"]:
        sys.exit(1)

if __name__ == "__main__":
    run_example()