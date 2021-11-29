from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        mailToName, graph = self._createGraph(accounts)
        return self._dpsSeparateGraph(mailToName, graph)

    def _createGraph(self, accounts: list[list[str]]) -> tuple[dict[str, str], defaultdict[str, set[str]]]:
        mailToName: dict[str, str] = {}
        graph: defaultdict[str, set[str]] = defaultdict(set)
        for name, node, *children in accounts:
            mailToName[node] = name
            for child in children:
                mailToName[child] = name
                graph[node].add(child)
                graph[child].add(node)

        return mailToName, graph

    def _dpsSeparateGraph(self, nodes: dict[str, str], graph: dict[str, set[str]]) -> list[list[str]]:
        visited: set[str] = set()
        result: list[list[str]] = []
        for mail, name in nodes.items():
            if mail in visited:
                continue

            visited.add(mail)
            stack: list[str] = [mail]
            mails: list[str] = []
            while len(stack) > 0:
                v = stack.pop()
                mails.append(v)
                for node in graph[v]:
                    if node not in visited:
                        visited.add(node)
                        stack.append(node)
            result.append([name] + sorted(mails))
        return result



if __name__ == '__main__':
    s = Solution()
    print(s.accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))
    print(s.accountsMerge([["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]))
