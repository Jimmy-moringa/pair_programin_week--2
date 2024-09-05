def generate_report():
    try:
        with open("log.text", "r") as log_file:
            entries = log_file.readlines()


        if len(entries) == 0:
            print("No log entries found.")
            return
        
        print(f"Total number of thr entries: {len(entries)}\n")
        print(f"{'Timestamp':<20} | Description")
        print('-'* 50)

        for entry in entries:
            timestamp, description = entry.split('- ')
            print(f"{timestamp:<20} | {description.strip()}")

    except FileNotFoundError:
        print("Log.txt  file not found. Make sure the file exists.")


if __name__ == "__main__":
    command = input("Enter 'report' to generate the report:").strip().lower()
    if command == 'report':
        generate_report