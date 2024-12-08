from parser import parse_log_file
from analysis import count_requests_per_ip, find_most_accessed_endpoint, detect_suspicious_activity
from output import save_results_to_csv, display_results

def main():
    log_file = 'sample.log'
    output_file = 'log_analysis_results.csv'

    # Step 1: Parse the log file
    log_data = parse_log_file(log_file)
    if not log_data:
        return

    # Step 2: Perform analysis
    ip_counts = count_requests_per_ip(log_data)
    most_accessed = find_most_accessed_endpoint(log_data)
    suspicious_activity = detect_suspicious_activity(log_data)
    # print("DEBUG: Suspicious Activity Results:", suspicious_activity)

    # Step 3: Prepare results
    results = {
        'ip_counts': ip_counts,
        'most_accessed': most_accessed,
        'suspicious_activity': suspicious_activity,
    }

    # Step 4: Display and save results
    display_results(results)
    save_results_to_csv(results, output_file)
    print(f"\nResults saved to {output_file}")

if __name__ == '__main__':
    main()
