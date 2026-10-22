import heapq


# ---------------- Problem 1: LRU Cache ----------------

class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}                      # key -> Node
        # dummy head and tail so we never check for None
        self.head = Node()                 # head.next = most recently used
        self.tail = Node()                 # tail.prev = least recently used
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._add_front(node)
        return node.value

    def put(self, key, value):
        if self.capacity <= 0:
            return
        if key in self.map:
            node = self.map[key]
            node.value = value
            self._remove(node)
            self._add_front(node)
            return
        if len(self.map) >= self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.key]
        node = Node(key, value)
        self.map[key] = node
        self._add_front(node)


# ---------------- Problem 2: Event Scheduler ----------------

def can_attend_all(events):
    events = sorted(events)
    for i in range(1, len(events)):
        if events[i][0] < events[i - 1][1]:     # next starts before previous ends
            return False
    return True


def min_rooms_required(events):
    if not events:
        return 0
    starts = sorted(e[0] for e in events)
    ends = sorted(e[1] for e in events)
    rooms = 0
    max_rooms = 0
    j = 0
    for s in starts:
        if s >= ends[j]:        # some meeting already finished, reuse its room
            j += 1
        else:
            rooms += 1          # nobody free, need a new room
        max_rooms = max(max_rooms, rooms)
    return max_rooms


# ---------------- Future proofing: assign room names ----------------

def assign_rooms(events):
    order = sorted(range(len(events)), key=lambda i: events[i][0])
    busy = []                      # min-heap of (end_time, room_no)
    free = []                      # min-heap of free room numbers
    total = 0
    result = [None] * len(events)
    for i in order:
        start, end = events[i]
        while busy and busy[0][0] <= start:
            _, r = heapq.heappop(busy)
            heapq.heappush(free, r)
        if free:
            r = heapq.heappop(free)
        else:
            r = total
            total += 1
        result[i] = "Room " + chr(ord("A") + r) if r < 26 else "Room " + str(r + 1)
        heapq.heappush(busy, (end, r))
    return result


# ---------------- Tests ----------------

if __name__ == "__main__":
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    assert c.get(1) == 1
    c.put(3, 3)                    # evicts key 2
    assert c.get(2) == -1
    c.put(4, 4)                    # evicts key 1
    assert c.get(1) == -1
    assert c.get(3) == 3
    assert c.get(4) == 4
    c.put(3, 30)                   # update
    assert c.get(3) == 30

    assert can_attend_all([(9, 10), (10, 11), (11, 12)]) is True
    assert can_attend_all([(9, 11), (10, 12)]) is False
    assert can_attend_all([]) is True
    assert min_rooms_required([(9, 10), (10, 11), (11, 12)]) == 1
    assert min_rooms_required([(9, 11), (10, 12), (10, 13)]) == 3
    assert min_rooms_required([(1, 5), (2, 3), (4, 6), (5, 7)]) == 2
    assert min_rooms_required([]) == 0
    print(assign_rooms([(9, 11), (10, 12), (11, 13)]))
    print("all tests passed")
