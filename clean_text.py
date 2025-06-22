import nltk
from nltk.corpus import stopwords
import re

# Download stopwords if not already downloaded
nltk.download('stopwords')

# Load stopwords
stop_words = set(stopwords.words('english'))

# Define the clean_text function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    text = ''.join(c for c in text if c.isalnum() or c.isspace())
    tokens = text.split()
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(filtered_tokens)

# Collect multiple bug reports
cleaned_reports = []
print("Enter your bug reports one at a time. Type 'done' when finished:\n")

while True:
    report = input("Bug report: ")
    if report.lower() == "done":
        break
    cleaned = clean_text(report)
    cleaned_reports.append(cleaned)

# Display all cleaned results
print("\n🧼 Cleaned Bug Reports:")
for i, cleaned in enumerate(cleaned_reports, start=1):
    print(f"{i}. {cleaned}")
