class TimeMap(object):
    def bin(self, key, val, x, y):
        if x >= y:
            return x
        else:
            mid = (x+y)//2
            if self.d_time[key][mid] > val:
                y = mid - 1
            else:
                x = mid + 1
            return self.bin(key, val, x, y)
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d_val = collections.defaultdict(list)
        self.d_time = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.d_val[key].append(value)
        self.d_time[key].append(timestamp)

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        index = self.bin(key, timestamp, 0, len(self.d_time.get(key)) - 1)
        if index != -1: index = index - 1 if self.d_time[key][index] > timestamp else index
        if index > -1:
            val = self.d_val[key][index]
            self.d_val[key] = self.d_val[key][index:]
            self.d_time[key] = self.d_time[key][index:]
        else:
            val = ""
        return val



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)