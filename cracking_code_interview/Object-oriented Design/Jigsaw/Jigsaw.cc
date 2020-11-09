#include "Jigsaw.hh"

void orientTopLeftCorner(Jigsaw::Piece*)
{

}

template<int R, int C>
void Jigsaw::Puzzle<R,C>::setEdgeInSolution(std::vector<Piece*> pieces, Edge edge, int row, int col, Orientation orientation)
{
  Piece* piece {edge.getParentPiece()};
  piece->setEdgeAsOrientation(edge, orientation);
  pieces.remove(piece);
  solution[row][column] = piece;
}

template<int R, int C>
bool Jigsaw::Puzzle<R,C>::fitNextEdge(
  std::vector<Piece*> piecesToSearch,
  int row, int column)
{
  if (row == 0 && column == 0) {
    Piece* p {piecesToSearch.back()};
    piecesToSearch.pop_back();
    orientTopLeftCorner(p);
    solution[0][0] = p;
  }
  else {
    Piece* pieceToMatch {column == 0 ? solution[row-1][0] : solution[row][column-1]};
    Orientation orientationToMatch {column == 0 ? Orientation::Bottom : Orientation::Right};
    Edge edgeToMatch {pieceToMatch->getEdgeWithOrientation(orientationToMatch)};

    Edge* edge = getMatchingEdge(edgeToMatch, piecesToSearch);
    if (edge == nullptr) return false;

    Orientation orientation = getOppsite(orientationToMatch);
    setEdgeInSolution(piecesToSearch, edge, row, column, orientation);
  }
}

template<int R, int C>
bool Jigsaw::Puzzle<R,C>::solve()
{
  std::vector<Piece*> cornerPieces {};
  std::vector<Piece*> borderPieces {};
  std::vector<Piece*> insidePieces {};
  groupPieces(cornerPieces, borderPieces, insidePieces);

  for (int row = 0; row < R; ++row) {
    for (int col = 0; col < C; ++col) {
      std::vector<Piece*> piecesToSearch {getPieceListToSearch(cornerPieces, borderPieces, insidePieces, row, col)};
      if (!fitNextEdge(piecesToSearch, row, col)) {
        return false;
      }
    }
  }
}