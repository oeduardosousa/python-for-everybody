# Grades Analyzer

A Python program that reads a file of student grades and calculates basic statistics such as the total number of students, average score, highest score, lowest score, and how many students passed or failed.

## Project Description

This project was created while studying the "Files" chapter of the Python for Everybody specialization. It demonstrates how to read data from a text file, process each line, and calculate useful results from the information stored in the file.

## Concepts Practiced

- reading files in Python
- using loops to process file contents
- splitting strings into parts
- converting strings to integers
- tracking statistics with variables
- identifying the students with the highest and lowest scores

## How It Works

The program reads a file named `grades.txt` where each line contains a student name and a score separated by a comma. It then:

- counts the total number of students
- calculates the average score
- finds the highest and lowest scores
- identifies the student associated with each of those scores
- counts how many students passed and failed

A passing score is considered to be 60 or higher.

## How to Run

Run the script with Python:

```bash
python grades_analyzer.py
```

## Example

If the file contains lines like:

```text
Alice,85
Bob,72
Carla,55
```

The program will print the summary statistics for those grades, including the student with the highest score and the student with the lowest score.