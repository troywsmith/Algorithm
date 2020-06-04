# def find_year(people):
#     """
#     Solution 1: Naive
#     Time Complexity:
#     """
#     # Find the last year someone was alive (max death year)
#     max_death = 1989
#     for birth, death in people:
#         print(birth, death)
#         max_death = max(max_death, death)

#     # Count how many people are alive in each year from 1900 to the max death year
#     max_people = 0
#     max_year = 1900
#     for x in range(1900, max_death+1):
#         year_alive_count = 0
#         for birth, death in people:
#             if birth <= x and x <= death:
#                 year_alive_count += 1
#         if year_alive_count > max_people:
#             max_people = year_alive_count
#             max_year = x

#             if max_people >= len(people):
#                 return max_year

#     return max_year


def find_year(people):
    """
    Time Complexity: O(P log P) where P is number of people 
    """
    births = [person[0] for person in people]
    deaths = [person[1] for person in people]
    births.sort()
    deaths.sort()

    max_year = 0
    max_people = 0
    people_alive = 0

    b = 0
    d = 0
    while b < len(births):

        if births[b] <= deaths[d]:
            people_alive += 1

            if people_alive > max_people:
                max_people = people_alive
                max_year = births[b]

            b += 1

        elif births[b] > deaths[d]:
            people_alive -= 1
            d += 1

    return max_year


if __name__ == '__main__':
    people = [
        [1900, 1980],
        [1940, 1970],
        [1920, 1950],
        [1910, 1970],
        [1960, 2000],
    ]
    print(find_year(people))
