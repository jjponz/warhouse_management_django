class DjangoSaveItemExecutor:
    def __init__(self, form, adapter, action):
        self.__form = form
        self.__adapter = adapter
        self.__action = action

    def do (self):
        django_item = self.__form.save(commit=False)
        item = self.__adapter.to_item(django_item)

        return self.__action.do(item)


