
#include "Tile.h"
//#include "Edge.h"

Tile::Tile()
{
    this->n = new Edge(this);
    this->e = new Edge(this);
    this->s = new Edge(this);
    this->w = new Edge(this);
}

int Tile::run()
{
    return 0;
}
