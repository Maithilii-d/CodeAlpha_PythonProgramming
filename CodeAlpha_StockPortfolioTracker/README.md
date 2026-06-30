# Stock Portfolio Tracker

## Description
This is a simple Stock Portfolio Tracker developed in Python as part of the CodeAlpha Python Programming Internship. The program allows users to enter stock symbols and quantities, calculates the total investment value using predefined stock prices, and optionally saves the portfolio report as TXT and CSV files.

## Features
- Accepts stock symbols and quantities from the user
- Calculates individual and total investment values
- Uses a predefined dictionary for stock prices
- Saves the portfolio report as TXT and CSV files
- Displays a portfolio summary

## Technologies Used
- Python

## Concepts Used
- Dictionary
- Loops
- Input/Output
- Basic Arithmetic
- File Handling
- CSV Module

## Sample Output

```
==================================================
            STOCK PORTFOLIO TRACKER
==================================================

Enter Stock Symbol (Example: AAPL): AAPL
Enter Quantity: 5
Add another stock? (y/n): y

Enter Stock Symbol (Example: TSLA): TSLA
Enter Quantity: 3
Add another stock? (y/n): n

==================================================
PORTFOLIO SUMMARY
==================================================
AAPL       Qty: 5     Price: $180      Value: $900
TSLA       Qty: 3     Price: $250      Value: $750
==================================================
TOTAL INVESTMENT VALUE = $1650
==================================================

Do you want to save the portfolio? (y/n): y

Portfolio saved successfully!
Files Created:
1. portfolio.txt
2. portfolio.csv

Thank you for using Stock Portfolio Tracker!
```
