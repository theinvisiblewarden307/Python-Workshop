#Exercise: Rainfall:

rainfall = {}

while True:   # I don't know how many entries the user will give me
    city_name = input('Enter city: ').strip()

    if city_name == '':   # no input? break
        break

    mm_rain = input('Rain: ').strip()
    mm_rain = int(mm_rain)

    if city_name in rainfall:    # if we've already seen this city...
        rainfall[city_name] += mm_rain
    else:
        rainfall[city_name] = mm_rain    