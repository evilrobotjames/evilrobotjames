#pragma once

#include <vector>
#include "Tile.h"

class TileSet
{
public:
    TileSet();

private:
    std::vector<Tile> tiles;
};
