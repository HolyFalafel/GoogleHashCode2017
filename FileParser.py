filename = 'me_at_the_zoo.in'

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

for endpoint_num in range(0, Endpoints):
    # reading endpoint line
    endpoint_latency, num_of_connections = lines[list_index].strip().split()
    list_index += 1

    endpoint_caches = []
    # reading all endpoint caches
    for cache_num in range(0,int(num_of_connections)):
        bla = 0

f = 0
      # ls = line.strip().split()






          # rw.write('\t'.join(ls) + '\n')
