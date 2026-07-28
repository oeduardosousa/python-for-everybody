# Email Analyzer

This project is a simple Python script that analyzes an email address entered by the user.

## What it does

The program:
- asks the user to enter an email address
- displays the full email
- shows the total number of characters
- prints the email in uppercase and lowercase
- extracts and displays the user name, domain, and provider

## Example

If the user enters:

```text
student@example.com
```

The program will show information such as:
- the full email address
- the username: `student`
- the domain: `example.com`
- the provider: `example`

## How to run

Run the script with Python:

```bash
python email_analyzer.py
```

## Notes

This is a beginner-friendly exercise that demonstrates:
- string input and output
- string slicing
- string methods such as `upper()`, `lower()`, and `capitalize()`
- finding positions in a string with `find()`