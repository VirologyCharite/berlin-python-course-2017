from unittest import TestCase

from plaques import calculateTiter


class TestCalculateTiter(TestCase):

    def testOneCountIsZero(self):
        self.assertEqual(0, calculateTiter([0], [100], 100))

    def testAllOnes(self):
        """
        If we pass just one count and one dilution and a volume
        and they are all equal to 1, the resulting titer must also be 1.
        """
        self.assertEqual(1, calculateTiter([1], [1], 1))

    def testNonTrivial(self):
        """
        If we pass non-trivial values, the resulting titer must be correct.
        """
        self.assertEqual(4, calculateTiter([1, 2], [2, 3], 2))

    def testFloatingPoint(self):
        """
        If we pass floating point values, the resulting titer must be correct.
        """
        self.assertEqual(15.5, calculateTiter([5, 3], [2, 7], 2.0))

    def testNegativeVolume(self):
        """
        If we pass a negative volume, calculateTiter must raise a ValueError.
        """
        with self.assertRaises(ValueError):
            calculateTiter([1], [1], -1)

    def testZeroVolume(self):
        """
        If we pass a zero volume, calculateTiter must raise a ValueError.
        """
        with self.assertRaises(ValueError):
            calculateTiter([1], [1], 0)

    def testNoCounts(self):
        """
        If we pass an empty counts list, calculateTiter must raise a
        ValueError.
        """
        with self.assertRaises(ValueError):
            calculateTiter([], [], 1)

    def testDifferentCountAndDilutionLengths(self):
        """
        If we pass a counts list that has a different number of items from the
        dilutions list, calculateTiter must raise a ValueError.
        """
        with self.assertRaises(ValueError):
            calculateTiter([1, 1], [1], 1)

    def testNonIntegerCounts(self):
        """
        If we pass a counts list that has a non-integer value, calculateTiter
        must raise a ValueError.
        """
        with self.assertRaises(ValueError):
            calculateTiter([0.5], [1], 1)
