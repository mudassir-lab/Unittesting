"""Extra Conceded in 2016"""
# from csv import DictReader

# matches_file = open("mock_matches.csv", "r", encoding='utf-8')
# matches_data = DictReader(matches_file)

# deliveries_file = open("mock_deliveries.csv", "r", encoding='utf-8')
# deliveries_data = DictReader(deliveries_file)


def calculate(matches_data, deliveries_data):

    teams_data = {}
    # matchin2016=[]
    matchin2016 = set()
    for match in matches_data:
        if match['season'] == '2016':
            matchin2016.add(match['id'])
            team_name = match['team1']
            if team_name not in teams_data:
                teams_data[team_name] = 0

    # print(teams_data)
    # print(matchin2016)

    for delivery in deliveries_data:
        if delivery['match_id'] in matchin2016:
            team_name = delivery['bowling_team']
            extrarun = int(delivery['extra_runs'])
            if extrarun > 0:
                teams_data[team_name] += extrarun

    # print(teams_data)
    return teams_data


def transform(teams_data):

    names = list(teams_data.keys())
    exruns = list(teams_data.values())
    # print(names,exruns)
    return names, exruns

# o=calculate(matches_data,deliveries_data)
# transform(o)