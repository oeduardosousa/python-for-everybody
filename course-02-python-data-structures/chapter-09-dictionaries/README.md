# Chapter 09 — Dictionaries: Contact Book

This folder contains a small interactive exercise that demonstrates how to store, lookup, and manage key/value pairs using Python dictionaries.

## Project Overview

`contact-book.py` is a console-based Contact Book that lets the user add, search, list, and delete contacts. Each contact is stored as a key/value pair in a dictionary where the key is the contact name and the value is the phone number.

## Features

- Add contacts by name and phone number
- Search for a contact using `dict.get()` (safe lookup)
- List all stored contacts
- Delete a contact after confirming it exists
- Simple menu-driven interface for interactive use

## How to run

From this chapter folder run:

```bash
python contact-book.py
```

Follow the numbered menu prompts to interact with the program.

## Design notes & tips

- The program stores contacts in memory only; data is lost when the program exits. To persist contacts, consider using `json` to save/load `contacts` to a file.
- Use `str.strip()` when reading names to avoid accidental whitespace keys.
- `contacts[name] = phone` inserts or updates a contact. The code uses `contacts.get(name)` for safe lookups.
- Add input validation around `int(input(...))` to handle non-numeric menu input without crashing.
- Refactor into functions (`add_contact`, `search_contact`, `show_all`, `delete_contact`, `main`) to improve readability and testability.

## Author

Eduardo Sousa