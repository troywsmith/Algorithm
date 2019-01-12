def find_duplicates(arr1, arr2):

    # Initialize an empty array to store the results
    duplicates = []

    # Iterate through both arrays at the same time
    x = 0
    y = 0
    while x < len(arr1) and y < len(arr2):

        # If numbers are the same, add the number to the results
        if arr1[x] == arr2[y]:
            duplicates.append(arr1[x])
            x += 1
            y += 1

        # If arr1 number is less than arr2 num, move arr1 pointer right
        elif arr1[x] < arr2[y]:
            x += 1

        # If both fail, arr2 num must be less than arr1 num and we should move arr2 pointer right
        else:
            y += 1

    # Return common elements
    return duplicates


if __name__ == '__main__':
    arr1 = [1, 5, 8, 10, 15, 24]
    arr2 = [1, 4, 8, 10]
    print(find_duplicates(arr1, arr2))
