from get_input import get_inputs

import sys
def check(input, output):
    fromFiles = get_inputs(input, output)
    if fromFiles["matches"] is None:
        print("Invalid matching found")
        return
    stable_check(fromFiles)


def stable_check(fromFiles):
    for hospital ,h_ranking in enumerate(fromFiles["preferences"]["hospitals"]):
        matched_candidate = fromFiles["matches"][hospital]
        for candidate in h_ranking:
            if candidate == matched_candidate:
                break
            matched_hospital = fromFiles["matches"].index(candidate)
            h_rank = fromFiles["preferences"]["students"][candidate].index(hospital)
            current_rank = fromFiles["preferences"]["students"][candidate].index(matched_hospital)
            if h_rank<current_rank:
                print("Unstable matching found")
                return
    print("stable matching found")
    
# check("example.in", "example.out")
check(f"n_{sys.argv[1]}.in", f"n_{sys.argv[1]}.out")
# check("example.in", "invalid.out")
