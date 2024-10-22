#include "board_env.h"

#include <iostream>
#include <string>
#include <vector>

bool checkCoord(int x, int y, int w, int h) {
    return x >= 0 && x < w && y >= 0 && y < h;
}

/*
 * DIE IMPLEMENTATION
 * */

Die::Die() {
}

Die::Die(std::vector<std::string> dieStr) {
    _die.clear();
    for (auto x : dieStr) {
        std::vector<int> temp;
        for (auto y : x) {
            int val = y - '0';
            temp.push_back(val);
        }
        _die.push_back(temp);
    }
    w = _die.size();
    h = _die[0].size();
}

int Die::at(int x, int y) {
    if (!checkCoord(x, y, w, h)) {
        return -1;
    }
    return _die[x][y];
}

std::string Die::toStr() {
    std::string s = "";
    for (auto x : _die) {
        for (auto y : x) {
            char c = y + '0';
            s += c;
        }
        s += "\n";
    }
    return s;
}

int Die::getW() {
    return this->w;
}

int Die::getH() {
    return this->h;
}

void Die::setW(int w) {
    this->w = w;
}

void Die::setH(int h) {
    this->h = h;
}
/*
 * BOARD IMPLEMENTATION
 * */
Board::Board() {
}

Board::Board(std::vector<std::string> boardStr, int w, int h) {
    this->w = w;
    this->h = h;
    _board.clear();
    for (auto x : boardStr) {
        std::vector<int> temp;
        for (auto y : x) {
            int val = y - '0';
            temp.push_back(val);
        }
        _board.push_back(temp);
    }
}

int Board::at(int x, int y) {
    if (!checkCoord(x, y, w, h)) {
        return -1;
    }
    return _board[x][y];
}

std::string Board::toStr() {
    std::string s = "";
    for (auto x : _board) {
        for (auto y : x) {
            char c = y + '0';
            s += c;
        }
        s += "\n";
    }
    return s;
}

int Board::getVal(int x, int y) {
    return _board[x][y];
}

void Board::setVal(int x, int y, int val) {
    if (checkCoord(x, y, w, h)) {
        _board[x][y] = val;
    }
}

int Board::getH() {
    return this->h;
}

int Board::getW() {
    return this->w;
}

void Board::setH(int h) {
    this->h = h;
}

void Board::setW(int w) {
    this->w = w;
}

/*
 * GAME IMPLEMENTATION
 * */
Game::Game(std::vector<std::string> initBoardStr, std::vector<std::string> targetStr, int w, int h, std::vector<Die> generalDies) {
    this->initialBoard = Board(initBoardStr, w, h);
    this->targetBoard = Board(targetStr, w, h);
    this->dies.clear();
    this->numberOfCuts = 0;
    std::string first_die = "1";
    dies.push_back(Die({first_die}));

    for (int i = 1; i < 9; i++) {
        int n = (1 << i);

        std::vector<std::string> temp_die_1;
        std::vector<std::string> temp_die_2;
        std::vector<std::string> temp_die_3;
        for (int j = 0; j < n; j++) {
            std::string row_die_1 = "";
            std::string row_die_2 = "";
            std::string row_die_3 = "";

            for (int k = 0; k < n; k++) {
                row_die_1 += '1';

                if (j & 1) {
                    row_die_2 += '0';
                } else {
                    row_die_2 += '1';
                }

                if (k & 1) {
                    row_die_3 += '0';
                } else {
                    row_die_3 += '1';
                }
            }
            temp_die_1.push_back(row_die_1);
            temp_die_2.push_back(row_die_2);
            temp_die_3.push_back(row_die_3);
        }
        dies.push_back(Die(temp_die_2));
        dies.push_back(Die(temp_die_3));
        dies.push_back(Die(temp_die_1));
    }

    for (auto x : generalDies) {
        dies.push_back(x);
    }
}

// Perform a die cut with dieIndex at top-left position (x, y)
// with direction s (0: top, 1: bottom, 2: left, 3: right)
double Game::cutDie(int dieIndex, int x, int y, int s) {
    this->numberOfCuts++;
    Die cur_die = dies[dieIndex];

    int x1 = std::max(0, x), y1 = std::max(0, y);
    int x2 = std::min(x + cur_die.getW(), initialBoard.getW()), y2 = std::min(y + cur_die.getH(), initialBoard.getH());

    if (s == 2) {
        for (int i = x1; i < x2; i++) {
            std::vector<int> temp;
            for (int j = 0; j < initialBoard.getH(); j++) {
                if (y1 <= j && j < y2) {
                    int x_die = i - x1;
                    int y_die = j - y1;
                    if (cur_die.at(x_die, y_die) == 1) {
                        temp.push_back(initialBoard.at(i, j));
                    } else {
                        initialBoard.setVal(i, j - temp.size(), initialBoard.at(i, j));
                    }
                } else {
                    initialBoard.setVal(i, j - temp.size(), initialBoard.at(i, j));
                }
            }
            int ct = 0;
            for (int j = initialBoard.getH() - temp.size(); j < initialBoard.getH(); j++) {
                initialBoard.setVal(i, j, temp[ct]);
                ct++;
            }
        }
    } else if (s == 3) {
        for (int i = x1; i < x2; i++) {
            std::vector<int> temp;
            for (int j = initialBoard.getH() - 1; j >= 0; j--) {
                if (y1 <= j && j < y2) {
                    int x_die = i - x1;
                    int y_die = j - y1;
                    if (cur_die.at(x_die, y_die) == 1) {
                        temp.push_back(initialBoard.at(i, j));
                    } else {
                        initialBoard.setVal(i, j + temp.size(), initialBoard.at(i, j));
                    }
                } else {
                    initialBoard.setVal(i, j + temp.size(), initialBoard.at(i, j));
                }
            }
            int ct = temp.size() - 1;
            for (int j = 0; j < temp.size(); j++) {
                initialBoard.setVal(i, j, temp[ct]);
                ct--;
            }
        }
    } else if (s == 1) {
        for (int i = y1; i < y2; i++) {
            std::vector<int> temp;
            for (int j = initialBoard.getW() - 1; j >= 0; j--) {
                if (x1 <= j && j < x2) {
                    int x_die = j - x1;
                    int y_die = i - y1;
                    if (cur_die.at(x_die, y_die) == 1) {
                        temp.push_back(initialBoard.at(j, i));
                    } else {
                        initialBoard.setVal(j + temp.size(), i, initialBoard.at(j, i));
                    }
                } else {
                    initialBoard.setVal(j + temp.size(), i, initialBoard.at(j, i));
                }
            }
            int ct = temp.size() - 1;
            for (int j = 0; j < temp.size(); j++) {
                initialBoard.setVal(j, i, temp[ct]);
                ct--;
            }
        }
    } else {
        for (int i = y1; i < y2; i++) {
            std::vector<int> temp;
            for (int j = 0; j < initialBoard.getW(); j++) {
                if (x1 <= j && j < x2) {
                    int x_die = j - x1;
                    int y_die = i - y1;
                    if (cur_die.at(x_die, y_die) == 1) {
                        temp.push_back(initialBoard.at(j, i));
                    } else {
                        initialBoard.setVal(j - temp.size(), i, initialBoard.at(j, i));
                    }
                } else {
                    initialBoard.setVal(j - temp.size(), i, initialBoard.at(j, i));
                }
            }
            int ct = 0;
            for (int j = initialBoard.getW() - temp.size(); j < initialBoard.getW(); j++) {
                initialBoard.setVal(j, i, temp[ct]);
                ct++;
            }
        }
    }
    return 0;
}

int Game::getNumberOfCuts() {
    return this->numberOfCuts;
}

double Game::getReward() {
    return 0;
}

std::vector<Die>& Game::getDies() {
    return this->dies;
}

Board& Game::getInitBoard() {
    return this->initialBoard;
}

Board& Game::getTargetBoard() {
    return this->targetBoard;
}

std::string Game::toStr() {
    return getInitBoard().toStr();
}
