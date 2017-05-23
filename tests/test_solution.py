from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution
        list = ['a', 'b', 'c', 'b', 'a']
        self.assertEqual(True, solution(list))
        list = ['a', 'c', 'c', 'b', 'a']
        self.assertEqual(False, solution(list))