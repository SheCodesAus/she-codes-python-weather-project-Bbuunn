import csv
from datetime import datetime
import calendar


DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celsius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celsius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    # ISO Example: 2021-07-02T07:00:00+08:00
    # expected_result = "Monday 05 July 2021"

    d = datetime.fromisoformat(iso_string)
    return "{0} {1:02} {2} {3}".format(
        calendar.day_name[d.weekday()],
        d.day,
        calendar.month_name[d.month],
        d.year
    )



def convert_f_to_c(temp_in_farenheit):
    """Converts a temperature from farenheit to celsius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celsius, rounded to 1dp.
    """
    return round((float(temp_in_farenheit) - 32) * 5 / 9, 1)
    

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    weather_data = [float(x) for x in weather_data]
    return sum(weather_data)/len(weather_data)


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    csv_data = []
    with open(csv_file) as csv_data_list:
        reader = csv.reader(csv_data_list)
        # skip heading line
        next(csv_data_list)
        # remove empty line
        for data in reader:
            if data != []:
                csv_data.append([
                    data[0],
                    int(data[1]),
                    int(data[2])
                ])
    return csv_data


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list.
    """

    if len(weather_data) == 0:
        return ()

    min_temp = ()
    for i, temp in enumerate(weather_data):
        temp = float(temp)
        # first iteration:
        # assign first tuple
        if (min_temp == ()):
            min_temp = (temp, i)
            continue
        # if current temp is lower
        # than min temp
        # update min temp and index
        if (temp <= min_temp[0]):
            min_temp = (temp, i)

    return min_temp

    

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    
    if len(weather_data) == 0:
        return ()

    max_temp = ()
    for i, temp in enumerate(weather_data):
        temp = float(temp)
        if (max_temp == ()):
            max_temp = (temp, i)
            continue
        if (temp >= max_temp[0]):
            max_temp = (temp, i)

    return max_temp



def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    # example 1: 5 Day Overview
    # number of days = length of weather_data
    summary = f"{len(weather_data)} Day Overview\n"
    # example 2: The lowest temperature will be 9.4°C, and will occur on Friday 02 July 2021.
    # use find_min(), convert_f_to_c(),
    # format_temperature(), convert_date() 
    min_weather_data = [x[1] for x in weather_data]
    sum_min_temp = convert_f_to_c(find_min(min_weather_data)[0])
    min_index = find_min(min_weather_data)[1]
    sum_min_date = convert_date(weather_data[min_index][0])

    summary += f"  The lowest temperature will be {format_temperature(sum_min_temp)}, and will occur on {sum_min_date}.\n"
    
     # example 3: The highest temperature will be 20.0°C, and will occur on Saturday 03 July 2021.1
    # use find_max(), convert_f_to_c(),
    # format_temperature, convert_date()
    max_weather_data = [x[2] for x in weather_data]

    sum_max_temp = convert_f_to_c(find_max(max_weather_data)[0])
    max_index = find_max(max_weather_data)[1]
    sum_max_date = convert_date(weather_data[max_index][0])

    summary += f"  The highest temperature will be {format_temperature(sum_max_temp)}, and will occur on {sum_max_date}.\n"
    
    # example 4: The average low this week is 12.2°C.
    sum_ave_low = convert_f_to_c(calculate_mean(min_weather_data))
    summary += f"  The average low this week is {format_temperature(sum_ave_low)}.\n"

    # example 5: The average high this week is 17.8°C.
    sum_ave_high = convert_f_to_c(calculate_mean(max_weather_data))
    summary += f"  The average high this week is {format_temperature(sum_ave_high)}.\n"
    
    return summary


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    # new_line = "\n"
    # concatenate each line to summary
    summary = ""
    for day in weather_data:
        summary += f"---- {convert_date(day[0])} ----\n"
        summary += f"  Minimum Temperature: {format_temperature(convert_f_to_c(day[1]))}\n"
        summary += f"  Maximum Temperature: {format_temperature(convert_f_to_c(day[2]))}\n\n"
    return summary
