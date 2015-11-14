#include "FeatureSection.h"

#include <assert.h>

FeatureSection::FeatureSection()
{
}

void FeatureSection::SetTile(Tile *t)
{
    // Assert this FeatureSection hasn't appeared on another tile and isn't
    // being assigned to nullptr.
    assert(tile == nullptr);
    assert(t != nullptr);

    tile = t;
}
