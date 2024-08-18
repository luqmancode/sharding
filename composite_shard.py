from hash_shard import HashSharding
from range_shard import RangeSharding

class CompositeShard:
    def __init__(self, no_shard, ranges):
        self.hash_sharding = HashSharding(no_shard)
        self.range_sharding = RangeSharding(ranges)

    def get_shard(self, key1, key2):
        hash_shard = self.hash_sharding.get_shard(key1)
        range_shard = self.range_sharding.get_shard(key2)
        return (hash_shard, range_shard)

ranges = {
    0: (0, 1000),
    1: (1000, 2000),
    2: (2000, 3000)
}

composite_shard = CompositeShard(6, ranges)
print(composite_shard.get_shard('user12456', 2000))