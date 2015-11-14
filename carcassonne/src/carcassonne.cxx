#include <iostream>
#include <stdlib.h>

#include "carcassonneConfig.h"
#include "Tile.h"
#include "FeatureSection.h"

using namespace std;

int main(int argc, char **)
{
    if (argc != 1)
    {
		cout << "usage: carcassonne";
		exit(EXIT_FAILURE);
    }

    cout << "Let's play carcassonne!" << endl;
    cout << "Version: " << carcassonne_VERSION_MAJOR << "."
         << carcassonne_VERSION_MINOR << endl;

    FeatureSection field = FeatureSection();
    FeatureSection road = FeatureSection();
    FeatureSection castle = FeatureSection();

    Edge edge = Edge();

	Tile tile = Tile();


}
