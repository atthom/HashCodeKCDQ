
def algo(cache_size, nb_cache, endpoints):
    # endpoint is : (latency, [(idCache, latencyCache)], [(idVideo, requests])
    # for each enpoints, sort videos by requests
    for endpoint in endpoints:
        endpoint[2] = sorted(endpoint[2], key=video_sorter, reverse=True)


    return []


def video_sorter(video):
    return video[1]