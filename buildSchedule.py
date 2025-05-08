from ImpData import impData
from generateSchedule_program_2 import calculate_shift_hours, build_pivoted_schedule
import pandas as pd

# Load employee data
employees = pd.read_csv('fake_employee_data.csv')

# Constants
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

pivoted_schedule = build_pivoted_schedule(employees)
pivoted_schedule.to_csv('pivoted_weekly_schedule.csv', index=False)
print(pivoted_schedule.head())
schedule_to_work_with = pd.read_csv('pivoted_weekly_schedule.csv')