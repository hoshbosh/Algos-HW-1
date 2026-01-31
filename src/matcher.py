from get_input import get_inputs
import time

def stableMatching(preferences):
    n = len(preferences["preferences"]["hospitals"])
    free = [x for x in range(n)]
    matches = [None] * n

    while len(free) > 0:

        curr = free[0]
        curr_prefs = preferences['preferences']['hospitals'][curr]


        for student in curr_prefs:
            matched = student in matches
            student_curr_prefs = preferences['preferences']['students'][student]
            if not matched:
                matches[curr] = student
                free.pop(0)
                break


            elif student_curr_prefs.index(curr) < student_curr_prefs.index(matches.index(student)):
                replaced = matches.index(student)
                matches[curr] = student
                matches[replaced] = None
                free.pop(0)
                free.append(replaced)
                break
            else:
                continue


    return matches

#creates output file
def matchingOutput(preferences):
    matches = stableMatching(preferences)
    print(matches)
    with open(f"..\\data\\n_{len(matches)}.out", "w") as f:
        for hospital, student in enumerate(matches):
            f.write(f"{hospital + 1} {student + 1}\n")


#for local testing purposes
#print(stableMatching(get_inputs('n_200.in')))
matchingOutput(get_inputs("n_400.in"))
