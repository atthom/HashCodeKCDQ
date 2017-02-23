import sys
from collections import namedtuple

Cache = namedtuple('Cache', ['id', 'capacity'])
Video = namedtuple('Video', ['id', 'size'])
Endpoint = namedtuple('Endpoint', ['id', 'dataCenterLat','cachesLat'])
RequestGroup = namedtuple('RequestGroup', ['nbRequests','video','endpoint'])
Inputs = namedtuple('Inputs', ['videos','endpoints','requestGroups','nbCaches','cacheCapa'])

def parseInputs():
    #nb videos, nb endpoints, nb request descriptions, nb caches of capacity cacheCapa each.
    nbVid,nbEndp,nbReqGr,nbCaches,cacheCapa = map(int,input().split())
    videosSizes = list(map(int,input().split()))
    assert(len(videosSizes)==nbVid)
    videos = []
    for idVideo in range(nbVid):
        videos.append(Video(idVideo,videosSizes[idVideo]))
    endpoints = []
    for idEndpoint in range(nbEndp):
        datacenterLat, nbCachesConnected = map(int, input().split())
        cachesLat = dict()
        for iCache in range(nbCachesConnected):
            idCache, latency = map(int, input().split())
            cachesLat[idCache] = latency
        endpoints.append(Endpoint(idEndpoint,datacenterLat,cachesLat))
    requestGroups = []
    for iReqGr in range(nbReqGr):
        idVideo, idEndpt, nbRequests = map(int, input().split())
        requestGroups.append(RequestGroup(nbRequests,idVideo,idEndpt))
    return Inputs(videos,endpoints,requestGroups,nbCaches,cacheCapa)

def parseSolution():
    nbCachesUsed = int(input())
    videosByCache = dict()
    for iCache in range(nbCachesUsed):
        values = map(int,input().split())
        idCache = values[0]
        videos = values[1:]
        videosByCache[idCache] = videos
    return videosByCache

def checkValiditySolution(inputs, videosByCache):
    videos, endpoints, requestGroups, nbCaches, cacheCapa = inputs
    for idCache,videosInCache in videosByCache.items():
        assert(0 <= idCache < nbCaches)
        assert(len(videosInCache) <= len(videos))
        sumVidSizes = 0
        for idVideo in videosInCache:
            assert (0 <= idVideo < len(videos))
            sumVidSizes += videos[idVideo].size
        assert(0 < sumVidSizes <= cacheCapa)




for line in sys.stdin:
    print(line)



