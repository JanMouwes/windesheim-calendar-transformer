from datetime import datetime, date

from lib.calendar.windesheim.classroom import ClassroomAbstract
from lib.calendar.windesheim.subject import Subject


class CalendarEvent:
    _id: str
    _classroom: ClassroomAbstract
    _start_time: datetime
    _end_time: datetime
    _timetable_date: date
    _title: str

    _timetable_code: str
    _group_code: str

    _subject: Subject

    _teacher_names: [str]

    # I have no idea what the variables below represent, they were just in the data. Use with caution.
    _status: bool
    _teacher_code: None
    _changed: bool

    @property
    def start_time(self):
        return self._start_time

    @property
    def end_time(self):
        return self._end_time

    @property
    def title(self):
        return self._title

    @property
    def classroom(self):
        return self._classroom

    @property
    def teacher_names(self):
        return self._teacher_names

    @property
    def subject(self):
        return self._subject

    @property
    def group_code(self):
        return self._group_code
