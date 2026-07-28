# Lightning McQueen's To-Do List

TASK 3 MIA 

## Running it

```bash
python3 mcqueen_todo.py
```

Requires Python 3. No packages to install.

## What it does

On start, it greets McQueen and loops on a menu until he quits:

```
1. Add a task
2. View my to-do list
3. Mark a task as done
4. Remove a task
5. Quit
```


## Data model

Tasks are stored as a plain Python list of dicts, held only in memory (nothing is saved to disk — the list resets every time you run the program):

```python
{"name": "Get new tires from Luigi", "done": False}
```

- `name` — the task text as typed in.
- `done` — `True`/`False`, flipped by the "mark as done" option.

## Function breakdown

| Function | Responsibility |
|---|---|
| `print_menu()` | Prints the header and the 5 menu options. Pure display, no logic. |
| `add_task(tasks)` | Prompts for task text, rejects blank/whitespace-only input, appends a new task dict, confirms. |
| `view_tasks(tasks)` | Prints every task with a `[DONE]` or `[PENDING]` tag. Handles the empty-list case separately. |
| `get_task_index(tasks, prompt)` | Shared helper used by both "complete" and "remove". Shows the list, asks for a task number, validates it's a real number and in range, and returns a 0-based index (or `None` if invalid). This is the single place that handles the 1-indexed-for-humans vs 0-indexed-for-Python conversion, so both features stay consistent. |
| `complete_task(tasks)` | Uses `get_task_index` to pick a task, flips `done` to `True`, confirms. Warns (doesn't error) if it's already done. |
| `remove_task(tasks)` | Uses `get_task_index` to pick a task, `.pop()`s it out, confirms what was removed. |
| `main()` | The loop: print menu, read choice, dispatch to the matching function, repeat until "5" is chosen. |
- **No editing.** Tasks can be added, completed, or removed, but not renamed.

These were left out because the spec didn't ask for them — flagging them here in case a future version needs to extend the program.
