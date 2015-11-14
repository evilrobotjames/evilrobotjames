#pragma once

class Tile;

#include <array>
#include <vector>

#include "Edge.h"

enum class CompassPoint {North, East, South, West};

class Tile
{
public:
    Tile();

    std::vector<FeatureSection *> getFeatureSections();
    std::array<Edge *, 4> getEdges();


    //void AddFeatureSection(FeatureSection *fs, TileCompass tc,
    //                       EdgeEntry ep);

    void EnsureComplete();

private:

    std::array<Edge, 4> edges;
    std::vector<FeatureSection *> featureSections;
};
