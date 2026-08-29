class TimeMap:

    def __init__(self):
        self.dict={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dict:
            self.dict[key].append([value,timestamp])
        else:
            self.dict[key] = [[value,timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""
        arr = self.dict[key]
        l = 0
        r = len(arr) - 1
        ans = -1
        while l <= r:
            m = (l+r)//2
            if arr[m][1] <= timestamp:
                ans = m
                l = m +1 
            else:
                r = m - 1
        if ans == -1:
            return ""
        else:
            return arr[ans][0]
        
