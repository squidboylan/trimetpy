import requests
import xmltodict
import datetime
import collections
import json

class TrimetBeta:
    def __init__(self):
        self.key = '27422954448A28C962C416950'

    def get_arrival(self, stop_id):
        r = requests.get('https://developer.trimet.org/ws/v2/arrivals/locIDs/'
                         + str(stop_id) + '/appID/' + self.key)
        arrivals = json.loads(r.text)
        return arrivals

if __name__ == '__main__':
    t = TrimetBeta()

    while 1:
        stop_id = input("Stop ID: ")

        arrivals = t.get_arrival(stop_id)
        print arrivals['resultSet']['arrival'][0]
