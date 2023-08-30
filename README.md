# ramp_up_python
rampup python code 

**rampup python code 
(3 TASKs)**

#   3 TASKS
# String Analysis Program

This is a Python program that performs analysis on a given string statement.

### Prerequisites

- Python (version 3.6 or later) installed on your system.

## How to Run

Follow the steps below to run the program and perform string analysis:

1. Clone the Repository: ** https://github.com/sarvan3527/ramp_up_python.git**

2. Navigate to the Repository Directory:

3. Run the Python Code:

4. Input a String Statement:
The program will prompt you to input a string statement. Enter the statement and press Enter.

5. View the Analysis Results:
The program will perform the following analysis on the input string:
- Total number of characters
- Total number of duplicate characters
- Total number of words
- Total number of duplicate words
- Reversed characters and words
- Statement with duplicate characters removed

6. Terminate the Program:
Once the analysis is complete, you can press `Ctrl + C` to terminate the program.


#      2nd TASK  ==============

# Email Validation Program

This is a simple Python program that validates and manages email addresses. It allows users to enter email addresses, validates them using regular expressions, and stores valid email addresses in a text file.

The regular expression used for email validation in this program is a simplified  using a regular expression pattern.

### Prerequisites
1. Make sure you have Python installed on your system.

2.Import modules what ever is required

## Instructions

3. Clone this repository to your local machine using the following command: 


4. Open a terminal or command prompt and navigate to the directory where you cloned the repository.
    ** https://github.com/sarvan3527/ramp_up_python.git**

5. Run the program by executing the following command:


6. The program will prompt you with the question "Do you want to enter an email address? (Yes/No) :" Enter your choice ("Yes" or "No").

- If you choose "No," the program will read and display the contents of the "email_txt.txt" file, which contains the list of valid email addresses.

- If you choose "Yes," the program will prompt you to enter an email address. It will then validate the email using regular expressions. If the email is valid, it will be added to the "email_txt.txt" file, and the updated list of valid email addresses will be displayed.

7. You can continue entering email addresses or exit the program by typing "No."

8. To view the list of valid email addresses stored in the "email_txt.txt" file, run the program and choose "No" when prompted.




#    3rd  TASK  ================================

  # IP Address Validation and Ping Program

This is a Python program that validates and checks the reachability of IP addresses. It allows users to enter IP addresses, validates them using regular expressions, and performs a ping operation to check if the IP is reachable.

The regular expression used for IP address validation in this program using regular pattern.

### Prerequisites

1. Make sure you have Python installed on your system.

2. Install the `ping3` library if you haven't already by running the following command:

## Instructions
3. Clone this repository to your local machine using the following command:


4. Open a terminal or command prompt and navigate to the directory where you cloned the repository.
    ** https://github.com/sarvan3527/ramp_up_python.git**

5. Run the program by executing the following command:


6. The program will prompt you with the question "Do you want to enter an ip address? (Yes/No) :" Enter your choice ("Yes" or "No").

- If you choose "No," the program will read and display the contents of the "ip_address.txt" file, which contains the results of IP address validations and ping tests.

- If you choose "Yes," the program will prompt you to enter an IP address. It will validate the IP using regular expressions. If the IP is valid, it will perform a ping operation to check its reachability. The validation and ping results will be saved in the "ip_address.txt" file.

7. You can continue entering IP addresses or exit the program by typing "No."

8. To view the results of IP address validations and ping tests stored in the "ip_address.txt" file, run the program and choose "No" when prompted.


#         4th Task      ==================

# Employee Details Generator with Threading

This Python program demonstrates the use of generators and threading to generate employee details concurrently. It generates random employee details including employee ID, location, and salary.

## Requirements

- Python 3.x

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory where the Python script is located.
3. Run the script using the following command:

4. Enter the desired number of employee details to generate.

5. The program will generate and display employee details concurrently using threading.

## Functionality

1. The `generate_employee_details` function generates employee details using a generator.
2. The generator yields employee ID, location, and salary for the specified number of employees.
3. Random values are chosen for each employee detail using the `random` module.
4. Threading is used to concurrently generate and display employee details.

#      5th Task      ============

5th Task

# Multiple Producers and Consumers using Threads

This Python program demonstrates the usage of multiple producers and consumers using threads. The program allows you to specify the number of producers and consumers, and it simulates their interactions through thread execution.

## Requirements

- Python 3.x

## How to Run

1. Open a terminal or command prompt.
2. Navigate to the directory where the Python script is located.
3. Run the script using the following command:

4. Follow the on-screen prompts to enter the number of producers and consumers.

## Example

1. Enter the number of producers you want to perform.
2. Enter the number of consumers you want to perform.

The program will then simulate producers and consumers interactions using threads and display the output accordingly.

# 6th Task      ===================

6th Task


# Shape Area Calculator

This Python program demonstrates object-oriented programming concepts using inheritance and function overriding. It calculates the areas of different geometric shapes: square, triangle, and circle.

## Requirements

- Python 3.x

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory where the Python script is located.
3. Run the script using the following command:

4. The program will calculate and display the area of a square, a triangle, and a circle based on the provided dimensions.

## Shapes and Their Areas

### Square

- To calculate the area of a square, provide the side length.
- Formula: area = side_length^2

### Triangle

- To calculate the area of a triangle, provide the base and height.
- Formula: area = 0.5 * base * height

### Circle

- To calculate the area of a circle, provide the radius.
- Formula: area = pi * radius^2


==================================================================================

30/08/2023 completed 


#		7th Task ATM		###########


ATM Withdrawal Note Calculator
The ATM Withdrawal Note Calculator is a Python program that calculates the number of currency notes required for a given withdrawal amount using various denominations. It ensures that the withdrawal amount is a multiple of 50, as ATMs typically dispense notes in multiples of 50.

How to Use
Download or copy the provided code into a Python file (e.g., atm_calculator.py).

Open a terminal or command prompt.

Navigate to the directory where the Python file is located.

Run the program by entering the following command:

Copy code
python atm_calculator.py
The program will prompt you to enter the withdrawal amount.

Enter the withdrawal amount. The program will then calculate and display the number of notes for each denomination (500, 200, 100, and 50).

If the provided withdrawal amount is not a multiple of 50, an error message will be displayed, and you will be prompted to enter a new amount.

Repeat steps 5-7 as needed.

You can exit the program by pressing Ctrl+C or closing the terminal.

Code Explanation:

The provided code defines a class ATM that encapsulates the logic for calculating and displaying the number of notes for a given withdrawal amount. The calculate_notes method performs the calculation based on various denominations (500, 200, 100, and 50). The display_notes method displays the calculated note counts.

The program uses a while loop to repeatedly prompt the user for a withdrawal amount until a valid multiple of 50 is provided. Once a valid amount is entered, the ATM class is instantiated, and the methods are called to calculate and display the note counts.



=======================================================================================================================

8th TASK


Attendance Analysis Using Pandas and Numpy

This repository contains Python code that demonstrates how to analyze attendance data from an Excel file using the Pandas and Numpy libraries. The code calculates the counts of employees working from home (WFH) and working from the office (WFO) for the current date and previous days, identifies employees who missed all days, and provides insights into attendance trends.

Requirements
Before running the code, make sure you have the following installed:

Python 3.x
Pandas
Numpy
You can install these dependencies using the following commands:

bash
Copy code
pip install pandas
pip install numpy
Usage
Clone this repository or download the provided code.

Place your Excel attendance data file (attendance.xlsx) in the same directory as the code.

Open the Python script attendance_analysis.py in your preferred code editor.

Run the script using the following command:

bash
Copy code
python attendance_analysis.py
The script will read the attendance data from the Excel file, perform calculations, and print the results in the console.
Explanation
The provided code performs the following steps:

Imports the required libraries: Pandas for data manipulation and Numpy for numerical operations.

Reads attendance data from an Excel file using the pd.read_excel function from Pandas.

Cleans up the column names by removing leading and trailing spaces.

Defines a list of date columns representing attendance dates.

Calculates the counts of WFH and WFO employees for the current date using Numpy's np.sum.

Calculates the cumulative WFH and WFO counts for the previous days using Numpy's np.sum and Pandas' .sum().

Identifies employees who missed all days by using the .isnull().all(axis=1) condition.

Prints the results including WFH and WFO counts for the current and previous days, as well as the list of employees who missed all days.

Customization:

You can customize the code according to your needs:

Update the attendance.xlsx file with your own attendance data.
Modify the dates list to match the date columns in your Excel file.
Adapt the code to different date formats or data structures as needed.


=======================================================================================================================================================

9Th TASK

Treemap Visualization Using Plotly and Pandas
This repository contains Python code that demonstrates how to create an interactive treemap visualization using the Plotly library for plotting and the Pandas library for data manipulation. The treemap visualization represents hierarchical data as nested rectangles, with the size of each rectangle representing a quantitative value.

Requirements::

Before running the code, make sure you have the following installed:

Python 3.x
Pandas
Plotly
You can install these dependencies using the following commands:

bash
Copy code
pip install pandas
pip install plotly
Usage
Clone this repository or download the provided code.

Place your Excel data file containing the necessary columns (label, index, colors) in the specified location.

Open the Python script treemap_visualization.py in your preferred code editor.

Update the data_file_path variable in the script to point to the location of your Excel data file.

Run the script using the following command:

bash
Copy code
python treemap_visualization.py
The script will read the data from the Excel file, create a treemap visualization using Plotly, and display the interactive plot in your default web browser.
Explanation
The provided code performs the following steps:

Imports necessary libraries: Pandas for data manipulation and Plotly for visualization.

Reads data from an Excel file using the pd.read_excel function from Pandas.

Defines lists of labels, values, and colors based on the columns in the Excel file.

Creates a treemap figure using go.Figure(go.Treemap(...)) from Plotly's graph objects.

Configures the labels, values, colors, text formatting, and hover information for the treemap trace.

Sets the layout of the figure to have no margins.

Displays the interactive treemap plot using the fig.show() method.

Customization:

You can customize the visualization by modifying the code:

Update the data_file_path variable to point to your Excel data file.
Modify the columns used for labels, values, and colors based on your data.











