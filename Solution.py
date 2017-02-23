import FileParser, FileWriter

Videos, Endpoints, Request_Descriptions, Caches, Max_Cache_Size, video_sizes, endpoint_dict, video_request_dict, endpoint_request_dict, cache_dict, endpoint_videos, endpoint_video_request_dict = \
    FileParser.parse_file('me_at_the_zoo.in')

cache_video_shibutz = {}

cache_video_weight = {}
for cache in range(0, Caches):
    cache_video_weight[cache] = []

    for curr_video in range(0, len(video_sizes)):
        sum = 0
        video_size = int(video_sizes[curr_video])

        for cache_endpoint, cache_latency in cache_dict.get(cache, []):

            # video is in endpoint request
            if curr_video in endpoint_videos[cache_endpoint]:
                endpoint_tuple = endpoint_dict[cache_endpoint]
                endpoint_latency = endpoint_tuple[0]

                latency_weight = endpoint_latency - cache_latency

                request_num_endpoint_video = endpoint_video_request_dict[(curr_video, cache_endpoint)]

                # request_num_endpoint_video = endpoint_request_dict[cache_endpoint]
                sum += latency_weight * request_num_endpoint_video
        weight = sum // video_size
        cache_video_weight[cache].append((curr_video, weight))

    # sort tuples by weight
    # cache_video_weight[cache].sort(key = lambda tup: tup[1])
    cache_video_weight[cache] = sorted(cache_video_weight[cache], key=lambda x: -x[1])
    bla = 0

    cache_video_shibutz[cache] = []
    total_size_in_cache = 0

    for video, weight in cache_video_weight[cache]:
        size = int(video_sizes[video])
        if total_size_in_cache + size <= Max_Cache_Size:
            cache_video_shibutz[cache].append(video)
            total_size_in_cache += size

dfsdf = 0
bla = 0

def VideoToCache (cache_video_value):
    bla = 0