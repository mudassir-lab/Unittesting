"""Matches won per team per year"""


def calculate(matches_data):
    win_of_teams = {}
    all_season = []

    for match in matches_data:
        team_name = match["winner"]
        if team_name == '':
            continue
        if team_name not in win_of_teams:
            win_of_teams[team_name] = {}
            year = match['season']
            if year not in win_of_teams[team_name]:
                win_of_teams[team_name][year] = 1
            else:
                win_of_teams[team_name][year] += 1
        else:
            year = match['season']
            if year not in win_of_teams[team_name]:
                win_of_teams[team_name][year] = 1
            else:
                win_of_teams[team_name][year] += 1
        if year not in all_season:
            all_season.append(year)

    for team, years in win_of_teams.items():
        for year in all_season:
            if year not in years:
                years[year] = 0
        sorted_dict = dict(sorted(years.items()))
        win_of_teams[team] = sorted_dict

    # print(win_of_teams)
    all_season = sorted(all_season)
    return win_of_teams


def transform(win_of_teams):
    matchlist = []
    for team in win_of_teams:
        temp = list(win_of_teams[team].values())
        matchlist.append(temp)
    # print(matchlist)
    return matchlist
