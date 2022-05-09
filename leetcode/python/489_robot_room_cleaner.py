class Robot:
   def move(self):
       """
       Returns true if the cell in front is open and robot moves into the cell.
       Returns false if the cell in front is blocked and robot stays in the current cell.
       :rtype bool
       """
       pass

   def turnLeft(self):
       """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """
       pass

   def turnRight(self):
       """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """
       pass

   def clean(self):
       """
       Clean the current cell.
       :rtype void
       """
       pass

class Solution:
    def cleanRoom(self, robot: Robot):
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set[tuple[int,int]]()

        def goBack() -> None:
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()


        def dfs(p: tuple[int, int], d: int) -> None:
            robot.clean()
            visited.add(p)
            for i in range(len(dirs)):
                dir = (d + i) % len(dirs)
                pos = (p[0] + dirs[dir][0], p[1] + dirs[dir][1])
                if pos not in visited and robot.move():
                    dfs(pos, dir)
                    goBack()
                robot.turnRight()
        dfs((0,0), 0)