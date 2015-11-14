#pragma once

class Tile;
class FeatureSection;

#include <array>

// Position of entry point when viewed from the centre point of the tile.
enum class EdgeEntryPoint {Left, Middle, Right};

class Edge
{
public:
    Edge();
    void SetFeatureSection(EdgeEntryPoint eep, FeatureSection *fs);
    void GetFeatureSection(EdgeEntryPoint eep);
    void SetTile(Tile *t);
private:
    Tile *tile;
    FeatureSection *left;
    FeatureSection *middle;
    FeatureSection *right;
};
