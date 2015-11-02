#pragma once

class Edge;
class Tile;

class Edge
{
public:
    Edge(Tile *t);

private:
    Tile *tile;
};
