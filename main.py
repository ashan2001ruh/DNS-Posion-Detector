from src.detector import detect_dns_poisoning
from src.reporter import generate_report

def main():
    print("Starting DNS Poisoning Detection...")
    suspicious_responses = detect_dns_poisoning()
    if suspicious_responses:
        print(f"Detected {len(suspicious_responses)} suspicious DNS responses.")
        generate_report(suspicious_responses)
    else:
        print("No suspicious DNS responses detected.")

if __name__ == "__main__":
    main()