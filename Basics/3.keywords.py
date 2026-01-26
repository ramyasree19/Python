"""3.keywords.py

Short, runnable reference for Python keywords.

- Prints the current keyword list (from the standard library `keyword` module).
- Shows how to check whether a name is a keyword.
- Provides categorized keyword lists and short usage tips.

Note: Using a Python keyword as an identifier (variable / function / class name)
will raise a SyntaxError. Prefer appending an underscore (e.g. `class_`) or
choose a different name.
"""

import keyword
import textwrap

# A small manual categorization for quick reference (not exhaustive).
KEYWORD_CATEGORIES = {
    "Values": ["True", "False", "None"],
    "Operators / Logic": ["and", "or", "not", "is", "in"],
    "Control flow": ["if", "else", "elif", "for", "while", "break", "continue", "pass"],
    "Exceptions / Error handling": ["try", "except", "finally", "raise", "assert"],
    "Functions & classes": ["def", "return", "lambda", "yield", "class"],
    "Context management": ["with", "as"],
    "Imports": ["import", "from"],
    "Scope": ["global", "nonlocal"],
    "Async": ["async", "await"],
}


def print_header(title: str):
    print(f"\n{title}")
    print("-" * len(title))


def show_keyword_list():
    print_header("Python keywords (from keyword.kwlist)")
    kws = keyword.kwlist
    print("Total:", len(kws))
    # print in columns
    cols = 4
    rows = (len(kws) + cols - 1) // cols
    for r in range(rows):
        row_items = []
        for c in range(cols):
            i = r + c * rows
            if i < len(kws):
                row_items.append(f"{kws[i]:<10}")
        print("  ".join(row_items))


def show_categories():
    print_header("Common keyword categories (quick reference)")
    for cat, items in KEYWORD_CATEGORIES.items():
        print(f"{cat}: {', '.join(items)}")


def demonstrate_checks_and_patterns():
    print_header("Checks & safe identifier patterns")
    names = ["if", "lambda", "my_var", "class"]
    for name in names:
        print(f"Is '{name}' a keyword? -> {keyword.iskeyword(name)}")

    print()
    print("Safe alternatives:")
    examples = {
        "class": "class_  # append underscore to avoid SyntaxError",
        "if": "if_cond or condition_if",
        "lambda": "use a named function or lambda_",
    }
    for k, v in examples.items():
        print(f"- {k}: {v}")

    print()
    print(textwrap.fill(
        "Remember: using a reserved keyword as a variable or function name causes a SyntaxError. "
        "When you need a similar name, append an underscore (e.g. `class_`) or rename for clarity.",
        width=80,
    ))


if __name__ == '__main__':
    show_keyword_list()
    show_categories()
    demonstrate_checks_and_patterns()

    print_header('Quick note')
    print('SyntaxError example (do not run):')
    print("  # def = 5  # invalid — 'def' is a keyword")
    print('\nTip: use keyword.iskeyword(name) to guard dynamic identifier creation.')
