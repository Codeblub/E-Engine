#include <SFML/Graphics.hpp>
#include <iostream>

int main() {
    // 1. Create the Window (Corrected spelling: VideoMode)
    sf::RenderWindow window(sf::VideoMode(1200, 800), "E-Engine Core");

    // 2. Set your background color (#3D3838 in RGB)
    sf::Color editorGrey(61, 56, 56);

    std::cout << "C++ Engine Core is running..." << std::endl;

    // 3. The Main Engine Loop
    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            // Close window if user clicks 'X'
            if (event.type == sf::Event::Closed)
                window.close();
        }

        // --- RENDER START ---
        window.clear(editorGrey);

        // This is where you will eventually add:
        // drawGrid();
        // draw3DModels();

        window.display();
        // --- RENDER END ---
    }

    return 0;
}