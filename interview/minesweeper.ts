
function generateRandomMinesweeperBoard(rows, cols, numMines) {
  // Create an empty board filled with cell objects 
  const board = Array.from({ length: rows }, () =>
      Array.from({ length: cols }, () => ({
          isMine: false,
          isClicked: false,
          isFlagged: false,
          adjacentMines: 0,
      }))
  );

  // Place mines randomly on the board 
  let minesPlaced = 0;
  while (minesPlaced < numMines) {
      const row = Math.floor(Math.random() * rows);
      const col = Math.floor(Math.random() * cols);

      if (!board[row][col].isMine) {
          board[row][col].isMine = true;
          minesPlaced++;
      }
  }

  // Calculate the number of adjacent mines for each cell 
  for (let i = 0; i < rows; i++) {
      for (let j = 0; j < cols; j++) {
          if (!board[i][j].isMine) {
              let count = 0;
              // Check adjacent cells 
              for (let x = -1; x <= 1; x++) {
                  for (let y = -1; y <= 1; y++) {
                      const newRow = i + x;
                      const newCol = j + y;
                      if (
                          newRow >= 0 &&
                          newRow < rows &&
                          newCol >= 0 &&
                          newCol < cols &&
                          board[newRow][newCol].isMine
                      ) {
                          count++;
                      }
                  }
              }
              board[i][j].adjacentMines = count;
          }
      }
  }

  return board;
}

const board = generateRandomMinesweeperBoard(5, 5, 3);
const bfs = (start: [number, number], board: Cell[][]) => {
  const rows = board.length;
  const cols = board[0].length;
  const res: [number,number][] = [];
  let q = [start];
  const dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]];
  const visited = new Set<string>();
  while (q.length > 0) {
    const tmp: [number,number][] = [];
    for (const [i, j] of q) {
      const key = `${i}-${j}`;
      if (visited.has(key)) continue;
      visited.add(key);
      for (const [di, dj] of dirs) {
        const ii = i + di;
        const jj = j + dj;
        if (ii < 0 || ii >= rows || jj < 0 || jj >= cols) {
          continue;
        }
        
        res.push([ii, jj]);
        if (board[ii][jj].adjacentMines === 0) {
          tmp.push([ii, jj]);
          console.log([ii, jj])
        }
      }
    }
    q = tmp;
  }
  return res;
}

for (const row of board) {
  const output: string[] = []
  for (const cell of row) {
    output.push(cell.isMine ? 'M' : String(cell.adjacentMines) || ' ')
  }
  console.log(output.join(''))
}

console.log(bfs([0, 0], board));

interface Cell {
isMine: boolean;
isClicked: boolean;
isFlagged: boolean;
adjacentMines: number;
}

interface AppProps {
rows: number;
cols: number;
mines: number;
}