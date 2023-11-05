import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Define a regular expression pattern to match valid input formats
    pattern = r'^\d{1,2}(:[0-5][0-9])? (AM|PM) to \d{1,2}(:[0-5][0-9])? (AM|PM)$'

    # Check if the input matches the pattern
    if not re.fullmatch(pattern, s):
        raise ValueError("Invalid input format")

    # Define a function to convert a single time from 12-hour to 24-hour format
    if ':' in s:
        def convert_single_time(time):
            parts = time.split()
            hours, minutes = map(int, parts[0].split(':'))
            am_pm = parts[1]

            if am_pm == 'PM' and hours != 12:
                hours += 12
            elif am_pm == 'AM' and hours == 12:
                hours = 0

            return f'{hours:02d}:{minutes:02d}'
    if ':' not in s:
        parts = s.split()
        hour1, hour2 = int(parts[0]), int(parts[3])
        if parts[1] == 'PM' and hour1 != 12:
            hour1 = hour1 + 12
        if parts[4] == 'PM' and hour2 != 12:
            hour2 = hour2 + 12
        elif parts[1] == 'AM' and hour1 == 12:
            hour1 = 0
        return f'{hour1:02d}:00 to {hour2:02d}:00'

    # Use regular expressions to find and convert both times
    result = re.sub(r'\d{1,2}:\d{2} (AM|PM)', lambda match: convert_single_time(match.group(0)), s)

    return result

if __name__ == "__main__":
    main()