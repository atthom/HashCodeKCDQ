import sys

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
for i in range(nbr_endpoints - 1):
    endpoint = []
    datacenter_latency, nbr_connected_cache = [int(item) for item in data[index].split(' ')]

    cache_latencies = []
    for j in range(nbr_connected_cache):
        cache_latencies.append([int(item) for item in data[index].split(' ')])
        index += 1

    endpoints.append([datacenter_latency, cache_latencies])

    index += 1
