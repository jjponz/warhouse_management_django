class ItemValidator:
    def __init__(self):
        pass

    def validate(self, item):
        return item.name is not ""

    @property
    def errors(self):
        return ['some']
