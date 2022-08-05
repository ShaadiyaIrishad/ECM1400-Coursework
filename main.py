from flask import Flask, render_template
from covid_data_handler import parse_csv_data, process_covid_csv_data, covid_API_request, process_live_data, create_total_list
from covid_news_handling import news_API_request


app = Flask(__name__, template_folder='./')


updates = [
    {'title': 'Covid-19 Dashboard'}]


articles = news_API_request()


@app.route('/')
def hello():
    result = parse_csv_data("nation_2021-10-28.csv")
    last7days_cases, current_hospital_cases, total_deaths = process_covid_csv_data(
        result)
    live_dict = covid_API_request()
    print(live_dict)
    return render_template('index.html',
                           favicon=True,
                           updates=" ",
                           title="Covid-19 Dashboard",
                           location=" ",
                           local_7day_infections=" ",
                           nation_location=" ",
                           national_7day_infections=last7days_cases,
                           hospital_cases=current_hospital_cases,
                           deaths_total=total_deaths,
                           news_articles=articles,
                           image="cov_image.jpg"
                           )


if __name__ == '__main__':

    app.run()
    result = parse_csv_data("nation_2021-10-28.csv")
    last7days_cases, current_hospital_cases, total_deaths = process_covid_csv_data(
        result)
    print(" last 7 days -> {} \n hospital -> {} \n total_death -> {}".format(
        last7days_cases, current_hospital_cases, total_deaths))
    live_dict = covid_API_request()
    live_formated = process_live_data(live_dict)
    result = create_total_list(live_formated, result)
    print(result[:15])
    last7days_cases, current_hospital_cases, total_deaths = process_covid_csv_data(
        result)
    print(" last 7 days -> {} \n hospital -> {} \n total_death -> {}".format(
        last7days_cases, current_hospital_cases, total_deaths))
