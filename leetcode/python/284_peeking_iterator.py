class Iterator:
    def __init__(self, nums):
        pass
    def hasNext(self):
        pass
    def next(self):
        pass

class PeekingIterator:
    def __init__(self, iterator: Iterator):
        self._iterator = iterator
        self._peeked: int | None = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self._peeked != None:
            return self._peeked
        if not self._iterator.hasNext():
            raise StopIteration()
        self._peeked = self._iterator.next()
        return self._peeked

    def next(self):
        """
        :rtype: int
        """
        if (v := self._peeked) != None:
            self._peeked = None
            return v
        return self._iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._peeked != None or self._iterator.hasNext()