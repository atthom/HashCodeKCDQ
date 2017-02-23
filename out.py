
'''
caches : array of :
    cache: array of video id
'''
def saveOutput(fileName, caches):
    valid_cache = [x for x in caches if len(x) != 0]
    file = open(fileName, 'w')
    file.write(str(len(valid_cache)) + "\n")
    cache_id = 0
    for cache in caches:
        if len(cache) != 0 :
            line = str(cache_id)
            for video in cache:
                line += " " + str(video)
            line += "\n"
            file.write(line)
        cache_id += 1
    file.close()

if __name__ == "__main__":
    saveOutput("test_output", [[1,2,3], [0], [], [2,3]])