class Bag():
    """
    A class for handling bags.

    @param model: A string model name.
    """
    def __init__(self, model, color, pockets, waterproof=False,
                 height=1, width=1, depth=1):
        self.model = model
        self.color = color
        self.pockets = pockets
        self.waterproof = waterproof
        self.height = height
        self.width = width
        self.depth = depth

    def fashionable(self):
        return self.color == 'red' and self.waterproof is False

    def volume(self):
        return self.height * self.width * self.depth


class Rucksack(Bag):
    def __init__(self, model, color, pockets, hasDaypack=True):
        super().__init__(model, color, pockets, waterproof=True)
        self.hasDaypack = hasDaypack

    def __len__(self):
        return 2 * self.pockets
