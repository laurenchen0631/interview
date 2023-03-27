class HtmlParser:
   def getUrls(self, url):
       pass

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> list[str]:
        def getHostname(url):
            # split url by slashes
            # for instance, "http://example.org/foo/bar" will be split into
            # "http:", "", "example.org", "foo", "bar"
            # the hostname is the 2-nd (0-indexed) element
            return url.split('/')[2]

        curHost = getHostname(startUrl)
        visited = set()

        def dfs(url, htmlParser):
            visited.add(url)
            for link in htmlParser.getUrls(url):
                if getHostname(link) == curHost and link not in visited:
                    dfs(link, htmlParser)

        dfs(startUrl, htmlParser)
        return list(visited)