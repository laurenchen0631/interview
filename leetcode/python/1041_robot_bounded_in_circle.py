class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dirIndex: int = 0
        coord = [0, 0]
        for _ in range(4):
            for c in instructions:
                if c == 'R':
                    dirIndex = (dirIndex + 1) % len(dirs)
                elif c == 'L':
                    dirIndex = (dirIndex - 1) % len(dirs)
                else:
                    coord[0] += dirs[dirIndex][0]
                    coord[1] += dirs[dirIndex][1]
            if coord[0] == 0 and coord[1] == 0:
                return True
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.isRobotBounded("GGLLGG"))
    print(s.isRobotBounded("GG"))
    print(s.isRobotBounded("GL"))