def parse_openings():
    openings = []

    openings += parse_opening_file('src/openings/e4_openings.txt')
    openings += parse_opening_file('src/openings/d4_openings.txt')

    return openings

def parse_opening_file(file_location):
    openings_list = []
    with open(file_location, 'r') as file:
        for line in file.readlines():
            l = line.strip().split(' ')

            for idx, i in enumerate(l):
                if i.startswith('//'):
                    l.pop(idx)

            openings_list.append(l)

    return openings_list