import uuid

class UIDGenerator:
    @classmethod
    def generate(cls):
        return str(uuid.uuid1())
