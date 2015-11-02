#include "Edge.h"

Edge::Edge(Tile* t) :
    left(this),
    middle(this),
    right(this)
{
    tile = t;
}
