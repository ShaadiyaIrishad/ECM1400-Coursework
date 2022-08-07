# ECM1400-Coursework

# Introduction
This dashboard hosted locally provides the latest COVID-19 statistics and information.
The project extracts data from the Public Health England API service. 
It displays local and national data - 7 day infection rates, national current hospitalizations and national total deaths. 
The local region is Exeter and nation is England, by default.
It also displays news articles with search terms 'Covid', 'Covid-19' or 'coronavirus'.


# Installation
Download the repository from github: https://github.com/ShaadiyaIrishad/ECM1400-Coursework

```python
pip install uk_covid19
pip install sched
pip install logging
pip install requests
pip install flask
```

- Flask:
$ pip install Flask

- Public Health England COVID-19 Module:
$pip install uk_covid19

- Requests:
$pip install requests

- Pytest:
$pip install -U pytest

An API key is needed to obtain the news articles : https://newsapi.org/register


## Running the Program
To execute the program, open a programming environment that runs python 3.8.8 or newer. 
Once all modules have been installed, you can run the dashboard from `main.py`.

To navigate the dashboard via a web browser, use `http://127.0.0.1:5000/`. 

To quit the program, press CTRL + C in the terminal. 


## Removing News Articles
News articles can be removed by pressing the x on them, allowing a new article to take its place.


## Configuration file
Figures must be filled out in the configuration file for customization, before executing the program. 
Values in the config file can be changed to create a more personalized dashboard. 


## Testing
Tests are included to ensure project functionality. 

For testing: 
```python
pip install pytest
```


### Developer Details 
Shaadiya Irishad
ECM1400 - University of Exeter
Github: https://github.com/ShaadiyaIrishad


### License
[MIT](https://choosealicense.com/licenses/mit/)
