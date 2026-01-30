import get_input

def stableMatching(preferences):
    n = len(preferences["preferences"]["hospitals"])
    free = [x for x in range(n)]
    matches = [None] * n

    while len(free) > 0:

        curr = free.pop(0)
        curr_prefs = preferences['preferences']['hospitals'][curr]


        for student in curr_prefs:
            matched = student in matches
            student_curr_prefs = preferences['preferences']['students'][student]
            if not matched:
                matches[student] = curr
                break


            elif student_curr_prefs.index(curr) < student_curr_prefs.index(matches.index(student)):
                matches[matches.index(student)] = None
                matches[student] = curr
            else:
                continue


    return matches

#creates output file
def matchingOutput(preferences):
    matches = stableMatching(preferences)

    with open(f"..\\data\\n_{len(matches)}.out", "w") as f:
        for hospital, student in enumerate(matches):
            f.write(f"{hospital + 1} {student + 1}\n")
