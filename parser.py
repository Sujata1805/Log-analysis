import re

def parse_log_file(filename):
    log_data = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                match = re.match(
                    r'(?P<ip>\d+\.\d+\.\d+\.\d+) .* "(?P<method>\w+) (?P<endpoint>\/\S*) .*" (?P<status>\d+) .*',
                    line
                )
                if match:
                    log_data.append(match.groupdict())  
        return log_data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
