import re

# Input and output file names
input_file = "input.txt"
output_file = "emails.txt"

# Read content from input file
with open(input_file, "r") as file:
    content = file.read()

# Regular expression for email extraction
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", content)

# Save extracted emails
with open(output_file, "w") as file:
    for email in emails:
        file.write(email + "\n")

print("Email extraction completed!")
print(f"Total emails found: {len(emails)}")
print(f"Saved to: {output_file}")