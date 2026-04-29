"""
E-Engine Translation Layer
Converts Java code to C++ and vice versa
"""

import re

def java_to_cpp(java_code):
    """
    Basic conversion from Java to C++
    Handles simple classes, methods, variables
    """
    # Replace package with include (simplified)
    cpp_code = re.sub(r'package\s+[\w.]+;', '', java_code)

    # Replace public class with class
    cpp_code = re.sub(r'public\s+class\s+(\w+)', r'class \1', cpp_code)

    # Add public: after class declaration
    cpp_code = re.sub(r'(class\s+\w+\s*\{)', r'\1\npublic:', cpp_code)

    # Replace void main with int main
    cpp_code = re.sub(r'public\s+static\s+void\s+main\s*\([^)]*\)', 'int main()', cpp_code)

    # Replace System.out.println with cout
    cpp_code = re.sub(r'System\.out\.println\(([^)]+)\);', r'cout << \1 << endl;', cpp_code)

    # Add #include <iostream>
    if 'cout' in cpp_code and '#include <iostream>' not in cpp_code:
        cpp_code = '#include <iostream>\n' + cpp_code

    # Add using namespace std;
    if ('cout' in cpp_code or 'endl' in cpp_code) and 'using namespace std;' not in cpp_code:
        cpp_code = cpp_code.replace('#include <iostream>\n', '#include <iostream>\nusing namespace std;\n')

    # Replace String with string
    cpp_code = re.sub(r'\bString\b', 'string', cpp_code)

    return cpp_code

def cpp_to_java(cpp_code):
    """
    Basic conversion from C++ to Java
    Handles simple classes, functions
    """
    # Remove #include
    java_code = re.sub(r'#include\s*<[^>]+>', '', cpp_code)

    # Remove using namespace std;
    java_code = re.sub(r'using\s+namespace\s+std;', '', java_code)

    # Replace class with public class
    java_code = re.sub(r'class\s+(\w+)', r'public class \1', java_code)

    # Remove public: label
    java_code = re.sub(r'public:\s*', '', java_code)

    # Replace int main with public static void main
    java_code = re.sub(r'int\s+main\s*\([^)]*\)', 'public static void main(String[] args)', java_code)

    # Replace cout with System.out.println
    java_code = re.sub(r'cout\s*<<\s*([^<]+)\s*<<\s*endl;', r'System.out.println(\1);', java_code)

    # Replace string with String
    java_code = re.sub(r'\bstring\b', 'String', java_code)

    # Remove return 0; in main
    java_code = re.sub(r'return\s+0;\s*', '', java_code)

    # Remove trailing }; if it's for the class
    java_code = re.sub(r'\};\s*$', '', java_code)

    return java_code

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        direction = sys.argv[1]
        input_file = sys.argv[2] if len(sys.argv) > 2 else None
        if input_file:
            with open(input_file, 'r') as f:
                code = f.read()
        else:
            code = sys.stdin.read()
        
        if direction == 'java2cpp':
            result = java_to_cpp(code)
        elif direction == 'cpp2java':
            result = cpp_to_java(code)
        else:
            print("Usage: python translator.py <java2cpp|cpp2java> [input_file]")
            sys.exit(1)
        
        print(result)
    else:
        # Example usage
        java_example = """
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
"""

        cpp_result = java_to_cpp(java_example)
        print("Java to C++:")
        print(cpp_result)

        cpp_example = """
#include <iostream>
using namespace std;

class HelloWorld {
public:
    void sayHello() {
        cout << "Hello, World!" << endl;
    }
};

int main() {
    HelloWorld hw;
    hw.sayHello();
    return 0;
}
"""

        java_result = cpp_to_java(cpp_example)
        print("\nC++ to Java:")
        print(java_result)
