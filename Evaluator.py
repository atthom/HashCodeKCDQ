import sys
from collections import namedtuple,defaultdict

Cache = namedtuple('Cache', ['id', 'capacity'])
Video = namedtuple('Video', ['id', 'size'])
Endpoint = namedtuple('Endpoint', ['id', 'dataCenterLat','cachesLat'])
RequestGroup = namedtuple('RequestGroup', ['nbRequests','idVideo','idEndpoint'])
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

def checkValiditySolutionAndBuildCachesByVideo(inputs, videosByCache):
    videos, endpoints, requestGroups, nbCaches, cacheCapa = inputs
    cachesByVideo = defaultdict()
    for idCache,videosInCache in videosByCache.items():
        assert(0 <= idCache < nbCaches)
        assert(len(videosInCache) <= len(videos))
        sumVidSizes = 0
        for idVideo in videosInCache:
            assert (0 <= idVideo < len(videos))
            sumVidSizes += videos[idVideo].size
            cachesByVideo[idVideo].append(idCache)
        assert(0 < sumVidSizes <= cacheCapa)
    return cachesByVideo

def scoreSolution(inputs, videosByCache):
    videos, endpoints, requestGroups, nbCaches, cacheCapa = inputs
    cachesByVideo = checkValiditySolutionAndBuildCachesByVideo(inputs, videosByCache)
    sumGains = 0
    sumNbReqs = 0
    for nbRequests,idVideo,idEndpoint in requestGroups:
        endpoint = endpoints[idEndpoint]
        cachesLatenciesFromEndpt = []
        for idCache in cachesByVideo[idVideo]:
            cachesLatenciesFromEndpt.append(endpoint.cachesLat[idCache])
        latToDatacenter = endpoint.dataCenterLat
        minLatToCaches = min(cachesLatenciesFromEndpt)
        minLatTotal = min(minLatToCaches,latToDatacenter)
        gainReqGroup = nbRequests * (latToDatacenter - minLatTotal)
        sumGains += gainReqGroup
        sumNbReqs += nbRequests
    ratio = sumGains/sumNbReqs
    return int(ratio*1000)

if __name__ == '__main__':
    inputs = parseInputs()
    videosByCache = parseSolution()
    score = scoreSolution(inputs,videosByCache)
    print("score = ",score)
