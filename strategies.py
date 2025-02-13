from abc import ABC, abstractmethod

from item import Item


class UpdateStrategy(ABC):
    @abstractmethod
    def update(self, item: Item):
        pass

    def decrease_quality(self, item: Item, amount: int):
        item.quality = max(0, item.quality - amount)

    def increase_quality(self, item: Item, amount: int):
        item.quality = min(50, item.quality + amount)

    def decrease_day(self, item: Item):
        item.sell_in = max(0, item.sell_in - 1)


class DefaultStrategy(UpdateStrategy):
    def update(self, item: Item):
        self.decrease_quality(item, 1)
        self.decrease_day(item)
        # At the end of each day our system lowers both values for every item
        if item.sell_in < 0:
            self.decrease_quality(item, 2)


class AgedBrieStrategy(UpdateStrategy):
    # "Aged Brie" actually increases in Quality the older it gets
    def update(self, item: Item):
        self.increase_quality(item, 1)
        self.decrease_day(item)


class SulfurasStrategy(UpdateStrategy):
    # "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
    def update(self, item: Item):
        pass


class BackstagePassStrategy(UpdateStrategy):
    # increases in Quality as its SellIn value approaches;
    # Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
    # Quality drops to 0 after the concert
    def update(self, item: Item):
        if item.sell_in > 10:
            self.increase_quality(item, 1)
        elif item.sell_in <= 10 and item.sell_in > 5:
            self.increase_quality(item, 2)
        elif item.sell_in <= 5 and item.sell_in > 0:
            self.increase_quality(item, 3)
        elif item.sell_in <= 0:
            item.quality = 0

        self.decrease_day(item)


class ConjureStrategy(UpdateStrategy):
    # "Conjured" items degrade in Quality twice as fast as normal items
    def update(self, item: Item):
        if item.sell_in > 0:
            self.decrease_quality(item, 2)
        else:
            self.decrease_quality(item, 4)
        self.decrease_day(item)


class UpdateStrategyFactory():
    def get_strategy(item: Item) -> UpdateStrategy:
        if item.name == "Aged Brie":
            return AgedBrieStrategy()
        elif item.name in "Sulfuras, Hand of Ragnaros":
            return SulfurasStrategy()
        elif item.name in "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePassStrategy()
        elif item.name in "Conjured":
            return ConjureStrategy()
        else:
            return DefaultStrategy()
