# Count lines in a file
def count_lines(input_path):
    with open(input_path, "r") as f:
        return sum(1 for _ in f)


# Extract the first N lines
def extract_first_lines(input_path, n=2):
    first_lines = []

    with open(input_path, "r") as f:
        for i, line in enumerate(f):
            if i >= n:
                break
            first_lines.append(line)

    return first_lines


# Write extracted lines to a new file
def write_lines(output_path, lines):
    with open(output_path, "w") as f:
        f.writelines(lines)


# Main program
if __name__ == "__main__":

    input_path = "input.txt"
    output_path = "output_first_two_lines.txt"

    # Create sample input file
    sample_content = (
        "Monday: Team stand-up at 9:00 AM\n"
        "Tuesday: Client review meeting\n"
        "Wednesday: Code review session\n"
        "Thursday: Sprint planning\n"
        "Friday: Deployment and retrospective\n"
    )

    with open(input_path, "w") as f:
        f.write(sample_content)

    print(f"Created sample input file: {input_path}\n")

    # Step 1: Count lines
    total_lines = count_lines(input_path)
    print(f"Total number of lines in '{input_path}': {total_lines}")

    # Step 2: Extract first two lines
    first_two = extract_first_lines(input_path, n=2)

    print("\nFirst two lines extracted:")
    for line in first_two:
        print(f"  {line.rstrip()}")

    # Step 3: Write extracted lines to new file
    write_lines(output_path, first_two)

    print(f"\nExtracted lines written to: {output_path}")

    # Verify output file
    print(f"\nContents of '{output_path}':")

    with open(output_path, "r") as f:
        print(f.read())
