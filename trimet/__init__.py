import requests
import xmltodict
import datetime
import collections

class Trimet:
    def __init__(self):
        self.key = '27422954448A28C962C416950'

    def get_arrival(self, arrival_id):
        r = requests.get('https://developer.trimet.org/ws/V1/arrivals/locIDs/'
                         + str(arrival_id) + '/appID/' + self.key)

        return xmltodict.parse(r.text)

if __name__ == '__main__':
    t = Trimet()

    stop_id = 7027

    arrivals = t.get_arrival(stop_id)
    if isinstance(arrivals['resultSet']['arrival'], collections.OrderedDict):
        arrivals['resultSet']['arrival'] = [arrivals['resultSet']['arrival']]

    query_time = datetime.datetime.fromtimestamp(int(arrivals['resultSet']['@queryTime'])/1000)
    for arrival in arrivals['resultSet']['arrival']:
        time = datetime.datetime.fromtimestamp(int(arrival['@scheduled'])/1000)
        td = time - query_time
        days = td.days
        hours= td.seconds // 3600
        minutes = td.seconds % 3600 / 60
        seconds = (td.seconds % 3600) % 60
        full_sign = arrival['@fullSign']

        print(
            "stopID: " + str(stop_id) + " " + full_sign + " arriving at " +
            str(time) + " (" + str(hours) + " hours " +
            str(minutes) + " minutes and " + str(seconds) + " seconds from now)"
        )
