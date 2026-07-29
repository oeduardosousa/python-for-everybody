# Best Selling Products

This project reads a text file containing product names and creates a simple sales report showing how many times each product appears.

## What the script does

The program:
- asks for a file name
- uses [sales.txt](sales.txt) by default if no name is provided
- counts how many times each product appears in the file
- prints the results from most sold to least sold

## Example input

If the file contains:

```text
Mouse
Keyboard
Mouse
Monitor
Keyboard
```

The program will print:

```text
Sales report by product
------------------------
Mouse: x sold
Keyboard: y sold
Monitor: z sold
```

## How to run

From this folder, run:

```bash
python best_selling_products.py
```

When prompted, enter the name of the file you want to analyze. Press Enter to use [sales.txt](sales.txt).

## File overview

- [best_selling_products.py](best_selling_products.py): main script that reads the file and generates the report
- [sales.txt](sales.txt): sample data used by the program

## Requirements

- Python 3.x