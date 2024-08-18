class ListSharding:
    def __init__(self, shard_map):
        self.shard_map = shard_map

    def get_shard(self, key):
        for shard, users_list in self.shard_map.items():
            if key in users_list:
                return shard
        else:
            raise ValueError("No shard found on this key")

shard_mapping = {
    0: ['user1', 'user2', 'user3'],
    1: ['user10', 'user11', 'user12'],
    2: ['user20', 'user21', 'user22']
}

list_sharding = ListSharding(shard_mapping)
print(list_sharding.get_shard('user21'))