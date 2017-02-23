

import sys
from collections import namedtuple, defaultdict




def totalvalue(comb):
    ' Totalise a particular combination of items'
    totwt = totval = 0
    for item, wt, val in comb:
        totwt += wt
        totval += val
    return (totval, -totwt) if totwt <= 400 else (0, 0)


# item (name, weight, value)

def add_item(item, items):
    items.append(item)


#items = [
#    (0, 9, 150), (1, 13, 35), (2, 153, 200), (3, 50, 160),
#    (4, 15, 60), (5, 68, 45), (6, 27, 60), (7, 39, 40),
#    (8, 23, 30), (9, 52, 10), (10, 11, 70), (11, 32, 30),
#    (12, 24, 15), (13, 48, 10), (14, 73, 40), (15, 42, 70), (16, 43, 75),
#    (17, 22, 80), (18, 7, 20), (19, 18, 12), (20, 4, 50), (21, 30, 10)
#]

def knapsack01_dp(items, limit):
    #print(items)
    table = [[0 for w in range(limit + 1)] for j in range(len(items) + 1)]

    for j in range(1, len(items) + 1):
        item, wt, val = items[j - 1]
       # print(item, wt, val)
        for w in range(1, limit + 1):
           # print(table[j - 1][w])
           # print(max(table[j - 1][w],  table[j - 1][w - wt] + val))
            if wt > w:
                table[j][w] = table[j - 1][w]
            else:
                table[j][w] = max(table[j - 1][w],  table[j - 1][w - wt] + val)

    result = []
    w = limit
    for j in range(len(items), 0, -1):
        was_added = table[j][w] != table[j - 1][w]
      #  print(table[j][w], table[j - 1][w])
        if was_added:
            item, wt, val = items[j - 1]
            result.append(items[j - 1])
            w -= wt

    return result

#list1 = [(1, 50, 1000*100), (4, 110, 500*100), (3, 30, 1500*100)]

#list2 = [(1, 50, 1000*300), (4, 110, 500*300), (3, 30, 1500*300)]

#list3 = [(1, 50, 1000*200), (4, 110, 500*200), (3, 30, 1500*200)]

#test = [list1, list2, list3]

#def prune_list(previous_result, current_tab):
#    for value_previous in previous_result:
#        for value_current in current_tab:
#            if value_previous[0] == value_current[0]:
#                if


def solve_it(tab_of_tab_request_servers, sizeof_server):
    result = []
    for tab_for_one_server in tab_of_tab_request_servers:
        result.append(knapsack01_dp(tab_for_one_server, sizeof_server))
    return result

#bagged = knapsack01_dp(items, 400)
#print("Bagged the following items\n  " +
#      '\n  '.join(sorted(item for item, _, _ in bagged)))
#val, wt = totalvalue(bagged)
#print("for a total value of %i and a total weight of %i" % (val, -wt))

Cache = namedtuple('Cache', ['id', 'capacity'])
Video = namedtuple('Video', ['id', 'size'])
Endpoint = namedtuple('Endpoint', ['id', 'dataCenterLat', 'cachesLat'])
RequestGroup = namedtuple('RequestGroup', ['nbRequests', 'idVideo', 'idEndpoint'])
Inputs = namedtuple('Inputs', ['videos', 'endpoints', 'requestGroups', 'nbCaches', 'cacheCapa'])


def parseInputs():
    # nb videos, nb endpoints, nb request descriptions, nb caches of capacity cacheCapa each.
    nbVid, nbEndp, nbReqGr, nbCaches, cacheCapa = map(int, input().split())
    videosSizes = list(map(int, input().split()))
    assert (len(videosSizes) == nbVid)
    videos = []
    for idVideo in range(nbVid):
        videos.append(Video(idVideo, videosSizes[idVideo]))
    endpoints = []
    for idEndpoint in range(nbEndp):
        datacenterLat, nbCachesConnected = map(int, input().split())
        cachesLat = dict()
        for iCache in range(nbCachesConnected):
            idCache, latency = map(int, input().split())
            cachesLat[idCache] = latency
        endpoints.append(Endpoint(idEndpoint, datacenterLat, cachesLat))
    requestGroups = []
    for iReqGr in range(nbReqGr):
        idVideo, idEndpt, nbRequests = map(int, input().split())
        requestGroups.append(RequestGroup(nbRequests, idVideo, idEndpt))
    return Inputs(videos, endpoints, requestGroups, nbCaches, cacheCapa)


def parseSolution():
    nbCachesUsed = int(input())
    videosByCache = dict()
    for iCache in range(nbCachesUsed):
        values = map(int, input().split())
        idCache = values[0]
        videos = values[1:]
        videosByCache[idCache] = videos
    return videosByCache


def checkValiditySolutionAndBuildCachesByVideo(inputs, videosByCache):
    videos, endpoints, requestGroups, nbCaches, cacheCapa = inputs
    cachesByVideo = defaultdict()
    for idCache, videosInCache in videosByCache.items():
        assert (0 <= idCache < nbCaches)
        assert (len(videosInCache) <= len(videos))
        sumVidSizes = 0
        for idVideo in videosInCache:
            assert (0 <= idVideo < len(videos))
            sumVidSizes += videos[idVideo].size
            cachesByVideo[idVideo].append(idCache)
        assert (0 < sumVidSizes <= cacheCapa)
    return cachesByVideo


def scoreSolution(inputs, videosByCache):
    videos, endpoints, requestGroups, nbCaches, cacheCapa = inputs
    cachesByVideo = checkValiditySolutionAndBuildCachesByVideo(inputs, videosByCache)
    sumGains = 0
    sumNbReqs = 0
    for nbRequests, idVideo, idEndpoint in requestGroups:
        endpoint = endpoints[idEndpoint]
        cachesLatenciesFromEndpt = []
        for idCache in cachesByVideo[idVideo]:
            cachesLatenciesFromEndpt.append(endpoint.cachesLat[idCache])
        latToDatacenter = endpoint.dataCenterLat
        minLatToCaches = min(cachesLatenciesFromEndpt)
        minLatTotal = min(minLatToCaches, latToDatacenter)
        gainReqGroup = nbRequests * (latToDatacenter - minLatTotal)
        sumGains += gainReqGroup
        sumNbReqs += nbRequests
    ratio = sumGains / sumNbReqs
    return int(ratio * 1000)


#if __name__ == '__main__':
#    inputs = parseInputs()
#    videosByCache = parseSolution()
#    score = scoreSolution(inputs, videosByCache)
#    print("score = ", score)


def totalvalue(comb):
    ' Totalise a particular combination of items'
    totwt = totval = 0
    for item, wt, val in comb:
        totwt += wt
        totval += val
    return (totval, -totwt) if totwt <= 400 else (0, 0)


# item (name, weight, value)

def add_item(item, items):
    items.append(item)


#items = [
#    (0, 9, 150), (1, 13, 35), (2, 153, 200), (3, 50, 160),
#    (4, 15, 60), (5, 68, 45), (6, 27, 60), (7, 39, 40),
#    (8, 23, 30), (9, 52, 10), (10, 11, 70), (11, 32, 30),
#    (12, 24, 15), (13, 48, 10), (14, 73, 40), (15, 42, 70), (16, 43, 75),
#    (17, 22, 80), (18, 7, 20), (19, 18, 12), (20, 4, 50), (21, 30, 10)
#]

def knapsack01_dp(items, limit):
    #print(items)
    table = [[0 for w in range(limit + 1)] for j in range(len(items) + 1)]

    for j in range(1, len(items) + 1):
        item, wt, val = items[j - 1]
       # print(item, wt, val)
        for w in range(1, limit + 1):
           # print(table[j - 1][w])
           # print(max(table[j - 1][w],  table[j - 1][w - wt] + val))
            if wt > w:
                table[j][w] = table[j - 1][w]
            else:
                table[j][w] = max(table[j - 1][w],  table[j - 1][w - wt] + val)

    result = []
    w = limit
    for j in range(len(items), 0, -1):
        was_added = table[j][w] != table[j - 1][w]
      #  print(table[j][w], table[j - 1][w])
        if was_added:
            item, wt, val = items[j - 1]
            result.append(items[j - 1])
            w -= wt

    return result

#list1 = [(1, 50, 1000*100), (4, 110, 500*100), (3, 30, 1500*100)]

#list2 = [(1, 50, 1000*300), (4, 110, 500*300), (3, 30, 1500*300)]

#list3 = [(1, 50, 1000*200), (4, 110, 500*200), (3, 30, 1500*200)]

#test = [list1, list2, list3]

#def prune_list(previous_result, current_tab):
#    for value_previous in previous_result:
#        for value_current in current_tab:
#            if value_previous[0] == value_current[0]:
#                if


def solve_it(tab_of_tab_request_servers, sizeof_server):
    result = []
    for tab_for_one_server in tab_of_tab_request_servers:
        result.append(knapsack01_dp(tab_for_one_server, sizeof_server))
    return result

#bagged = knapsack01_dp(items, 400)
#print("Bagged the following items\n  " +
#      '\n  '.join(sorted(item for item, _, _ in bagged)))
#val, wt = totalvalue(bagged)
#print("for a total value of %i and a total weight of %i" % (val, -wt))

all_data =parseInputs()

videos = all_data.videos

list3 = [(1, 50, 1000*200), (4, 110, 500*200), (3, 30, 1500*200)]


list_list_tuple = [[(-1, all_data.cacheCapa +1, 0) for _ in range(len(all_data.videos))] for _ in range(all_data.nbCaches)]

for requestGroup in all_data.requestGroups:
    nbRequest, idVideo, idEndpoint = requestGroup
    video = all_data.videos[idVideo]
    endPoint = all_data.endpoints[idEndpoint]
    cachesLaten = endPoint.cachesLat
    for idcache in cachesLaten:
        valeur = 1000000-cachesLaten[idcache] * nbRequest
        poids = video.size
        list_list_tuple[idcache][idVideo] = (idVideo, poids, valeur)


def printall(list_list_tuple):
    for list_tuple in list_list_tuple:
        print(list_tuple)

#print("zijdz")
#printall(list_list_tuple)
#print("adazpf,za")

res =solve_it(list_list_tuple, all_data.cacheCapa)

#printall(res)


def submit(res, f):
    f.write(str(len(res)))
    for icaches in range(0, len(res)):
        videos = ' '.join(map(lambda x:str(x[0]), res[icaches]))
        f.write(str(icaches) + videos)

f = open("zoo.check", "w")

stri = open("me_at_the_zoo.in", "r").read()
f.write(stri)
submit(res, f)
f.close()

