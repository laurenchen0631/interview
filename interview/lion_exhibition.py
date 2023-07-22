from dataclasses import dataclass

@dataclass
class LionDescription:
    name: str
    height: int

@dataclass
class LionSchedule:
    name: str
    enter_time: int
    exit_time: int

class LionCompetition:
    def __init__(self, lions: list[LionDescription], schedule: list[LionSchedule]):
        self._lions_detail = {lion.name: lion for lion in lions}
        self._lion_enter_schedule = dict[int, dict[int, list[str]]]()
        self._lion_exit_schedule = dict[int, dict[int, list[str]]]()
        
        for lion in schedule:
            if lion.enter_time not in self._lion_enter_schedule:
                self._lion_enter_schedule[lion.enter_time] = dict[int, list[str]]()
            
            if lion.exit_time not in self._lion_exit_schedule:
                self._lion_exit_schedule[lion.exit_time] = dict[int, list[str]]()
                
            height = self._lions_detail[lion.name].height
                
            if height not in self._lion_enter_schedule[lion.enter_time]:
                self._lion_enter_schedule[lion.enter_time][height] = []
            if height not in self._lion_exit_schedule[lion.exit_time]:
                self._lion_exit_schedule[lion.exit_time][height] = []
            
            self._lion_enter_schedule[lion.enter_time][height].append(lion.name)
            self._lion_exit_schedule[lion.exit_time][height].append(lion.name)
            
        self._competing_lions = [] # sorted heights
        self._current_lions = set()
        
    def lion_entered(self, current_time: int, height: int):
        if current_time not in self._lion_enter_schedule or height not in self._lion_enter_schedule[current_time] or not self._lion_enter_schedule[current_time][height]:
            self._competing_lions.append(height)
            return
            
        lions = self._lion_enter_schedule[current_time][height]
        self._current_lions.add(lions.pop()) # enter only once

    def lion_left(self, current_time: int, height: int):
        if current_time not in self._lion_exit_schedule or height not in self._lion_exit_schedule[current_time] or not self._lion_exit_schedule[current_time][height]:
            self._competing_lions.remove(height)
            return
        
        lions = self._lion_exit_schedule[current_time][height]
        self._current_lions.remove(lions.pop()) # exit only once

    
    def get_biggest_lions(self) -> list[str]:
        max_height = max(self._competing_lions) # faster when sorted? Use heap + binary search?
        res = []
        for lion in self._current_lions:
            if self._lions_detail[lion].height >= max_height:
                res.append(lion)
        res.sort()
        return res

comptition = LionCompetition(
    lions=[LionDescription("marry", 300), LionDescription("rob", 250)],
    schedule=[LionSchedule("marry", 10, 15), LionSchedule("rob", 13, 20)]
)
comptition.lion_entered(8, 200)
comptition.lion_entered(10, 310)
comptition.lion_entered(10, 300)
print(comptition.get_biggest_lions())
comptition.lion_entered(13, 250)
comptition.lion_left(13, 310)
print(comptition.get_biggest_lions())
comptition.lion_left(15, 300)
print(comptition.get_biggest_lions())
