Log Script and Utilities
This repository contains a Python script with utilities for logging, searching, and manipulating text. The script includes functions for logging with timestamps, searching for literal strings, finding emails and dates, replacing words, and generating a log report.

Requirements
Python 3.10 or higher
No additional dependencies
Script Overview
Functions
append_to_log(description)

Description: Appends a log entry with a timestamp to log.txt.
Parameters:
description (str): The log entry description.
Usage:
append_to_log("Sample log entry.")
search_literal_string(text, word)

Description: Searches for a literal string in the provided text.
Parameters:
text (str): The text to search in.
word (str): The word to search for.
Usage:
search_literal_string("The quick brown fox jumps over the lazy dog.", "fox")
find_emails(text)

Description: Finds and prints all email addresses in the provided text.
Parameters:
text (str): The text to search for email addresses.
Usage:
find_emails("Contact us at example@example.com.")
find_dates(text)

Description: Finds and prints all dates in the format MM/DD/YYYY in the provided text.
Parameters:
text (str): The text to search for dates.
Usage:
find_dates("The event is scheduled for 12/09/2024.")
replace_word(text, old_word, new_word)

Description: Replaces occurrences of a word in the text with a new word.
Parameters:
text (str): The text where replacements will be made.
old_word (str): The word to be replaced.
new_word (str): The word to replace with.
Usage:
updated_text = replace_word("Replace the old word.", "old", "new")
generate_report()

Description: Generates and prints a report from the log file log.txt.
Usage:
generate_report()
Usage
Running the Script:

To use the script, simply run the Python file:
python log_script.py
Adding Log Entries:

When prompted, enter a description for the log entry. The entry will be appended to log.txt with a timestamp.
Generating a Report:

Enter report when prompted to generate and print a report of log entries.
Example Execution:

Enter 'report' to generate the report: report