import random
import string


class Codec:
    def __init__(self) -> None:
        self.chars = string.ascii_lowercase + string.digits
        self.map: dict[str, str] = {}
        self.url = 'http://tinyurl.com/'

    def _genKey(self) -> str:
        return ''.join(random.choices(self.chars, k=6))

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = self._genKey()
        while key in self.map:
            key = self._genKey()
        self.map[key] = longUrl
        return self.url + key
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.map[shortUrl.replace(self.url, '')]

c = Codec()
tiny = c.encode("https://leetcode.com/problems/design-tinyurl")
print(tiny)
print(c.decode(tiny))