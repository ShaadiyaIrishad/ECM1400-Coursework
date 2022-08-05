import logging
import json
import sched
import time
from uk_covid19 import Cov19API


logging.basicConfig(level=logging.DEBUG)


def parse_csv_data(csv_filename):

    logging.info("covid_data_handler :: parse_csv_data :: Begin")
    with open(csv_filename, 'r') as csvfile:
        lines = csvfile.readlines()
        lines = [line.replace('\n', '') for line in lines]
        logging.info("covid_data_handler :: parse_csv_data :: End")
        return lines[1:]


def process_covid_csv_data(covid_csv_data):
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

    nation_location, location = locations()


def locations():

    f = open('config.json',)
    config_dict = json.load(f)
    location = config_dict["location"]
    nation_location = config_dict["nation_location"]

    return nation_location, location
