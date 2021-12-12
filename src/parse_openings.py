def parse_openings():
    openings = []

    with open('src/openings/e4_openings.txt', 'r') as e4_openings:
        for line in e4_openings.readlines():
            l = line.strip().split(' ')
            openings.append(l)

    with open('src/openings/d4_openings.txt', 'r') as d4_openings:
        for line in d4_openings.readlines():
            l = line.strip().split(' ')
            openings.append(l)

    return openings