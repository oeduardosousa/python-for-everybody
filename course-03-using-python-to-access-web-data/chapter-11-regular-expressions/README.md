# Chapter 11 — Regular Expressions

This chapter introduces regular expressions in Python. Regular expressions are a powerful tool for finding and extracting text patterns from strings and files.

## What is included

- `log_analyzer.py` — a script that reads a log file, extracts values with regular expressions, counts log levels, and identifies the most frequent user.
- `server_log.txt` — sample log data used by the script if no filename is provided.

## What you will learn

- How to use `re.findall()` to extract data from text
- How to detect and count patterns such as `ID:<number>` and `User: <name>`
- How to keep counts using Python dictionaries
- How to read files line by line and process each line safely

## How to run the script

1. Open a terminal in this chapter folder.
2. Run:
   ```bash
   python log_analyzer.py
   ```
3. When asked for a file name, press Enter to use `server_log.txt` or type a different filename.

## Expected output

The script prints:

- total number of lines processed
- sum of the extracted IDs
- counts for `INFO`, `WARNING`, and `ERROR` log entries
- the most frequent user seen in the log

## Notes

- The script uses a beginner-friendly Python style with dictionaries and simple loops.
- Regular expressions are used only where needed to extract IDs and usernames.
- If the file cannot be found, the script prints an error message and exits.
