# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]

    # example of test that checks for logical errors
    # def test_sulfuras_should_not_decrease_quality(self):
    #     items = [Item("Sulfuras", 5, 80)]
    #     gilded_rose = GildedRose(items)
    #     gilded_rose.update_quality()
    #     self.assertEquals("Sulfuras", items[0].name)
    #     sulfuras_item = items[0]
    #     self.assertEquals(80, sulfuras_item.quality)
    #     self.assertEquals(4, sulfuras_item.sell_in)
    #     self.assertEquals("Sulfuras", sulfuras_item.name)

    # example of test that checks for syntax errors
    # def test_gilded_rose_list_all_items(self):
    #     items = [Item("Sulfuras", 5, 80)]
    #     gilded_rose = GildedRose(items)
    #     all_items = gilded_rose.get_items()
    #     self.assertEquals(["Sulfuras"], all_items)


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
        self.assertEqual("item2", items[0].to_string())


if __name__ == '__main__':
    unittest.main()
