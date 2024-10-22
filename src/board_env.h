#pragma once

#include <string>
#include <vector>

/*
 * Represents a Die/Pattern
 */
class Die {
    std::vector<std::vector<int>> _die;
    int w, h;

   public:
    Die();
    Die(std::vector<std::string> dieStr);
    int at(int x, int y);
    std::string toStr();
    int getW();
    int getH();
    void setW(int w);
    void setH(int h);
};

/*
 * Represents a board
 */
class Board {
    std::vector<std::vector<int>> _board;
    int w;
    int h;

   public:
    Board();
    Board(std::vector<std::string> boardStr, int w, int h);
    int at(int x, int y);
    int getVal(int x, int y);
    void setVal(int x, int y, int val);
    std::string toStr();
    int getW();
    int getH();
    void setW(int w);
    void setH(int h);
};

/*
 * Represents a game
 */
class Game {
    int numberOfCuts;
    std::vector<Die> dies;
    Board initialBoard;
    Board targetBoard;

   public:
    Game(std::vector<std::string> initBoardStr, std::vector<std::string> targetStr, int w, int h, std::vector<Die> generalDies);

    // Perform a die cut with dieIndex at top-left position (x, y)
    // with direction s (0: top, 1: bottom, 2: left, 3: right)
    double cutDie(int dieIndex, int x, int y, int s);
    int getNumberOfCuts();

    double getReward();

    std::vector<Die>& getDies();
    Board& getInitBoard();
    Board& getTargetBoard();
    std::string toStr();
};
