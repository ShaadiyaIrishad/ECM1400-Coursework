""" Module for handling COVID data updates """

# importing modules for logging
import logging

# importing API and modules to access it
import json
import sched
import time
from uk_covid19 import Cov19API

# setting up logging
logging.basicConfig(level=logging.DEBUG)


def parse_csv_data(csv_filename):
    """
    This function opens the csv file, extracts the data from the file and returns it.
    """

    logging.info("covid_data_handler :: parse_csv_data :: Begin")
    with open(csv_filename, 'r') as csvfile:
        lines = csvfile.readlines()
        lines = [line.replace('\n', '') for line in lines]
        logging.info("covid_data_handler :: parse_csv_data :: End")
        return lines[1:]


def process_covid_csv_data(covid_csv_data):
    """
    This function is used to iterate through, and extract specfic data in the covid_csv_data file
    as well as also being used in the covid_API_request for formatting purposes.
    """

    last7days_cases = 0
    current_hospital_cases = 0
    total_deaths = 0
    count = 0
    for row in covid_csv_data:
        row_splitted = row.split(',')
        if (not row_splitted[5] == '') and current_hospital_cases == 0:
            current_hospital_cases = row_splitted[5]
        if (not row_splitted[4] == '') and total_deaths == 0:
            total_deaths = row_splitted[4]

        if count in range(2, 9):
            last7days_cases += int(row_splitted[6])

        if int(total_deaths) > 0 and int(current_hospital_cases) > 0 and count > 8:
            break

        count += 1

    return last7days_cases, current_hospital_cases, total_deaths


def covid_API_request(location="Exeter", location_type="ltla"):
    """
    This function uses the uk_covid19 module and the API key from it
    to extract live data to be displayed on the flask interface.
    It also formats what order the data must be fetched in to be stored in a dictionary.
    """

    england_only = [
        'areaType=' + location_type,
        'areaName=' + location
    ]

    cases_and_deaths = {
        "date": "date",
        "areaType": "areaType",
        "areaName": "areaName",
        "areaCode": "areaCode",
        "newCasesByPublishDate": "newCasesByPublishDate",
        "hospitalCases": "hospitalCases",
        "cumDeaths28DaysByDeathDate": "cumDeaths28DaysByDeathDate"
    }

    api = Cov19API(filters=england_only, structure=cases_and_deaths)
    return api.get_json()


def process_live_data(json_obj):

    result_set = []

    my_list = json_obj['data']
    for line in my_list:

        result_set.append("{},{},{},{},{},{},{}".format(
            line['areaCode'],
            line['areaName'],
            line['areaType'],
            line['date'],
            line['cumDeaths28DaysByDeathDate'] if not line['cumDeaths28DaysByDeathDate'] == None else '',
            '',
            line['newCasesByPublishDate'] if not line['newCasesByPublishDate'] == None else ''
        ))

    return result_set


def create_total_list(live_data, csv_data):

    final_data = live_data + csv_data
    final_data = sorted(
        final_data, key=lambda x: x.split(',')[3], reverse=True)
    return final_data


def schedule_covid_updates(update_interval, update_name):
    """
    Create scheduler to update covid data based on user specified time,
    in order to update the covid data that is shown to the user.
    """

    nation_location, location = locations()


def locations():
    """
    This function extracts data from the configuration file 
    to set up the national_location and location variable.
    This will help set up the locations for data to be pulled from the API
    """

    f = open('config.json',)
    config_dict = json.load(f)
    location = config_dict["location"]
    nation_location = config_dict["nation_location"]

    return nation_location, location
