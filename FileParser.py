def parse_file(filename):
# filename = 'me_at_the_zoo.in'

    with open(filename, 'r') as ro:
          lines = ro.readlines()
    # for line in ro.readlines():
    # first_line = lines[0].strip().split()
    Videos, Endpoints, Request_Descriptions, Caches, Max_Cache_Size = lines[0].strip().split()

    video_sizes = lines[1].strip().split()

    lines.remove(lines[0])
    lines.remove(lines[0])

    # reading endpoints data
    list_index = 0

    Endpoints = int(Endpoints)

    endpoint_dict = {}
    cache_dict = {}

    for endpoint_num in range(0, Endpoints):
        # reading endpoint line
        endpoint_latency, num_of_connections = lines[list_index].strip().split()
        list_index += 1

        endpoint_caches = []

        # reading all endpoint caches
        for cache_num in range(0, int(num_of_connections)):
            req_cache, cache_latency = lines[list_index].strip().split()
            req_cache = int(req_cache)
            cache_latency = int(cache_latency)
            endpoint_caches.append((req_cache, cache_latency))
            list_index += 1
            # bla = 0

            cache_dict.setdefault(req_cache, []).append((endpoint_num, cache_latency))
        endpoint_dict[endpoint_num] = (int(endpoint_latency), tuple(endpoint_caches))

    ################# reading requests
    video_request_dict = {}  # key: video, value: (endpoint, request)
    endpoint_request_dict = {}  # key: endpoint, value: (video, request)
    endpoint_video_request_dict = {}

    endpoint_videos = {}

    for request_index in range(list_index, len(lines)):
        req_video, req_endpoint, num_of_requests = lines[request_index].strip().split()

        req_video = int(req_video)
        req_endpoint = int(req_endpoint)
        num_of_requests = int(num_of_requests)

        # adding to dictionaries
        video_request_dict.setdefault(req_video, []).append((req_endpoint, num_of_requests))
        endpoint_request_dict.setdefault(req_endpoint, []).append((req_video, num_of_requests))

        endpoint_video_request_dict[(req_video, req_endpoint)] = num_of_requests

        endpoint_videos.setdefault(req_endpoint, []).append(req_video)

    return int(Videos), Endpoints, int(Request_Descriptions), int(Caches), int(Max_Cache_Size), video_sizes, endpoint_dict, video_request_dict, endpoint_request_dict, cache_dict, endpoint_videos, endpoint_video_request_dict


# Videos, Endpoints, Request_Descriptions, Caches, Max_Cache_Size, video_sizes, endpoint_dict, video_request_dict, endpoint_request_dict = parse_file('me_at_the_zoo.in')
# f = 0




          # rw.write('\t'.join(ls) + '\n')
