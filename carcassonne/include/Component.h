#pragma once

class Edge;

class Component
{
public:
    Component(Edge *edge);

private:
    Edge *edge;
};
