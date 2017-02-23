import math
import copy

# Output:
#   Array containing array representing one cache
#   Each cache contains videos
#   [ [vId, vId, ...], ...]
def algo(cache_size, nb_cache, endpoints, video_sizes):
    # endpoint is : (latency, [(idCache, latencyCache)], [(idVideo, requests])
    # for each enpoints, sort videos by requests

    # Initialization
    caches = [[] for item in range(nb_cache - 1)]
    used_endpoints = copy.deepcopy(endpoints)


    while not is_full(compute_used_place_cache(caches, videos_sizes)):
        for index in range(nb_cache - 1):
            endpoint_id = used_endpoints[find_nearest_endpoint_not_empty(index, used_endpoints)]
            video_id = used_endpoints[endpoint_id][2].pop(0)[0]
            caches[index].append(video_id)

    return caches

def find_nearest_endpoint_not_empty(cache_id, endpoints):
    nearest = [none, math.inf]
    for index in range(len(videos_required) - 1):
        endpoint = endpoints[index]
        if endpoint[1][cache_id] < nearest[1] and len(endpoint[2]) == 0:
            nearest[0] = index
            nearest[1] = endpoint[1][cache_id]



def compute_used_place_cache(caches, video_sizes):
    caches_used_place = []

    for cache in caches:
        used_place = 0
        for video_id in cache:
            used_place += video_sizes[video_id]

            caches_used_place.append(used_place)

    return caches_used_place

def is_full(cache_size, video_sizes, caches):
    for cache in caches:
        for s in video_sizes:
            if cache + s < cache_size:
                return false

    return true
