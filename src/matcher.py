def tradeUP(preferences, student, hospital, hospital1):



def stableMatching(preferences):
    n = len(preferences['hospitals'])
    unmatchedCount = n
    studentsH = [-1] * n
    hospitalsUM = [False] * n

    while unmatchedCount > 0:
        hospital = next(i for i in range(n) if not hospitalsUM[i])
        for i in range(n):
            if hospitalsUM[i]:
                break

            student = preferences[hospital][i]
            if studentsH[student - n] == -1:
                studentsH[student - n] = hospital
                hospitalsUM[hospital] = True
                unmatchedCount -= 1
            else:
                hospital1 = studentsH[student - n]
                if not tradeUP(preferences, student, hospital, hospital1):
                    studentsH[student - n] = hospital
                    hospitalsUM[hospital] = True
                    hospitalsUM[hospital1] = False
    return studentsH