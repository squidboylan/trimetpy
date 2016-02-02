import requests
import xmltodict
import datetime
import collections
import json

class Trimet:
    def __init__(self):
        self.key = '27422954448A28C962C416950'

    def get_arrival(self, stop_id):
        r = requests.get('https://developer.trimet.org/ws/V1/arrivals/locIDs/'
                         + str(stop_id) + '/appID/' + self.key)

        data = dict()

        arrivals = xmltodict.parse(r.text)

        if not 'arrival' in arrivals['resultSet']:
            return None

        if isinstance(arrivals['resultSet']['arrival'], collections.OrderedDict):
            arrivals['resultSet']['arrival'] = [arrivals['resultSet']['arrival']]

        data['query_time'] = datetime.datetime.fromtimestamp(int(arrivals['resultSet']['@queryTime'])/1000)
        data['arrivals'] = []
        for arrival in arrivals['resultSet']['arrival']:
            status = arrival['@status']
            time = datetime.datetime.fromtimestamp(int(arrival['@' + status])/1000)
            td = time - data['query_time']
            days = td.days
            hours= td.seconds // 3600
            minutes = td.seconds % 3600 / 60
            seconds = (td.seconds % 3600) % 60
            full_sign = arrival['@fullSign']
            arr = {status: time, 'hours': hours, 'minutes': minutes,
                   'seconds': seconds, 'fullsign': full_sign,
                   'stopid': stop_id, 'status': status}
            data['arrivals'].append(arr)

        return data

    def get_arrival_beta(self, stop_id):
        r = requests.get('https://developer.trimet.org/ws/v2/arrivals/locIDs/'
                         + str(stop_id) + '/appID/' + self.key)

        data = dict()

        arrivals = json.loads(r.text)

        if not 'arrival' in arrivals['resultSet']:
            return None

        """
        if isinstance(arrivals['resultSet']['arrival'], collections.OrderedDict):
            arrivals['resultSet']['arrival'] = [arrivals['resultSet']['arrival']]
        """

        data['query_time'] = datetime.datetime.fromtimestamp(int(arrivals['resultSet']['queryTime'])/1000)
        data['arrivals'] = []
        for arrival in arrivals['resultSet']['arrival']:
            status = arrival['status']
            time = datetime.datetime.fromtimestamp(int(arrival[status])/1000)
            td = time - data['query_time']
            days = td.days
            hours= td.seconds // 3600
            minutes = td.seconds % 3600 / 60
            seconds = (td.seconds % 3600) % 60
            full_sign = arrival['fullSign']
            load_percentage = arrival['loadPercentage']
            arr = {status: time, 'hours': hours, 'minutes': minutes,
                   'seconds': seconds, 'fullsign': full_sign,
                   'stopid': stop_id, 'status': status, 'loadPercentage':
                   load_percentage}
            data['arrivals'].append(arr)

        return data

if __name__ == '__main__':
    t = Trimet()

    while 1:
        try:
            stop_id = input("Stop ID: ")

            arrivals = t.get_arrival_beta(stop_id)
            print arrivals
        except:
            pass
