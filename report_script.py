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
        