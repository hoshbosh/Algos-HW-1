def get_inputs(rankings, matches = None):
    preferences = {"hospitals":[], "students":[]}
    match_obj = []

    with open(f"../data/{rankings}", 'r') as file:
        all_lines = file.readlines()
    
    n = int(all_lines[0])
    all_lines.pop(0)
    for i, v in enumerate(all_lines):
        curr = []
        for y in v.split(" "):
            curr.append(int(y[0]))
        preferences["hospitals" if i<n else "students"].append(curr)

    if not matches:
        return {
                "preferences": preferences
                }

    with open(f"../data/{matches}", 'r') as file:
        all_lines = file.readlines()

    for x in all_lines:
        match_obj.append(int(x[2]))

    return {
            "preferences": preferences,
            "matches": match_obj
        }
