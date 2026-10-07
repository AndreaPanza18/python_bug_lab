# 🐍 Python Bug Lab

Welcome to the **Python Bug Lab**!

The project contains a module (`app.py`) with **20 simple utility functions**, each containing one small, isolated bug. A full unit test suite (`test_app.py`) verifies the correct behavior.

---

## 🚀 Quickstart for Students

### 1. Run All Tests

To see the current status of all 20 exercises, run from the project root:

```bash
python -m unittest test_app.py
```

*(All 20 tests will initially fail or report errors because the bugs are waiting to be solved!)*

### 2. Run a Single Test

To test only the specific bug you are working on (e.g. Bug #01):

```bash
python -m unittest test_app.TestBugLab.test_bug_01
```

---

## 📋 The 20 Bugs Catalog

| Bug ID | Function | Category | Symptom | Test Command |
| :---: | :--- | :--- | :--- | :--- |
| **#01** | `is_even()` | Math | Erroneously checks `n % 2 == 1`, fails for negative evens | `python -m unittest test_app.TestBugLab.test_bug_01` |
| **#02** | `clamp_number()` | Math | Inverted bounds check: returns `max_val` when too small | `python -m unittest test_app.TestBugLab.test_bug_02` |
| **#03** | `discount_price()` | Math | Returns the discount amount instead of discounted price | `python -m unittest test_app.TestBugLab.test_bug_03` |
| **#04** | `find_max_number()` | Math | Initializes max to `0`, fails when all numbers are negative | `python -m unittest test_app.TestBugLab.test_bug_04` |
| **#05** | `calculate_bmi()` | Math | Forgets to square the height | `python -m unittest test_app.TestBugLab.test_bug_05` |
| **#06** | `is_palindrome()` | Strings | Fails on mixed-case words like `"Racecar"` | `python -m unittest test_app.TestBugLab.test_bug_06` |
| **#07** | `count_vowels()` | Strings | Missing the letter `'u'` in vowels list | `python -m unittest test_app.TestBugLab.test_bug_07` |
| **#08** | `truncate_text()` | Strings | Appends `"..."` without subtracting 3, exceeding `max_len` | `python -m unittest test_app.TestBugLab.test_bug_08` |
| **#09** | `reverse_words()` | Strings | Reverses character stream instead of word order | `python -m unittest test_app.TestBugLab.test_bug_09` |
| **#10** | `get_file_extension()` | Strings | Returns full filename if no extension is present | `python -m unittest test_app.TestBugLab.test_bug_10` |
| **#11** | `get_top_students()` | Lists | Off-by-one slice: returns `n-1` students instead of `n` | `python -m unittest test_app.TestBugLab.test_bug_11` |
| **#12** | `remove_duplicates...()` | Lists | Uses `set()` which scrambles original element order | `python -m unittest test_app.TestBugLab.test_bug_12` |
| **#13** | `sum_even_numbers()` | Lists | Condition checks `n % 2 != 0`, summing odds instead | `python -m unittest test_app.TestBugLab.test_bug_13` |
| **#14** | `merge_two_dicts()` | Lists | Mutates `d1` in-place instead of returning a new dict | `python -m unittest test_app.TestBugLab.test_bug_14` |
| **#15** | `filter_positive_...()` | Lists | Uses `>= 0` instead of `> 0`, including zero | `python -m unittest test_app.TestBugLab.test_bug_15` |
| **#16** | `is_leap_year()` | Logic | Divisibility by 4 only; misses 100/400 century rule | `python -m unittest test_app.TestBugLab.test_bug_16` |
| **#17** | `calculate_average()` | Math | Crashes with `ZeroDivisionError` on empty list `[]` | `python -m unittest test_app.TestBugLab.test_bug_17` |
| **#18** | `is_valid_password...()` | Logic | Returns `True` when length is LESS than 8 | `python -m unittest test_app.TestBugLab.test_bug_18` |
| **#19** | `format_currency_usd()` | Logic | Formats with 1 decimal place (`$19.9`) instead of 2 | `python -m unittest test_app.TestBugLab.test_bug_19` |
| **#20** | `calculate_ticket_price()` | Logic | Condition charges adults senior rate ($7.0 instead of $12) | `python -m unittest test_app.TestBugLab.test_bug_20` |

---

## 🛠️ Detailed Bug Descriptions & Hints

### Bug #01: `is_even(n)`

- **Symptom**: Calling `is_even(4)` returns `False` and `is_even(-2)` returns `False`.
- **Expected**: Should return `True` for even integers and `False` for odd integers.
- **Hint**: Change `return n % 2 == 1` to `return n % 2 == 0`.

### Bug #02: `clamp_number(value, min_val, max_val)`

- **Symptom**: `clamp_number(5, 10, 20)` returns `20` instead of `10`.
- **Expected**: Numbers below `min_val` should clamp to `min_val`; numbers above `max_val` should clamp to `max_val`.
- **Hint**: Invert the returned values in the `if/elif` branches (`return min_val` when `value < min_val`).

### Bug #03: `discount_price(price, discount_percent)`

- **Symptom**: A \$100 item with a 20% discount returns \$20 instead of \$80.
- **Expected**: Should subtract the discount amount from the original price.
- **Hint**: Return `price - discount_amount`.

### Bug #04: `find_max_number(numbers)`

- **Symptom**: `find_max_number([-10, -5, -20])` returns `0`.
- **Expected**: The maximum of those numbers is `-5`.
- **Hint**: Initialize `current_max = numbers[0]` instead of `0`.

### Bug #05: `calculate_bmi(weight_kg, height_m)`

- **Symptom**: For weight 70kg and height 1.75m, calculates `40.0` instead of `22.86`.
- **Expected**: The BMI formula is `weight / (height ** 2)`.
- **Hint**: Make sure height is squared in the denominator.

### Bug #06: `is_palindrome(text)`

- **Symptom**: `"Racecar"` returns `False`.
- **Expected**: Palindromes should be case-insensitive.
- **Hint**: Apply `.lower()` to the cleaned string before comparing.

### Bug #07: `count_vowels(text)`

- **Symptom**: `count_vowels("umbrella")` returns `2` instead of `3`.
- **Expected**: English vowels are `a, e, i, o, u`.
- **Hint**: Add `'u'` and `'U'` to the `vowels` string.

### Bug #08: `truncate_text(text, max_len)`

- **Symptom**: `truncate_text("Hello World", 8)` produces `"Hello Wo..."` (11 chars).
- **Expected**: Total output length must equal `max_len` (8 chars: `"Hello..."`).
- **Hint**: Slice up to `max_len - 3` before appending `"..."`.

### Bug #09: `reverse_words(sentence)`

- **Symptom**: `"Hello World"` becomes `"dlroW olleH"`.
- **Expected**: Should become `"World Hello"`.
- **Hint**: Split the sentence into words with `.split()`, reverse the list of words, and re-join with `" ".join()`.

### Bug #10: `get_file_extension(filename)`

- **Symptom**: `get_file_extension("README")` returns `"README"`.
- **Expected**: Should return `""` (empty string) when there is no dot.
- **Hint**: Return `""` if `"." not in filename`.

### Bug #11: `get_top_students(grades, n)`

- **Symptom**: Asking for top 2 students returns only 1 student.
- **Expected**: Slicing should return `n` elements.
- **Hint**: Python slice `[:n]` is already exclusive of `n`, do not subtract 1!

### Bug #12: `remove_duplicates_preserve_order(items)`

- **Symptom**: Input `[3, 1, 2, 3, 2]` might return `[1, 2, 3]`.
- **Expected**: Output must maintain insertion order: `[3, 1, 2]`.
- **Hint**: Use a loop with a seen set: `seen = set()`, append to list if not in `seen`.

### Bug #13: `sum_even_numbers(numbers)`

- **Symptom**: `sum_even_numbers([1, 2, 3, 4, 5, 6])` returns `9` (1+3+5).
- **Expected**: Should sum `2 + 4 + 6 = 12`.
- **Hint**: Change `n % 2 != 0` to `n % 2 == 0`.

### Bug #14: `merge_two_dicts(d1, d2)`

- **Symptom**: Modifies the original dictionary `d1`.
- **Expected**: A pure function that returns a new dictionary without mutating `d1`.
- **Hint**: Use `{**d1, **d2}` or `d1.copy()`.

### Bug #15: `filter_positive_numbers(numbers)`

- **Symptom**: Input `[-3, 0, 5]` returns `[0, 5]`.
- **Expected**: Strictly positive numbers (`> 0`). Zero is neither positive nor negative.
- **Hint**: Change `n >= 0` to `n > 0`.

### Bug #16: `is_leap_year(year)`

- **Symptom**: Year 1900 returns `True`.
- **Expected**: Year 1900 is NOT a leap year (divisible by 100 but not by 400).
- **Hint**: `(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)`.

### Bug #17: `calculate_average(numbers)`

- **Symptom**: Calling `calculate_average([])` throws `ZeroDivisionError: division by zero`.
- **Expected**: Should return `0.0` when the list is empty.
- **Hint**: Add `if not numbers: return 0.0` before calculating the average.

### Bug #18: `is_valid_password_length(password)`

- **Symptom**: Password `"short"` returns `True`.
- **Expected**: Valid length is at least 8 characters.
- **Hint**: Return `len(password) >= 8`.

### Bug #19: `format_currency_usd(amount)`

- **Symptom**: Formats `19.9` as `"$19.9"`.
- **Expected**: Currency must show 2 decimal places: `"$19.90"`.
- **Hint**: Use formatting specifier `:.2f`.

### Bug #20: `calculate_ticket_price(age)`

- **Symptom**: Adults (age 30) are charged $7.0 instead of $12.0.
- **Expected**: Children (<12): $5.0; Seniors (>=65): $7.0; Adults (12-64): $12.0.
- **Hint**: Change `elif age < 65:` to `elif age >= 65:`.

---

## 🎯 Hands-on Lab 2 Instructions (Step-by-Step)

### Step 1: Fork & Issue Setup

1. Click **Fork** on the repository page to create a copy under your account.
2. Go to the **Issues** tab on your fork and click **New Issue**.
3. Create Issue #1 for Bug #01 (`is_even`) and Issue #2 for Bug #02 (`clamp_number`).
4. Assign both issues to yourself!

### Step 2: Create 'development' Branch & Clone in PyCharm

1. On GitHub, create a new branch called `development` from `main`.
2. Open PyCharm -> **Get from VCS** -> paste your fork URL -> click **Clone**.
3. In PyCharm's bottom-right status bar, click `main` -> select `origin/development` -> click **Checkout**.

### Step 3: Bug 1 - Local Merge in PyCharm

1. Fix Bug 1 in `app.py` and run:

   ```bash
   python -m unittest test_app.TestBugLab.test_bug_01
   ```

2. Press `Alt + 0` (Commit Window) -> write commit message: `fix: resolve bug 1 negative even parity in is_even` -> click **Commit**.
3. In the branch widget (bottom-right), click `main` -> **Checkout**.
4. Click the branch widget -> select `development` -> click **Merge into Current**.
5. Press `Ctrl + Shift + K` -> click **Push** to send `main` to GitHub!
6. Delete local `development` branch in PyCharm, and manually close Issue #1 on GitHub.

### Step 4: Bug 2 - Pull Request via GitHub

1. In PyCharm, create a new branch `fix/bug-02-clamp` from `main`.
2. Fix Bug 2 in `app.py` and run:

   ```bash
   python -m unittest test_app.TestBugLab.test_bug_02
   ```

3. Commit with: `fix: correct clamp bound checking (Closes #2)` and push to GitHub (`Ctrl + Shift + K`).
4. On GitHub, open a **Pull Request** from `fix/bug-02-clamp` into `main`.
5. Review the diff and click **Merge pull request**.
6. Verify on GitHub that Issue #2 is **automatically closed**!
7. In PyCharm, checkout `main` and click **Update Project** (`Ctrl + T`).
