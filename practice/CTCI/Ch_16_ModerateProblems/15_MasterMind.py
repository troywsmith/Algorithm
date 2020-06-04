def hit_counter(actual, guess):
    """
    Time Complexity: O(M*N)
    Space Complexity: O(H)
    """

    hits = 0
    pseudo_hits = 0
    used_slots = set()
    used_guesses = set()

    # Count hits first: count number of correct slot colors
    for i in range(len(guess)):

        if actual[i] == guess[i]:
            hits += 1
            used_slots.add(i)
            used_guesses.add(i)
            continue

    # Count pseudo hits: count number of correct colors, skip hit slots
    for i in range(len(guess)):

        for j in range(len(actual)):

            if i in used_guesses or j in used_slots:
                continue

            if guess[i] == actual[j]:
                pseudo_hits += 1
                used_slots.add(j)
                used_guesses.add(i)

    print(used_slots, used_guesses)
    # Return hits and pseudo hits
    return (hits, pseudo_hits)


if __name__ == '__main__':
    actual = 'RRRG'
    guess =  'GGRR'
    print(hit_counter(actual, guess))
