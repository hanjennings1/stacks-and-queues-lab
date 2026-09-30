# Lab: Stacks and Queues  
**Completed Sept 30, 2026**

---

# Stacks and Queues Lab

This project uses two basic data structures to solve two small, real-world problems:

- A **stack** (last in, first out) checks whether brackets in a string are balanced, the same kind of check code editors and compilers run on your code.
- A **queue** (first in, first out) runs a customer raffle. Customers are kept in the order they arrived, a random winner is picked, and everyone up to and including the winner is removed from the line.

## How to Run

This project uses only Python's standard library, so there's nothing to install.

1. Clone the repository and move into the project folder:

```
   git clone https://github.com/hanjennings1/stacks-and-queues-lab.git
   cd stacks-and-queues-lab
```

2. Run the tests:

```
   python test_structures.py
```

   On some systems you may need `python3` instead of `python`.

The test output shows each step: the customers in the queue, the raffle winner, the customers still in line, and the result of each bracket check. All 5 tests pass.

## Project Files

- `custom_stack.py` contains `is_valid_parentheses(s)`, which uses a stack to check that `()`, `[]`, and `{}` are balanced and correctly nested.
- `custom_queue.py` contains the `Queue` class with `enqueue`, `dequeue`, `peek`, `is_empty`, and `select_and_announce_winner`.
- `test_structures.py` contains the unit tests for both files.

## How It Works

### Balanced brackets (stack)

The function reads the string one character at a time. Each opening bracket is added to the top of the stack. When a closing bracket appears, the function removes the top item from the stack and checks that it's the matching opener. The string is invalid if a closing bracket has nothing to match, if it's matched with the wrong opener, or if any opening brackets are left over at the end.

For example, `{[()]}` is valid because each pair is fully nested inside the next. `([)]` is invalid even though every bracket has a partner, because the `[` was opened last but the `)` tries to close first.

### Customer raffle (queue)

Customers join the back of the line with `enqueue` and leave from the front with `dequeue`. `select_and_announce_winner` picks a random customer who is currently in line, then removes customers from the front one at a time until the winner has been removed. It prints and returns the winner's name, and everyone who was behind the winner stays in line.

For example, if Customer #4 wins in a line of 20, customers #1 through #4 are removed, and #5 through #20 remain.

## Built With

- Python 3
- `unittest` and `random` from the standard library