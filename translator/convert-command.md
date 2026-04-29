### Usage
Run the translator with examples:
```bash
python src/translator.py
```

Convert a file:
```bash
python src/translator.py java2cpp input.java > output.cpp
python src/translator.py cpp2java input.cpp > output.java
```

Or from stdin:
```bash
echo "public class Test {}" | python src/translator.py java2cpp
```



## Translation Layer
This project includes a basic translation layer to convert Java code to C++ and vice versa. This allows developers to write code in either language for the game engine.

### Features
- Basic Java to C++ conversion (classes, main method, print statements)
- Basic C++ to Java conversion
- Supports simple syntax transformations



