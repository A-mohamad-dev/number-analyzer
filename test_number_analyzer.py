import unittest
from number_analyzer import analyze_number, calculate_statistics

class TestAnalyzeNumber(unittest.TestCase):
    
    def test_positive_odd(self):
        self.assertEqual(analyze_number(5), ("odd", "positive"))
    
    def test_negative_even(self):
        self.assertEqual(analyze_number(-8), ("even", "negative"))
    
    def test_zero(self):
        self.assertEqual(analyze_number(0), ("even", "zero"))
    
    def test_positive_even(self):
        self.assertEqual(analyze_number(24), ("even", "positive"))
    
    def test_negative_odd(self):
        self.assertEqual(analyze_number(-7), ("odd", "negative"))
        
class TestCalculateStatistics(unittest.TestCase):
    
    def test_statistics(self):
        numbers = [5, -8, 0, 24, -7]
        
        statistics = calculate_statistics(numbers)
        
        self.assertEqual(statistics["even"], 3)
        self.assertEqual(statistics["odd"], 2)
        self.assertEqual(statistics["positive"], 2)
        self.assertEqual(statistics["negative"], 2)
        self.assertEqual(statistics["zero"], 1)
        self.assertEqual(statistics["sum"], 14)
        self.assertEqual(statistics["average"], 2.8)

    def test_empty_list(self):
        statistics = calculate_statistics([])

        self.assertEqual(statistics["even"], 0)
        self.assertEqual(statistics["odd"], 0)
        self.assertEqual(statistics["positive"], 0)
        self.assertEqual(statistics["negative"], 0)
        self.assertEqual(statistics["zero"], 0)
        self.assertEqual(statistics["sum"], 0)
        self.assertIsNone(statistics["average"])
  
if __name__ == "__main__":
  unittest.main()