class RecentCounter:
    def __init__(self):
        self.requests = []
    def ping(self, t):
        self.requests.append(t)
        requests = 0
        for i in range(len(self.requests)-1, -1, -1):
            if t - self.requests[i] <= 3000:
                requests += 1
        return requests

obj = RecentCounter()
param_1 = obj.ping(5)
param_2 = obj.ping(5)

print(param_1, param_2)
