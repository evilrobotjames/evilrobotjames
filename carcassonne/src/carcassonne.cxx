#include <iostream>
#include <stdlib.h>

#include "Tile.h"

using namespace std;

int main(int argc, char *argv[] __attribute__((unused)))
{
    if (argc != 1)
    {
        cout << "usage: carcassonne";
        exit(EXIT_FAILURE);
    }

    cout << "Let's play carcassonne!" << endl;

    Tile t = Tile();
    t.run();
}
