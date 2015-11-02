#pragma once

class Tile;

#include "Component.h"

class Edge
{
public:
    Edge(Tile *t);

private:
    Tile *tile;
    Component left;
    Component middle;
    Component right;
};
