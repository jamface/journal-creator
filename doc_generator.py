"""
A Markdown document template generator (Python 3.5).

Navigate to the Journal folder in Windows Explorer.
Run using 'python3 doc_generator.py <year> <month>'.
Month should be zero-padded, e.g. 02 for February.
"""
import datetime
import argparse
import sys
import os

parser = argparse.ArgumentParser(description='Create a Journal template file.')
parser.add_argument('year')
parser.add_argument('month')


VALID_MONTHS = {
    '01': 'Jan',
    '02': 'Feb',
    '03': 'Mar',
    '04': 'Apr',
    '05': 'May',
    '06': 'Jun',
    '07': 'Jul',
    '08': 'Aug',
    '09': 'Sep',
    '10': 'Oct',
    '11': 'Nov',
    '12': 'Dec'
}

SPECIFIC_DAY_SUFFIX = {
    '1': 'st',
    '2': 'nd',
    '3': 'rd',
    '21': 'st',
    '22': 'nd',
    '23': 'rd',
    '31': 'st'
}


def validate_year(year):
    """
    Validate the year.
    """
    try:
        parsed_year = int(year)
    except Exception:
        return False
    return parsed_year >= 2015 and parsed_year <= 2018

def validate_month(month):
    """
    Validate the month.
    """
    return month in VALID_MONTHS.keys()

def create_filename(year, month):
    """
    Create a filename.
    """
    return '{}-{} ({}).md'.format(year, month, VALID_MONTHS[month])

def format_day(day):
    """
    Pretty format a day.
    """
    lstripped_day = day.lstrip('0')
    if lstripped_day in SPECIFIC_DAY_SUFFIX.keys():
        return '{}{}'.format(lstripped_day, SPECIFIC_DAY_SUFFIX[lstripped_day])
    return '{}th'.format(lstripped_day)

def create_headers(year, month):
    """
    Create the file content (headers).
    """
    headers = []
    lstripped_month = month.lstrip('0')
    date = datetime.date(int(year), int(lstripped_month), 1)
    base_month, month_next_day = date.strftime('%b'), date.strftime('%b')
    doc_title = date.strftime('# %B, %Y')
    while base_month == month_next_day:
        formatted_day = format_day(date.strftime('%d'))
        headers.append('{} {}'.format(date.strftime('### %A'), formatted_day))
        date += datetime.timedelta(days=1)
        month_next_day = date.strftime('%b')
    headers.append(doc_title)
    return list(reversed(headers))

def create_file_content(file_headers):
    """
    Create the file content using headers.
    """
    return ''.join(['{}\n\n'.format(x) for x in file_headers])

def write_file(file_name, file_content, path):
    """
    Create the file with the file content in the specified path.
    """
    existing_files = os.listdir(path)
    if file_name in existing_files:
        return False
    with open(os.path.join(path, file_name), 'w') as output:
        output.write(file_content)
    return True


if __name__ == '__main__':
    args = parser.parse_args()
    if not validate_year(args.year):
        print('Year {} is not valid.'.format(args.year))
        sys.exit(1)
    if not validate_month(args.month):
        print('Month {} is not valid.'.format(args.month))
        sys.exit(2)
    file_name = create_filename(args.year, args.month)
    file_headers = create_headers(args.year, args.month)
    file_content = create_file_content(file_headers)
    success = write_file(file_name, file_content, '.')
    if success:
        print('Created file {}'.format(file_name))
    else:
        print(('WARNING - file \'{}\' already '
               'exists in the directory.'.format(file_name)))
