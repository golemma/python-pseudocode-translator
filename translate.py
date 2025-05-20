#this is a test comment to see how github works

def translate_line(line):
    stripped = line.strip()
    if stripped.startswith("def"):
        name = stripped.split()[1].split("(")[0]
        return f"Define function {name}"
    elif stripped.startswith("for"):
        return "Loop: " + stripped
    elif stripped.startswith("if"):
        return "If condition: " + stripped
    elif "print(" in stripped:
        start = stripped.find("print(") + 6
        end = stripped.rfind(")")
        return "Output: " + stripped[start:end]
    else:
        return "Do: " + stripped

def translate_file(input_path, output_path):
    print(f"Translating from: {input_path}")
    print(f"Output file: {output_path}")
    with open(input_path) as f_in, open(output_path, "w") as f_out:
        prev_indent = 0
        for line in f_in:
            # Count leading spaces (assuming 4 spaces per indent level)
            indent = (len(line) - len(line.lstrip(' '))) // 4
            pseudo = translate_line(line)
            # Indent pseudocode to match Python code structure
            f_out.write('    ' * indent + pseudo + '\n')

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python translate.py input.py output.txt")
    else:
        translate_file(sys.argv[1], sys.argv[2])
