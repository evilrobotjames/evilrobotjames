#ifndef __EDGE_H__
#define __EDGE_H__

class Edge;

#include "Tile.h"

class Edge
{

public:
    Edge(Tile *t);

private:
    int i;
    Tile *tile;
};

#endif
