def solution(cacheSize, cities):
    cache = []
    running_time = 0
    num_cities = len(cities)
    cities = map(lambda city: city.lower(), cities)
    for ref in cities:
        if cacheSize == 0:
            return num_cities*5
        if not ref in cache:
            if len(cache) < cacheSize:
                cache.append(ref)
            else:
                cache.pop(0)
                cache.append(ref)
            running_time += 5

        else:
            cache.pop(cache.index(ref))
            cache.append(ref)
            running_time += 1

    return running_time
