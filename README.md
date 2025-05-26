# Turing Machine – Binary Real Number Addition

## Project Purpose & Explanation

This project explores the capabilities and limitations of Turing machines in simulating arithmetic operations on binary real numbers using a **deterministic, single tape, one-way infinite machine**. Specifically, it demonstrates how a classical model of computation can be used to perform **fixed point binary addition**, a task typically handled by modern digital hardware or high level programming languages.

The input format requires parsing and aligning binary real numbers with fractional parts, managing carry propagation across the decimal point, and handling formatting constraints, all within the bounds of the Turing machine model. This highlights both the power and complexity of using Turing machines for practical computation. Designing such a machine encourages thinking in terms of pure computation theory rather than traditional programming constructs.

## Input/Output Generation with Python

To support this project and ensure correctness, the repository includes a utility script:

### `BinaryNumberGenerator.py`

This Python file automates the process of:

- Generating valid binary real number pairs `X#Y` in the correct format
- Computing the **expected output** of `X + Y` using precise decimal arithmetic
- Verifying the correctness of the Turing machine by comparing its output to the Python-generated ground truth

The generator uses fixed point binary to decimal conversion with Python’s `decimal.Decimal` for high precision results, followed by a custom binary encoder to produce outputs in the same format expected from the Turing machine.

This script is especially useful for:

- Creating random test cases with varying lengths and precision
- Rapidly testing the Turing machine’s behavior under many scenarios
- Debugging edge cases, such as carries across the decimal point or formatting boundary conditions

  
## This is a picture of my implementation if you do not have JFLAP. - Rick Kabuto
<img width="1343" alt="Screenshot 2025-05-04 at 6 10 35 PM" src="https://github.com/user-attachments/assets/6df13e72-2ae6-4c84-bba4-a63fee4c81f9" />

## Project Directions From The Class 

Construct a Turing machine that adds two binary real numbers. An input will be of the form:

X#Y

Where:

- `X` and `Y` are elements of `{0, 1}+.{0, 1}+`
- `X = xₙxₙ₋₁...x₁x₀.x₋₁x₋₂...x₋ₖ`
- `Y = yₘyₘ₋₁...y₁y₀.y₋₁y₋₂...y₋ₗ`

With:
1) X = (xₙ × 2ⁿ) + (xₙ₋₁ × 2ⁿ⁻¹) + ... + (x₁ × 2¹) + (x₀ × 2⁰) + (x₋₁ × 2⁻¹) + ... + (x₋ₖ × 2⁻ᵏ)
2) Y = (yₘ × 2ᵐ) + (yₘ₋₁ × 2ᵐ⁻¹) + ... + (y₁ × 2¹) + (y₀ × 2⁰) + (y₋₁ × 2⁻¹) + ... + (y₋ₗ × 2⁻ˡ)

Your Turing machine must be a single-tape, one-way infinite, deterministic Turing machine.

## Output Format

When the Turing machine completes:

- The tape should contain `Z`, where `Z = X + Y`
- The original input `X#Y` may remain on the tape
- The read/write head must be positioned at the **leftmost symbol of `Z`**

### Formatting Rules

- No leading `0`s to the left of the decimal point unless `Z < 1`
  - Invalid: `01.0`  
  - Valid: `0.1`, `0.0`
- No trailing `0`s to the right of the decimal point unless `Z` is an integer
  - Invalid: `1.10`  
  - Valid: `1.0`, `2.0`

To handle formatting:
- To remove **trailing zeros**, move right to the end of `Z`, then move left over `0`s, replacing them with blank spaces until a `1` or a decimal is reached. If a decimal is reached, write a single `0` to its right.
- To remove **leading zeros**, move right until a `1` or decimal is seen. If a decimal is found first, move back left.

## Input Alphabet - { 0, 1, ., # }
## Tape Alphabet - { 0, 1, ., x, a, b, #, $, ␣ }

## Example Input/Output
### Input 
111100101101101.01011100010001101001011#1010111010110001.0110011010110010010111
### Output
10010100000011110.11000010111110001111001


(The head will be placed at the leftmost digit of this output.)

## Constraints

- The machine must be **deterministic**, **single-tape**, **one-way infinite**
- Transitions may:
  - Move Left (L), Right (R), or Stay (S)
  - Use `~` as a wildcard match
- Transitions **must** read/write a single symbol per step
- Transitions like `({a,b,c}w; w, R)` are **not allowed**
- **Blank space to the left of the input may not be used**

## Implementation Notes

- You may use modular blocks to organize your logic
- Each block may handle sub-operations like formatting, padding, or addition
- The output must be aligned and cleaned per the rules above



