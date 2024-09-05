import re 

def search_litral_string(text, word):
    match = re.search(word, text)
    if match :
        print(f"Found '{word}' at position {match.start()}")
    else:
        print(f"'{word}' not found")


def find_emails(text):
    emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)
    print("Emails found:", emails)

def find_dates(text):
    dates = re.findall(r'(\d{2}/\d{2}/\d{4}/\d{1,2)/\d{1,2}/\{4}', text)
    print("Dates found:", dates)


def  replace_word(text, old_world, new_word):
    return re.sub(old_world, new_word, text)

sample_text = """"Hello,

I hope this email finds you well. Please note that the meeting is scheduled  for  12/09/2024, 
and you can contact us at dogsAreUs@gmail.com or infoOnDogs@helpcenter.gmail.com for any quaries. Also, remember to send your report by 8/15/2024.
You can reach out to www.alexanderkaranja@yahoo.com if you have any concerns .


Best regards,
Alexander Kaneky.
Report Coordinator.
"""

search_litral_string('The quick brown fox jumps over the lazy dog.', 'fox')
find_emails(sample_text)
find_dates(sample_text)
update_text = replace_word(sample_text, 'report', 'document')
print(update_text)