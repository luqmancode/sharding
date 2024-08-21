import hashlib
import bisect 

class ConsistentHashing:
    def __init__(self, nodes=None, replicas=100):
        self.replicas = replicas 
        self.ring = dict()
        self.sorted_keys = []

        if nodes:
            for node in nodes:
                self.add_node(node)

    def _hash(self, key):
        return int(hashlib.sha256(key.encode('utf-8')).hexdigest(), 16)

    def add_node(self, node):
        for i in range(self.replicas):
            hash_key = self._hash(f"{node}-{i}")
            self.ring[hash_key] = node
            print(self.ring, 5555555, self.sorted_keys)
            bisect.insort(self.sorted_keys, hash_key)

    def remove_node(self, node):
        for i in range(self.replicas):
            hash_key = self._hash(f"{node}-{i}")
            del self.ring[hash_key]
            index = bisect.bisect_left(self.sorted_keys, hash_key)
            self.sorted_keys.pop(index)

    def get_node(self, key):
        if not self.ring:
            return None
        hash_key = self._hash(key)
        index = bisect.bisect(self.sorted_keys, hash_key)

        if index == len(self.sorted_keys):
            index = 0
        return self.ring[self.sorted_keys[index]]

nodes = ['node1', 'node2', 'node3']

consistent_hash = ConsistentHashing(nodes=nodes, replicas=10)

print("Initial Distribution")
for key in ['user1', 'user2', 'user3', 'user4', 'user5']:
    node = consistent_hash.get_node(key)
    print(f"Key '{key}' is assigned to node '{node}'")


print("\nAdding node4 to the cluster:")
consistent_hash.add_node('node4')
for key in ['user1', 'user2', 'user3', 'user4', 'user5']:
    node = consistent_hash.get_node(key)
    print(f"Key '{key}' is assigned to node '{node}'")

print("\nRemoving node2 from the cluster:")
consistent_hash.remove_node('node2')
for key in ['user1', 'user2', 'user3', 'user4', 'user5']:
    node = consistent_hash.get_node(key)
    print(f"Key '{key}' is assigned to node '{node}'")