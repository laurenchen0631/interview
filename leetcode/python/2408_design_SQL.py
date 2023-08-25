class SQL:
    def __init__(self, names: list[str], columns: list[int]):
        self._names = { name: i for i, name in enumerate(names) }
        self._cur_id = [0] * len(names)
        self._tables = [{} for _ in range(len(names))]

    def insertRow(self, name: str, row: list[str]) -> None:
        i = self._names[name]
        self._cur_id[i] += 1
        key = self._cur_id[i]

        self._tables[i][key] = row
        
    def deleteRow(self, name: str, rowId: int) -> None:
        i = self._names[name]
        del self._tables[i][rowId]

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        i = self._names[name]
        return self._tables[i][rowId][columnId-1]
        