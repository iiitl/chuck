from chuck.tasks.data_encoding.task import generate, solve

def run_example():
    payload = generate(8192, 42)
    results = solve(payload)

    print("--- Chuck Data Encoding Report ---")
    print(f"Original:   {results['input_bytes']} bytes")
    print(f"Compressed: {results['compressed_bytes']} bytes")
    print(f"Ratio:      {results['ratio']}")
    
    status = "SUCCESS" if results["roundtrip"] else "FAILED"
    print(f"Integrity Check: {status}")

if __name__ == "__main__":
    run_example()