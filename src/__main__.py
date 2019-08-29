import json
import os
import sys

from ics import Calendar

from lib.calendar.windesheim.calendar.parser import EventParser, WindesheimEventParser
from lib.util.cli.command_reader import CommandReader

if __name__ == '__main__':

    file_name = "" + input("Please enter the path to the data file\n")

    # read command line arguments, set offset
    command_reader = CommandReader()
    command_reader._argv = sys.argv
    commands = command_reader.commands
    hours_offset = float(0 if "offset" not in commands else commands.get("offset"))

    try:
        output_directory = input("Please enter the path to the output directory\n")
        output_file_name = output_directory + ("" if output_directory is "" else "/") + "windesheim-calendar.ics"

        calendar = Calendar()
        with open(file_name) as data_file:
            json_dict_array = json.load(data_file)

        for json_dict in json_dict_array:
            windesheim_event = EventParser.parse_from(json_dict, hours_offset)
            event = WindesheimEventParser.parse_windesheim_event(windesheim_event)

            calendar.events.add(event)

        with open(output_file_name, "w") as event_file:
            event_file.writelines(calendar)

        print("Done!")

    except FileNotFoundError as error:
        working_dir = os.getcwd()
        print("File " + error.filename + " not found in " + working_dir)
    except Exception as exception:
        print("An exception occurred")
