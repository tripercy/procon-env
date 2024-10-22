/*#include <iostream>

#include "board_env.cpp"
#include "board_env.h"

int main() {
    // Board init_board({"0123", "3210", "2222"}, 3, 4);
    // Board target_board({"0000", "0000", "0000"}, 3, 4);
    Die die({
        "11",
        "11",
    });

    std::vector<std::string> init_board_str = {
        "0123",
        "3210",
        "3322",
    };
    std::vector<std::string> target_str = {
        "0000",
        "0000",
        "0000",
    };

    Game game(init_board_str, target_str, 3, 4, {});
    game.cutDie(0, 2, 3, 3);

    for (int k = 0; k < 10; k++) {
        Die x = game.getDies()[k];
        for (int i = 0; i < x.getW(); i++) {
            for (int j = 0; j < x.getH(); j++) {
                std::cout << x.at(i, j) << " ";
            }
            std::cout << std::endl;
        }
        std::cout << "\n";
    }
return 0;
}
*/