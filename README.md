# Growing Code — Python 00

> Python fundamentals through community garden data. Seven small exercises
> covering printing, input, integer conversion, conditionals, loops,
> recursion, and type annotations.

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Prerequisites](#2-prerequisites)
3. [Directory Structure](#3-directory-structure)
4. [Setup](#4-setup)
5. [How to Test Your Functions](#5-how-to-test-your-functions)
6. [How to Check Style and Types](#6-how-to-check-style-and-types)
7. [Exercise Overview](#7-exercise-overview)
8. [Verification Checklist](#8-verification-checklist)
9. [Troubleshooting](#9-troubleshooting)

---

## 1. Project Overview

This repository contains the solutions for **Growing Code (Python 00)**, an
introductory Python project. Each exercise is a single function placed in its
own `exN/` directory. The functions handle their own input and output — there
are no `main` programs and no calls to the functions inside the solution files
(a provided `main.py` helper is used for testing).

Core concepts covered, one per exercise:

- **ex0** — calling `print()` (output only)
- **ex1** — reading user input with `input()`
- **ex2** — converting strings to integers with `int()` and doing arithmetic
- **ex3** — combining several inputs into a total
- **ex4** — making a decision with `if` / `else`
- **ex5** — another `if` / `else` with a boundary condition
- **ex6** — repetition two ways: an iterative loop and a recursive function
- **ex7** — type annotations (checked with `mypy`) and an `if`/`elif`/`else` chain

---

## 2. Prerequisites

| Tool   | Minimum Version | Notes                                            |
|--------|-----------------|--------------------------------------------------|
| Python | 3.10+           | Required by the project (uses 3.10+ syntax)      |
| flake8 | any recent      | Style/linter check for every file                |
| mypy   | any recent      | Type check — required for ex7                    |

Verify your environment:

```bash
python3 --version    # should be 3.10 or higher
flake8 --version
mypy --version
```

If `flake8` or `mypy` report "command not found", see
[Troubleshooting](#9-troubleshooting).

---

## 3. Directory Structure

```
Python-00/
├── README.md
├── main.py                              # provided test helper (not submitted)
├── ex0/
│   └── ft_hello_garden.py
├── ex1/
│   └── ft_garden_name.py
├── ex2/
│   └── ft_plot_area.py
├── ex3/
│   └── ft_harvest_total.py
├── ex4/
│   └── ft_plant_age.py
├── ex5/
│   └── ft_water_reminder.py
├── ex6/
│   ├── ft_count_harvest_iterative.py
│   └── ft_count_harvest_recursive.py
└── ex7/
    └── ft_seed_inventory.py
```

Each solution file contains **only** the requested function — no top-level
calls, no `if __name__ == "__main__":` block, no code outside the function.

---

## 4. Setup

The tools (`flake8`, `mypy`) only need to be available on your PATH. One clean
way that works across all your Python modules without reinstalling each time:

```bash
# Install pipx once (system package), then the tools globally
sudo apt install pipx
pipx ensurepath          # then restart your terminal
pipx install flake8
pipx install mypy
```

After this, `flake8` and `mypy` work in any folder with no activation step.

> If you prefer a per-project virtual environment instead:
> ```bash
> python3 -m venv venv
> source venv/bin/activate
> pip install flake8 mypy
> ```
> Remember to add `venv/` to `.gitignore` so it is never committed.

---

## 5. How to Test Your Functions

The provided `main.py` imports and runs your functions. It expects the file it
is testing to be reachable from where you run it. The simplest approach is to
test from inside each exercise folder:

```bash
cd ex6
cp ../main.py .          # bring the helper next to the files being tested
python3 main.py          # follow the menu, enter a NUMBER when prompted
```

You can also run a single function directly, without the menu:

```bash
cd ex2
python3 -c "from ft_plot_area import ft_plot_area; ft_plot_area()"
```

> When a prompt asks for a number (e.g. "Days until harvest:"), type a plain
> number like `5`. Typing text causes `invalid literal for int()` — that is
> expected; the project does not require handling invalid input.

---

## 6. How to Check Style and Types

**Style (flake8)** — run on every file. No output means the file is clean:

```bash
flake8 ex0/ft_hello_garden.py
flake8 ex1/ft_garden_name.py
# ... and so on for each file
```

Check all files at once:

```bash
flake8 ex*/*.py
```

**Types (mypy)** — required for ex7:

```bash
mypy ex7/ft_seed_inventory.py
```

A clean run prints nothing (or `Success: no issues found`).

<!-- > **Style note:** flake8 expects **4 spaces** for indentation, never tabs
> (`W191`). If you are coming from the 42 C norm (which uses tabs), configure
> your editor to insert spaces for Python. In VS Code, create
> `.vscode/settings.json`:
> ```json
> {
>     "[python]": {
>         "editor.insertSpaces": true,
>         "editor.tabSize": 4,
>         "editor.detectIndentation": false
>     }
> } -->
> ```
> To fix a file that already has tabs: Command Palette →
> "Convert Indentation to Spaces".

---

## 7. Exercise Overview

Each entry below states the **required behaviour** (per the project spec) so you
can confirm your output matches exactly. Output is compared character-for-
character, so capitalization and punctuation matter.

### ex0 — `ft_hello_garden`
Prints a fixed welcome line.
```
Hello, Garden Community!
```

### ex1 — `ft_garden_name`
Asks for a garden name, then prints it with a fixed status line.
```
Enter garden name: Community Garden
Garden: Community Garden
Status: Growing well!
```

### ex2 — `ft_plot_area`
Asks for length and width, prints their product.
```
Enter length: 5
Enter width: 3
Plot area: 15
```

### ex3 — `ft_harvest_total`
Asks for three daily harvests, prints the sum.
```
Day 1 harvest: 5
Day 2 harvest: 8
Day 3 harvest: 3
Total harvest: 16
```

### ex4 — `ft_plant_age`
Ready to harvest only when age is **strictly more than 60** (`> 60`).
```
Enter plant age in days: 75
Plant is ready to harvest!
```
```
Enter plant age in days: 45
Plant needs more time to grow.
```

### ex5 — `ft_water_reminder`
Water only when days since watering is **more than 2** (`> 2`). Note the
second message has **no** trailing punctuation.
```
Days since last watering: 4
Water the plants!
```
```
Days since last watering: 1
Plants are fine
```

### ex6 — `ft_count_harvest_iterative` and `ft_count_harvest_recursive`
Both count from 1 to n and then print a final line. Identical output.
```
Days until harvest: 5
Day 1
Day 2
Day 3
Day 4
Day 5
Harvest time!
```
The recursive version reads input once in the outer function and uses a helper
(nested function, default parameter, or separate function) to do the counting.

### ex7 — `ft_seed_inventory`
Takes arguments directly (no `input()`). Required signature:
```python
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
```
Capitalizes the seed type and branches on `unit`:
```
ft_seed_inventory("tomato", 15, "packets")  -> Tomato seeds: 15 packets available
ft_seed_inventory("carrot", 8, "grams")     -> Carrot seeds: 8 grams total
ft_seed_inventory("lettuce", 12, "area")    -> Lettuce seeds: covers 12 square meters
```
Any other unit prints only:
```
Unknown unit type
```

---

## 8. Verification Checklist

Run this before submitting. It checks every file for style and type-checks
ex7. If it prints `ALL CLEAN`, everything passed:

```bash
flake8 ex*/*.py && mypy ex7/*.py && echo "ALL CLEAN"
```

Manual checklist:

- [ ] Every file contains **only** the requested function (no extra calls)
- [ ] Indentation is 4 spaces, not tabs
- [ ] Function names match the spec exactly
- [ ] Output matches the expected text exactly (caps, spaces, punctuation)
- [ ] ex4 uses `> 60` (strictly more than); day 60 is *not* ready
- [ ] ex5 uses `> 2`; day 2 prints `Plants are fine` (no period)
- [ ] ex6 iterative and recursive produce identical output
- [ ] ex7 uses the exact typed signature and passes `mypy`
- [ ] `flake8 ex*/*.py` prints nothing

---

## 9. Troubleshooting

### `flake8: command not found` (or `mypy: command not found`)
Cause: The tool is not on your PATH — usually a virtual environment that is not
activated, or pipx's path not yet picked up.

Fix: If using a venv, run `source venv/bin/activate` (and confirm with
`which python3`). If using pipx, run `pipx ensurepath` and restart the terminal.
As a fallback, call the tool through Python: `python3 -m flake8 yourfile.py`.

### `W191 indentation contains tabs`
Cause: The file uses tab characters for indentation; Python style wants spaces.

Fix: Configure your editor to insert 4 spaces for Python (see the style note in
[Section 6](#6-how-to-check-style-and-types)), then convert the existing file's
indentation to spaces.

### `E302 expected 2 blank lines, got 1`
Cause: A top-level function needs two blank lines before it when preceded by
code. (A header comment at the very top of the file may not trigger this.)

Fix: Add a blank line so there are two before the `def`.

### `invalid literal for int() with base 10: '...'`
Cause: Text was entered where a number was expected (e.g. a menu label fed into
an `input()` prompt).

Fix: Enter a plain number at numeric prompts. The project does not require
handling invalid input, so this is expected behaviour, not a code bug.

### `main.py` reports "Could not find <file>"
Cause: `main.py` looks for the exercise file in its own folder, but the file is
in an `exN/` subfolder.

Fix: Copy `main.py` into the exercise folder and run it there
(`cd ex6 && cp ../main.py . && python3 main.py`), or run the function directly
with `python3 -c "from <module> import <func>; <func>()"`.

---

> **Note:** The check commands in this README have not been run for you —
> run Section 8's verification yourself to confirm a clean state before
> submitting. The project evaluates the code in your repository, so make sure
> your latest work is committed and pushed.