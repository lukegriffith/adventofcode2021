#!/bin/env python3
import unittest
import main

sample = 'sample_input.txt'

class TestDay4(unittest.TestCase):

    def test_main_sample_data(self):
        self.assertEqual(main.main(sample), 4512)
       
    def test_structure(self):
        with open(sample) as f:
            struct = main.structure(f)
            self.assertNotEqual(struct.bingo_numbers, None)
            self.assertEqual(len(struct.boards), 3)
            for number in list(map(int,struct.bingo_numbers.split(","))):
                if number not in struct.coord_set:
                    self.fail("Coords not correct")
            


if __name__ == '__main__':
    unittest.main()
