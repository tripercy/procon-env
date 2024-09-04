#include "board_env.h"
#include <string>
#include <vector>

bool checkCoord(int x, int y, int w, int h)
{
    return x >= 0 && x < w && y >= 0 && y < h;
}

/*
 * DIE IMPLEMENTATION
 * */

Die::Die()
{
}

Die::Die(std::vector<std::string> dieStr)
{
    // TODO: FILL THIS
}

int Die::at(int x, int y)
{
    if (!checkCoord(x, y, n, n)) {
        return -1;
    }
    return _die[x][y];
}

std::string Die::toStr()
{
    // TODO: FILL THIS
}
/*
 * BOARD IMPLEMENTATION
 * */
Board::Board()
{
}

Board::Board(std::vector<std::string> boardStr, int w, int h)
{
    this->w = w;
    this->h = h;
    // TODO: FILL THIS
}

int Board::at(int x, int y)
{
    if (!checkCoord(x, y, w, h)) {
        return -1;
    }
    return _board[x][y];
}

std::string Board::toStr()
{
    // TODO: FILL THIS
}

/*
 * GAME IMPLEMENTATION
 * */
Game::Game(std::vector<std::string> initBoardStr, std::vector<std::string> targetStr, int w, int h, std::vector<Die> generalDies)
{
    this->initialBoard = Board(initBoardStr, w, h);
    this->targetBoard = Board(targetStr, w, h);
    this->dies = generalDies;
}

// Perform a die cut with dieIndex at top-left position (x, y)
// with direction s (0: top, 1: bottom, 2: left, 3: right)
double Game::cutDie(int dieIndex, int x, int y)
{
    // TODO: FILL THIS
    return 0;
}

double Game::getReward()
{
    // TODO: FILL THIS
    return 0;
}

std::vector<Die>& Game::getDies()
{
    return this->dies;
}

Board& Game::getInitBoard()
{
    return this->initialBoard;
}

Board& Game::getTargetBoard()
{
    return this->targetBoard;
}

std::string Game::toStr()
{
    // TODO: FILL THIS
}
