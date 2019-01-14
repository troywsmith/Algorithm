from collections import defaultdict, Counter
import pprint


def find_min_browsers(report, min_traffic_pct):

    # Iterate through report to get cumulative total trafifc, and traffic for ea brow
    browsers = defaultdict()
    total_traffic = 0

    for line in report:
        browser = line[0]
        version = line[1]
        traffic = line[2]

        if browser not in browsers:
            browsers[browser] = [traffic, [version]]
        else:
            browsers[browser][0] += traffic
            browsers[browser][1].append(version)
            total_traffic += traffic

    # Minimum traffic a browser should have to be considered
    min_traffic = total_traffic * (1 - min_traffic_pct)

    results = []
    for browser, data in browsers.items():
        traffic = data[0]
        versions = data[1]

        if traffic >= min_traffic:
            versions.sort()
            min_version = versions[0]
            results.append((browser, min_version))

    return results


if __name__ == '__main__':
    analytics = [
        ["Safari", '11', 119177],
        ["Chrome", '63.0.3239.132', 85426],
        ["Chrome", '63.0.3325.181', 81119],
        ["Internet Explorer", '11', 74185],
        ["Chrome", '64.0.3282.186', 54633],
        ["Chrome", '63.0.3239.84', 53506],
        ["Chrome", '62.0.3202.94', 41744],
        ["Edge", '16.16299', 32186],
        ["Chrome", '63.0.3282.167', 24153],
        ["Safari", '10', 22651],
        ["Firefox", '57', 22532],
        ["Chrome", '66.0.3225.109', 21846],
        ["Chrome", '63.0.3239.111', 21640],
        ["Chrome", '64.0.3282.137', 19658],
        ["Firefox", '58', 19090],
        ["Chrome", '64.0.3282.140', 15454],
    ]
    traffic = .95
    print(find_min_browsers(analytics, traffic))
