class RangeSharding:
    def __init__(self, range_map):
        self.range_map = range_map 

    def get_shard(self, key):
        for shard, (start, end) in self.range_map.items():
            if start <= key < end:
                return shard
        else:
            raise ValueError("Key not found in the range shard")

ranges = {
    0: (1, 1000),
    1: (1000, 2000),
    2: (2000, 5000)
}

range_sharding = RangeSharding(ranges)
print(range_sharding.get_shard(1000))