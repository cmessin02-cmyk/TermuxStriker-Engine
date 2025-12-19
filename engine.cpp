#include <iostream>
#include <vector>
#include <string>

extern "C" {
    char world[20][20];

    void init_world() {
        for(int i=0; i<20; i++) {
            for(int j=0; j<20; j++) {
                if(i == 0 || i == 19 || j == 0 || j == 19) world[i][j] = '#'; 
                else world[i][j] = ' '; 
            }
        }
    }

    // Now accepts gx and gy to draw the goal
    void update_player(int x, int y, char icon, int gx, int gy) {
        init_world(); 
        
        // Draw the Goal first
        if(gx > 0 && gx < 19 && gy > 0 && gy < 19) {
            world[gy][gx] = 'X'; 
        }

        // Draw the Player (G)
        if(x > 0 && x < 19 && y > 0 && y < 19) {
            world[y][x] = icon;
        }
    }

    void render() {
        std::cout << "\033[H\033[J"; 
        std::string frame = "";
        for(int i=0; i<20; i++) {
            for(int j=0; j<20; j++) {
                frame += world[i][j];
                frame += ' '; 
            }
            frame += '\n';
        }
        std::cout << frame << std::flush;
    }
}
