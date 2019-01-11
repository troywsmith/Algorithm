"""
Given a real number from 0 to 1 that is passed in as a double, print the binary representation.
If the number cannot be represented accurately in binary with at most 32 characters, print 'ERROR'
"""


def to_binary(n):
    """
    Description: Solution for coverting any real number between 0 and 1 to binary
    Time Complexity: 
    """
    if n <= 0 or n >= 1:
        return 'ERROR'

    answer = '.'

    while n > 0 and len(answer) < 32:

        # Check if doubled n is greater than 1
        r = n * 2

        # If it is, add 1 to the answer and set n to doubled n without the 1
        if r >= 1:
            answer += '1'
            n = r - 1

        # If not, add 0 to the answer and set n to doubled n
        else:
            answer += '0'
            n = r

    return answer


# def convert(decimal, k):
#     """
#     Description: Solution for coverting any fractional decimal number to binary
#     Time Complexity: O(digits in decimal number)
#     """

#     # Convert decimal number to string
#     integ = int(decimal)
#     fract = decimal - integ

#     # Step 1: Convert integral part of decimal number to binary by repetetively halving it
#     results = []
#     while integ > 0:
#         results.insert(0, str(integ % 2))
#         integ /= 2
#     results.append('.')

#     # Step 2: Convert fractional part of decimal number to binary
#     while k > 0:

#         # Double the fractional part
#         result = str(fract * 2).split('.')

#         # Remove the integer part to add to the result
#         integ_part = result[0]
#         results.append(integ_part)

#         # Use the fractional part for the next iteration
#         fract = float('.' + result[1])

#         # Decrement k so this repeats k times
#         k -= 1

#     # Step 3: Combine results from step 1 and step 2 and return it
#     return float(''.join(results))


if __name__ == '__main__':
    num = 0.101
    print(to_binary(num))
