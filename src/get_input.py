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
            curr.append(int(y)-1)
        preferences["hospitals" if i<n else "students"].append(curr)

    if not matches:
        return {
                "preferences": preferences
                }

    with open(f"../data/{matches}", 'r') as file:
        all_lines = file.readlines()

    inv = {}
    for x in all_lines:
        for y in x.split(" "):
            if y not in inv:
                inv[y] = 1
            else:
                inv[y] += 1
    for _, freq in inv.items():
        if freq!=2:
            match_obj=None
    if len(inv) != n:
        match_obj = None
    if match_obj is not None:
        for x in all_lines:
            sep = x.split(" ")
            match_obj.append(int(sep[2])-1)

    return {
            "preferences": preferences,
            "matches": match_obj
        }
