import pandas as pd
import numpy as np

# Read data from Excel file
data = pd.read_excel("attendance.xlsx")
data.columns = data.columns.str.strip()

# Define date columns
dates = ['aug 25 2023', 'aug 26 2023', 'aug 26 2023', 'aug 28 2023', 'aug 29 2023']

# Calculate WFH and WFO counts for today
wfh_today = np.sum(data['aug 29 2023'] == 'WFH')
wfo_today = np.sum(data['aug 29 2023'] == 'WFO')

# Calculate WFH and WFO counts for previous days
wfh_count_previous_days = np.sum(data[dates] == 'WFH').sum()
wfo_count_previous_days = np.sum(data[dates] == 'WFO').sum()

# Find employees who missed all days
missing_all_days = data[data[dates].isnull().all(axis=1)]['emp_id']
missing = missing_all_days.tolist()

# Print results
print("WFH Count on Current Date:", wfh_today)
print("WFO Count on Current Date:", wfo_today)
print("WFH Count for last 5 Days:", wfh_count_previous_days)
print("WFO Count for last 5 Days:", wfo_count_previous_days)
print("Employees who Missed All Days: ", missing)


