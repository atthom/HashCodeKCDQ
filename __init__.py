import sys
from algo_v1 import algo
from out import saveOutput

data = [item[:-1] for item in sys.stdin.readlines()]

# Parses the first line
first_line = data[0].split(' ')

nbr_videos = int(first_line[0])
nbr_endpoints = int(first_line[1])
nbr_request_description = int(first_line[2])
nbr_cache = int(first_line[3])
cache_size = int(first_line[4])

# Parses the second one: size of videos
video_sizes = [int(item) for item in data[1].split(' ')]


# Parses each endpoint
endpoints = []
index = 2
for i in range(nbr_endpoints):
    endpoint = []
    datacenter_latency, nbr_connected_cache = [int(item) for item in data[index].split(' ')]

    cache_latencies = {}
    for j in range(nbr_connected_cache):
        cache_id, latency = [int(item) for item in data[index].split(' ')]
        cache_latencies[cache_id] = latency
        index += 1

    endpoints.append([datacenter_latency, cache_latencies])

    index += 1

videos = []
for i in range(len(video_sizes)):
    line = data[index].split(' ')
    videos.append((int(line[0]), int(line[1]), int(line[2])))
    index += 1

for video in videos:
    if len(endpoints[video[1]]) == 2:
        endpoints[video[1]].append([])
    endpoints[video[1]][2].append((video[0], video[2]))

caches = algo(cache_size, nbr_cache, endpoints, video_sizes)
saveOutput("kitten.out", caches)