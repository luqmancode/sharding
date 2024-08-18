import hashlib 

class HashSharding:
    def __init__(self, no_shards):
        self.no_shards = no_shards

    def get_shard(self, key):
        hash_value = int(hashlib.md5(key.encode()).hexdigest(), 16)
        return hash_value % self.no_shards 

    
user_id = "user123"
hash_sharding = HashSharding(4)
print(hash_sharding.get_shard(user_id))