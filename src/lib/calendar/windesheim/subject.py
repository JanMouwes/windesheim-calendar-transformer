class Subject:
    __name: str
    __code: str

    def __init__(self, name, code):
        self.__name = name
        self.__code = code

    @property
    def name(self) -> str:
        return self.__name

    @property
    def code(self) -> str:
        return self.__code
