import datetime
import requests
import json

def fetchInput():
    date = str(datetime.date.today())
    date = date.split('-')
    YEAR = date [0]
    MONTH = date [1]
    DAY = date[2]

    print("Fetching input for Day {day} of year {year}...".format(day = DAY, year = YEAR))
    session_is = getSession()
    cookies_are = dict(session=session_is)
    r = requests.get("https://adventofcode.com/{year}/day/{day}/input".format(year = YEAR, day = DAY), cookies=cookies_are)

    try:
        input = open("Day{day}\input.txt".format(day = DAY), 'a')
        input.write(r.text)
        input.close()
        print("Fetched! Happy coding :)")
    except FileNotFoundError:
        print("Error occurred when fetching today's input. Is it not the Advent of Code?")

    print("Fetched! Happy coding :)")

def getSession():
    with open("secrets.json") as secrets:
        data = json.load(secrets)
    return data['session']

if __name__ == '__main__':
    fetchInput()

    