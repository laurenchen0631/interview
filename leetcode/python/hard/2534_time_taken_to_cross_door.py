from collections import deque


class Solution:
    def timeTaken(self, arrival: list[int], state: list[int]) -> list[int]:
        enter_queue = deque()
        exit_queue = deque()
        cur_time = 0
        prev_state = 1
        i = 0
        res = [0] * len(arrival)
        
        while i < len(arrival) or enter_queue or exit_queue:
            while i < len(arrival) and arrival[i] <= cur_time:
                if state[i] == 0:
                    enter_queue.append(i)
                else:
                    exit_queue.append(i)
                i += 1
            
            # If the door was used in the previous second for exiting, the person who wants to exit goes first.
            if prev_state == 1:
                if exit_queue:
                    res[exit_queue.popleft()] = cur_time
                elif enter_queue:
                    res[enter_queue.popleft()] = cur_time
                    prev_state = 0
            # If the door was used in the previous second for entering, the person who wants to enter goes first.
            else:
                if enter_queue:
                    res[enter_queue.popleft()] = cur_time
                elif exit_queue:
                    res[exit_queue.popleft()] = cur_time
                    prev_state = 1
                # If the door was not used in the previous second, then the person who wants to exit goes first.
                else: 
                    prev_state = 1
            cur_time += 1
        return res