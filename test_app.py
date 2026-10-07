"""
test_app.py - Test Suite for Python Bug Lab

Run all tests:
    python -m unittest test_app.py

Run a single test (e.g. for Bug #01):
    python -m unittest test_app.TestBugLab.test_bug_01
"""

import unittest
from app import (
    is_even,
    clamp_number,
    discount_price,
    find_max_number,
    calculate_bmi,
    is_palindrome,
    count_vowels,
    truncate_text,
    reverse_words,
    get_file_extension,
    get_top_students,
    remove_duplicates_preserve_order,
    sum_even_numbers,
    merge_two_dicts,
    filter_positive_numbers,
    is_leap_year,
    calculate_average,
    is_valid_password_length,
    format_currency_usd,
    calculate_ticket_price
)

class TestBugLab(unittest.TestCase):

    # --- Category 1: Math & Statistics ---

    def test_bug_01(self):
        """Bug #01: is_even should return True for even numbers and False for odd numbers."""
        self.assertTrue(is_even(4))
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(-2))
        self.assertFalse(is_even(7))
        self.assertFalse(is_even(-3))

    def test_bug_02(self):
        """Bug #02: clamp_number should constrain values to min_val and max_val."""
        self.assertEqual(clamp_number(5, 10, 20), 10)
        self.assertEqual(clamp_number(25, 10, 20), 20)
        self.assertEqual(clamp_number(15, 10, 20), 15)

    def test_bug_03(self):
        """Bug #03: discount_price should return the final discounted price."""
        self.assertAlmostEqual(discount_price(100.0, 20.0), 80.0)
        self.assertAlmostEqual(discount_price(50.0, 10.0), 45.0)

    def test_bug_04(self):
        """Bug #04: find_max_number should correctly identify max in negative lists."""
        self.assertEqual(find_max_number([1, 5, 3]), 5)
        self.assertEqual(find_max_number([-10, -5, -20]), -5)

    def test_bug_05(self):
        """Bug #05: calculate_bmi should square the height."""
        # 70 / (1.75 ** 2) = ~22.86
        self.assertAlmostEqual(calculate_bmi(70, 1.75), 22.86, places=2)

    # --- Category 2: Strings & Text Processing ---

    def test_bug_06(self):
        """Bug #06: is_palindrome should be case-insensitive."""
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("Racecar"))
        self.assertFalse(is_palindrome("python"))

    def test_bug_07(self):
        """Bug #07: count_vowels should count all vowels including 'u'."""
        self.assertEqual(count_vowels("umbrella"), 3) # u, e, a
        self.assertEqual(count_vowels("sky"), 0)

    def test_bug_08(self):
        """Bug #08: truncate_text should not exceed max_len."""
        truncated = truncate_text("Hello World", 8)
        self.assertEqual(truncated, "Hello...")
        self.assertEqual(len(truncated), 8)
        self.assertEqual(truncate_text("Short", 10), "Short")

    def test_bug_09(self):
        """Bug #09: reverse_words should reverse word order, not characters."""
        self.assertEqual(reverse_words("Hello World"), "World Hello")
        self.assertEqual(reverse_words("Git and GitHub"), "GitHub and Git")

    def test_bug_10(self):
        """Bug #10: get_file_extension should return empty string for files without extension."""
        self.assertEqual(get_file_extension("main.py"), "py")
        self.assertEqual(get_file_extension("README"), "")

    # --- Category 3: Lists & Collections ---

    def test_bug_11(self):
        """Bug #11: get_top_students should return exactly n students."""
        students = ["Alice", "Bob", "Charlie", "David"]
        self.assertEqual(get_top_students(students, 2), ["Alice", "Bob"])

    def test_bug_12(self):
        """Bug #12: remove_duplicates_preserve_order should maintain initial order."""
        self.assertEqual(remove_duplicates_preserve_order([3, 1, 2, 3, 2, 4]), [3, 1, 2, 4])

    def test_bug_13(self):
        """Bug #13: sum_even_numbers should sum even numbers only."""
        self.assertEqual(sum_even_numbers([1, 2, 3, 4, 5, 6]), 12)

    def test_bug_14(self):
        """Bug #14: merge_two_dicts should not modify input dictionary d1."""
        d1 = {"a": 1}
        d2 = {"b": 2}
        result = merge_two_dicts(d1, d2)
        self.assertEqual(result, {"a": 1, "b": 2})
        self.assertEqual(d1, {"a": 1}) # d1 must remain intact!

    def test_bug_15(self):
        """Bug #15: filter_positive_numbers should exclude zero."""
        self.assertEqual(filter_positive_numbers([-3, 0, 5, -1, 10]), [5, 10])

    # --- Category 4: Logic & Validation ---

    def test_bug_16(self):
        """Bug #16: is_leap_year should follow 100/400 century rules."""
        self.assertTrue(is_leap_year(2024))
        self.assertTrue(is_leap_year(2000))
        self.assertFalse(is_leap_year(1900))
        self.assertFalse(is_leap_year(2023))

    def test_bug_17(self):
        """Bug #17: calculate_average should handle empty lists without ZeroDivisionError."""
        self.assertEqual(calculate_average([10, 20, 30]), 20.0)
        self.assertEqual(calculate_average([]), 0.0)

    def test_bug_18(self):
        """Bug #18: is_valid_password_length should require at least 8 characters."""
        self.assertFalse(is_valid_password_length("short"))
        self.assertTrue(is_valid_password_length("longenough123"))

    def test_bug_19(self):
        """Bug #19: format_currency_usd should format with exactly 2 decimal places."""
        self.assertEqual(format_currency_usd(19.9), "$19.90")
        self.assertEqual(format_currency_usd(5.0), "$5.00")

    def test_bug_20(self):
        """Bug #20: calculate_ticket_price should charge adults $12.0 and seniors $7.0."""
        self.assertEqual(calculate_ticket_price(10), 5.0)  # Child
        self.assertEqual(calculate_ticket_price(30), 12.0) # Adult
        self.assertEqual(calculate_ticket_price(70), 7.0)  # Senior

if __name__ == "__main__":
    unittest.main()
