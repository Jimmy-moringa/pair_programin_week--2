from datetime import datetime 

def append_to_log(description):
    with open('log.txt', 'a') as log_file:
        timestamp = datetime.no().strftime('%Y-%m-%d %H:%M:%S')
        log_file.write(f'{timestamp} - {description}\n')
    print("log entry added.")

if __name__ == '__main__':
    description = input("Entry log description: ")
    append_to_log(description)