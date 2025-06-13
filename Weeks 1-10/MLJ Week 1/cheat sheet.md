## 🛠️ Python Condition Toolkit (Cheat-Sheet)

took this word for word, bar for bar from chatgpt.
### 1. Essential Patterns
| Syntax | Meaning | Example |
|--------|---------|---------|
| `a <= x <= b` | `x` is between `a` and `b` (inclusive) | `1 <= x <= 12` |
| `not expr` | logical NOT | `if not items:` |
| `expr1 and expr2` / `expr1 or expr2` | logical AND / OR (short-circuit) | `if hungry and food:` |
| `value in seq` / `value not in seq` | membership test | `"@" in email` |
| `obj is other` / `obj is not other` | identity (same object) | `if value is None:` |
| `==` / `!=` | equality / inequality | `if guess != secret:` |
| `any(iterable)` | True if **any** element is truthy | `any(errors)` |
| `all(iterable)` | True if **all** elements are truthy | `all(nums)` |
| `a if cond else b` | ternary/inline if-else | `status = "ok" if ok else "fail"` |

### 2. Quick Gotchas
- **Chained comparisons** (`a < b < c`) are atomic; `b` is evaluated only once.
- `and` / `or` **return the last evaluated operand**, e.g. `result = user_input or default`.
- **Falsy values** → `0, 0.0, "", [], {}, set(), None`; almost everything else is truthy.
- Use `is` **only** for singletons (`None`, `True`, `False`) or explicit identity checks.
- Mix `and` & `or`? Add **parentheses** for clarity:  
  ```python
  if (logged_in and admin) or superuser:
      ...
