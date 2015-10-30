#ifndef __TILE_H__
#define __TILE_H__

class Tile;

#include "Edge.h"

class Tile
{
public:
    Tile();
    int run();

private:
    Edge *n;
    Edge *e;
    Edge *s;
    Edge *w;
};

#endif
