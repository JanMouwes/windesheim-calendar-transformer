from abc import abstractmethod

UNKNOWN_CLASSROOM_STRING: str = "Unknown classroom"
UNKNOWN_BUILDING_STRING: str = "Unknown building"
UNKNOWN_NUMBER_STRING: str = "Unknown number"


class ClassroomAbstract:
    @property
    @abstractmethod
    def building(self) -> str:
        pass

    @property
    @abstractmethod
    def number(self) -> str:
        pass

    @abstractmethod
    def to_string(self):
        pass


class Classroom(ClassroomAbstract):
    __building: str
    __number: str

    def __init__(self, building: str, number: str) -> None:
        super().__init__()
        self.__building = building
        self.__number = number

    @property
    def building(self) -> str:
        return self.__building

    @property
    def number(self) -> str:
        return self.__number

    def to_string(self):
        return self.building + str(self.number)


class EmptyClassroom(ClassroomAbstract):

    @property
    def building(self) -> str:
        return UNKNOWN_BUILDING_STRING

    @property
    def number(self) -> str:
        return UNKNOWN_NUMBER_STRING

    def to_string(self):
        return UNKNOWN_CLASSROOM_STRING


class ClassroomParser:
    @staticmethod
    def parse_string(classroom_string: str) -> ClassroomAbstract:
        if len(classroom_string) == 0:
            return EmptyClassroom()

        [building_letter, *number] = classroom_string
        return Classroom(building_letter, str("".join(number)))
