#include <unordered_map>
#include <initializer_list>
#include <vector>

namespace Jigsaw {
  enum class Orientation {
    Left,
    Top,
    Right,
    Bottom,
  };

  Orientation getOppsite(Orientation o)
  {
    switch (o)
    {
    case Orientation::Left:
      return Orientation::Right;
    case Orientation::Top:
      return Orientation::Bottom;
    case Orientation::Right:
      return Orientation::Left;
    case Orientation::Bottom:
      return Orientation::Top;
    }
  }

  enum class Shape {
    Inner,
    Outer,
    Flat,
  };

  Shape getOppsite(Shape o)
  {
    switch (o)
    {
    case Shape::Inner:
      return Shape::Outer;
    case Shape::Outer:
      return Shape::Inner;
    case Shape::Flat:
      return Shape::Flat;
    }
  }

  class Piece;

  class Edge {
  public:
    Edge(Shape);
    bool fitsWith(Edge);
  private:
    Shape shape;
    Piece* parentPiece;
  };

  class Piece {
  public:
    Piece(std::initializer_list<Edge>);
    void rotateEdges(int numberRotations);
    bool isCorner();
    bool isBorder();

  private:
    std::unordered_map<Orientation, Shape> edges;
  };

  template<int R, int C>
  class Puzzle {
  public:
    Puzzle(std::vector<Piece*>);
    bool solve();
  private:
    std::vector<Piece*> pieces;
    Piece* solution[R][C];

    void setEdgeInSolution(std::vector<Piece*>, Edge, int row, int col, Orientation);
    bool fitNextEdge(std::vector<Piece*>, int row, int col);
  };
  
}

