def write_to_file(filename, num_of_cache_server_descriptions, cache_videos_dict):
    f = open(filename, 'w')

    f.write(str(num_of_cache_server_descriptions) + '\n')

    for cache in range(0,num_of_cache_server_descriptions):
        str_1 = str(cache)
        for curr_video in cache_videos_dict[cache]:
            str_1 += ' ' + str(curr_video)
        str_1 += '\n'
        f.write(str_1)

    bla = 0

# write_to_file(filename, )