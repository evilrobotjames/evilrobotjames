#pragma once

class Tile;

#include "Edge.h"

class Tile
{
public:
    Tile();

private:
    Edge n;
    Edge e;
    Edge s;
    Edge w;
};
