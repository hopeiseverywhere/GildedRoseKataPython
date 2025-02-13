# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]

    def test_conjured_degrade_twice_as_fast(self):
        items = [Item("Conjured", 1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 8) 

    def test_back_stage_pass_increase_quantity_under_ten_days(self):
        items = [Item("Backstage passes", 9, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 12)

    def test_back_stage_pass_quantity_drop_to_zero_post_concert(self):
        items = [Item("Backstage passes", 1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)

    def test_item_name_to_string(self):
        items = [Item("item2", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("item2", gilded_rose.get_name(0))

if __name__ == '__main__':
    unittest.main()
