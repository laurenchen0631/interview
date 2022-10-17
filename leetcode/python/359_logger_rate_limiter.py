class Logger:
    def __init__(self):
        self._log = dict[str, int]()
        self._wait = 10

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        nextTime = self._log.get(message, 0)
        if nextTime <= timestamp:
            self._log[message] = timestamp + self._wait
            return True
        return False



# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)