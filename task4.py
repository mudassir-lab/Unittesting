"""Top Economy of bowlers in 2015"""


def calculate(matches_data, deliveries_data):
    bowlers_balls = {}
    bowlers_runs = {}
    matchin2015 = set()

    for match in matches_data:
        if match['season'] == '2015':
            matchin2015.add(match['id'])

    for delivery in deliveries_data:
        if delivery['match_id'] in matchin2015:
            temp_bowler = delivery['bowler']
            temp_run = int(delivery['total_runs'])
            if temp_bowler not in bowlers_balls:
                bowlers_balls[temp_bowler] = 1
            else:
                bowlers_balls[temp_bowler] += 1

            if temp_bowler not in bowlers_runs:
                bowlers_runs[temp_bowler] = temp_run
            else:
                if temp_run > 0:
                    bowlers_runs[temp_bowler] += temp_run
    # print(bowlers_runs, bowlers_balls)
    bowlers_econmy = {}
    for name, balls in bowlers_balls.items():
        # print(i)
        bowlers_econmy[name] = round(
            bowlers_runs[name]/bowlers_balls[name]*6, 2)
    # print(bowlers_econmy)
    return bowlers_econmy


def transform(bowlers_econmy):
    top10_econmy = sorted(bowlers_econmy.values())[:10]
    bowlers_name = []
    for econmy_s in top10_econmy:
        for blr, score in bowlers_econmy.items():
            if score == econmy_s:
                bowlers_name.append(blr)
    # print(bowlers_name, top10_econmy)
    return bowlers_name, top10_econmy


# o = calculate(matches_data, deliveries_data)
# transform(o)
