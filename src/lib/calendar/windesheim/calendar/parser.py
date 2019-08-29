import json
import os
import sys
from datetime import datetime, date, timedelta
from typing import Any, Dict

from ics import Event
from mako.template import Template

from lib.calendar.windesheim.calendar.event import CalendarEvent
from lib.calendar.windesheim.classroom import ClassroomParser
from lib.calendar.windesheim.subject import Subject

TEMPLATE_DIRECTORY = os.path.dirname(os.path.realpath(__file__)) + "/../../../../templates/"
TEMPLATE_DESCRIPTION = "description.mako"
print(os.getcwd())


class EventParser:
    @staticmethod
    def parse_from(json_dict: Dict[str, Any], hours_offset: float) -> CalendarEvent:
        event = CalendarEvent()

        event._id = json_dict["id"]
        event._classroom = ClassroomParser.parse_string(json_dict["lokaal"])
        event._start_time = datetime.fromtimestamp(json_dict["starttijd"] / 1000) + timedelta(hours=hours_offset)
        event._end_time = datetime.fromtimestamp(json_dict["eindtijd"] / 1000) + timedelta(hours=hours_offset)
        event._timetable_date = EventParser.__parse_bad_date(json_dict["roosterdatum"])
        event._title = json_dict["commentaar"]

        event._timetable_code = json_dict["roostercode"]
        event._group_code = json_dict["groepcode"]

        event._subject = Subject(json_dict["vaknaam"], json_dict["vakcode"])
        event._teacher_names = json_dict["docentnamen"]

        event._status = json_dict["status"]
        event._teacher_code = json_dict["docentcode"]
        event._changed = json_dict["changed"]

        return event

    @staticmethod
    def __parse_bad_date(date_time_string: str) -> date:
        [date_string, *time] = date_time_string.split("T")
        return date.fromisoformat(date_string)


class WindesheimEventParser:
    @staticmethod
    def parse(json_string: str) -> Event:
        json_object = json.loads(json_string)

        return WindesheimEventParser.parse_json(json_object)

    @staticmethod
    def parse_json(json_object: Dict[str, Any]) -> Event:
        windesheim_event = EventParser.parse_from(json_object)
        return WindesheimEventParser.parse_windesheim_event(windesheim_event)

    @staticmethod
    def parse_windesheim_event(windesheim_event: CalendarEvent) -> Event:
        event = Event()
        event.begin = windesheim_event.start_time
        event.end = windesheim_event.end_time
        event.name = windesheim_event.title
        event.location = windesheim_event.classroom.to_string()

        with open(TEMPLATE_DIRECTORY + TEMPLATE_DESCRIPTION) as template_file:
            event.description = Template(template_file.read()).render(
                teachers=windesheim_event.teacher_names,
                subject=windesheim_event.subject,
                group_code=windesheim_event.group_code
            )

        return event
