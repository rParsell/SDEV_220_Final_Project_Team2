import pandas as pd

# Load employee data
employees = pd.read_csv('fake_employee_data.csv')

# Constants
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# Function to convert time range like '0800 - 1700' to number of hours
def calculate_shift_hours(military_range: str) -> float:
    if pd.isna(military_range) or '-' not in military_range:
        return 0.0
    military_range = military_range.replace(" ", "")
    split_range = military_range.split('-')

    start_str = split_range[0]
    end_str = split_range[1]

    start_hour = int(start_str[:2])
    start_min = int(start_str[2:])
    end_hour = int(end_str[:2])
    end_min = int(end_str[2:])

    start_time = start_hour + start_min / 60
    end_time = end_hour + end_min / 60

    hours = end_time - start_time
    if hours < 0:
        hours += 24  # Handle overnight shifts

    return round(hours, 2)-1

# Function to build the pivoted weekly schedule
def build_pivoted_schedule(employees_df):
    schedule_rows = []

    for _, row in employees_df.iterrows():
        emp_name = row['Employee']
        hours_shift = row['Hours']
        shift = row['Shift']
        dept = row['Department']
        day_off = row['Day Off']
        pt_ft = row['PT or FT']
        days_available = int(row['Number of Days available to work'])
        shift_duration = calculate_shift_hours(str(row['Hours']))

        # Create base row
        schedule_entry = {
            'Employee': emp_name,
            'Department': dept,
            'Shift': shift,
            'PT or FT': pt_ft,
        }

        # Fill in working hours for each day
        workdays = [day for day in days if day != day_off][:days_available]
        for day in days:
            schedule_entry[day] = hours_shift if day in workdays else 0.0

        schedule_rows.append(schedule_entry)

    return pd.DataFrame(schedule_rows)

# Generate and save the pivoted schedule
pivoted_schedule = build_pivoted_schedule(employees)
pivoted_schedule.to_csv('pivoted_weekly_schedule.csv', index=False)
print(pivoted_schedule.head())
schedule_to_work_with = pd.read_csv('pivoted_weekly_schedule.csv')