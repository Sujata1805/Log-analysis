from collections import Counter

def count_requests_per_ip(log_data):
    
    return Counter(entry['ip'] for entry in log_data).most_common()

def find_most_accessed_endpoint(log_data):
    
    endpoint_counts = Counter(entry['endpoint'] for entry in log_data)
    most_accessed = endpoint_counts.most_common(1)
    if most_accessed:
        return most_accessed[0]
    else:
        return None

def detect_suspicious_activity(log_entries, threshold=10):
    failed_attempts = {}

    for entry in log_entries:
        ip = entry['ip']
        status_code = entry['status']
        message = entry.get('message', '') 

        if status_code == '401' or "Invalid credentials" in message:
            if ip not in failed_attempts:
                failed_attempts[ip] = 0
            failed_attempts[ip] += 1

    print("DEBUG: Failed Attempts Dictionary:", failed_attempts)  

    suspicious_ips = [(ip, count) for ip, count in failed_attempts.items() if count > threshold]
    print("DEBUG: Suspicious IPs Detected:", suspicious_ips)  

    return suspicious_ips
