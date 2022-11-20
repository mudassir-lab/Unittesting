"""Matches played per year"""


def calculate(matches_data):
    mplayed = {}
    for match in matches_data:
        # print(match)
        year = match['season']
        if year not in mplayed:
            mplayed[year] = 1
        else:
            mplayed[year] += 1
    mplayed = dict(sorted(mplayed.items()))
    # print(mplayed)
    return mplayed


def transform(mplayed):
    seasons = list(mplayed.keys())
    num_of_matches = list(mplayed.values())
    # print(seasons,num_of_matches)

    return seasons, num_of_matches

# calculate(matches_data)
