#include "Edge.h"

#include <assert.h>

Edge::Edge()
{
}

void Edge::SetTile(Tile *t)
{
    assert(t != nullptr);
    assert(tile == nullptr);

    tile = t;
}

void Edge::SetFeatureSection(EdgeEntryPoint eep, FeatureSection *fs)
{
    assert(fs != nullptr);

    switch (eep)
    {
        case EdgeEntryPoint::Left:
            assert(this->left == nullptr);
            this->left = fs;
            break;
        case EdgeEntryPoint::Middle:
            assert(this->middle == nullptr);
            this->middle = fs;
            break;
        case EdgeEntryPoint::Right:
            assert(this->right == nullptr);
            this->right = fs;
            break;
    }
}
