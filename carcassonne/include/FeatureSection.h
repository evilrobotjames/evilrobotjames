#pragma once

class Edge;
class Tile;

class FeatureSection
{
public:
    FeatureSection();
    void SetTile(Tile *t);
private:
    Tile *tile;
};
