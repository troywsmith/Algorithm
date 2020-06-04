"""
This problem was asked by Microsoft.
Given a clock time in hh:mm format, determine, to the nearest degree, 
the angle between the hour and the minute hands.
Bonus: When, during the course of a day, will the angle be zero?
"""


def findAngle(time):
    hour = int(time[0:2])
    minute = int(time[3:])
    minHand = (minute/60) * 360
    hourHand = (hour/12)*360 + (minute/60) * (360/12)
    return abs(hourHand - minHand)


def calcAngle(time):

    h = int(time[0:2])
    m = int(time[3:])

    # validate the input
    if (h < 0 or m < 0 or h > 12 or m > 60):
        print('Wrong input')

    if (h == 12):
        h = 0
    if (m == 60):
        m = 0

    # Calculate the angles moved by
    # hour and minute hands with
    # reference to 12:00
    hour_angle = 0.5 * (h * 60 + m)
    minute_angle = 6 * m

    # Find the difference between two angles
    angle = abs(hour_angle - minute_angle)

    # Return the smaller angle of two
    # possible angles
    angle = min(360 - angle, angle)

    return angle


if __name__ == '__main__':
    time = "03:30"
    print(findAngle(time))
    print(calcAngle(time))
