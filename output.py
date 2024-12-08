import csv

def save_results_to_csv(results, filename='log_analysis_results.csv'):
   
    try:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)

           
            writer.writerow(['IP Address', 'Request Count'])
            if results['ip_counts']:
                writer.writerows(results['ip_counts'])

            
            writer.writerow([])
            writer.writerow(['Most Accessed Endpoint', 'Access Count'])
            if results['most_accessed']:
                writer.writerow(results['most_accessed'])

            
            writer.writerow([])
            writer.writerow(['IP Address', 'Failed Login Count'])
            if results['suspicious_activity']:
                writer.writerows(results['suspicious_activity'])

    except Exception as e:
        print(f"Error writing to CSV: {e}")

def display_results(results):
    
    print("\nRequests per IP Address:")
    for ip, count in results['ip_counts']:
        print(f"{ip:20} {count}")

    print("\nMost Frequently Accessed Endpoint:")
    print(f"{results['most_accessed'][0]} (Accessed {results['most_accessed'][1]} times)")

    print("\nSuspicious Activity Detected:")
    for ip, count in results['suspicious_activity']:
        print(f"{ip:20} {count}")
