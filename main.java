import javax.swing.*;
import java.awt.*;

public class Main {
    public static void main(String[] args) {
        // --- 1. WINDOW SETUP ---
        JFrame frame = new JFrame("E-Engine");
        frame.setSize(1200, 800);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        Color editorColor = Color.decode("#3D3838");
        JPanel rootPanel = new JPanel(new BorderLayout());
        rootPanel.setBackground(editorColor);

        // --- 2. SIDEBAR (Hierarchy) ---
        JPanel sidebar = new JPanel();
        sidebar.setPreferredSize(new Dimension(250, 0)); // Fixed spelling
        sidebar.setBackground(new Color(45, 45, 45)); 
        sidebar.setBorder(BorderFactory.createMatteBorder(0, 0, 0, 1, Color.BLACK));
        
        // --- 3. VIEWPORT (The C++ Rendering will show up here) ---
        JPanel viewport = new JPanel();
        viewport.setBackground(editorColor); 
        viewport.add(new JLabel("Viewport Area")).setForeground(Color.LIGHT_GRAY);

        // --- 4. BOTTOM BAR (Console) ---
        JPanel bottomBar = new JPanel();
        bottomBar.setPreferredSize(new Dimension(0, 150));
        bottomBar.setBackground(new Color(30, 30, 30));
        bottomBar.setBorder(BorderFactory.createMatteBorder(1, 0, 0, 0, Color.BLACK));

        // --- 5. THE BRIDGE (Where Java talks to C++) ---
        // PASTE YOUR "TALKING" CODE RIGHT HERE LATER:
        System.out.println("Connecting to C++ Engine..."); 

        // --- 6. ASSEMBLE ---
        rootPanel.add(sidebar, BorderLayout.WEST);
        rootPanel.add(viewport, BorderLayout.CENTER);
        rootPanel.add(bottomBar, BorderLayout.SOUTH);

        frame.add(rootPanel);
        frame.setLocationRelativeTo(null); // Fixed spelling
        try {
    // This tells Java to run your C++ Engine executable
    Runtime.getRuntime().exec("./EEngine.exe"); 
    System.out.println("C++ Engine Started!");
} catch (Exception e) {
    System.out.println("Could not find EngineCore. Build it first!");
}
        frame.setVisible(true);
    }
}