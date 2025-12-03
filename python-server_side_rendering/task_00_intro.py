#!/usr/bin/env python3
import os


def generate_invitations(template, attendees):
    """Generate invitation files from a template and a list of attendees."""

    # Check input types
    if not isinstance(template, str):
        print("Template must be a string")
        return

    if not isinstance(attendees, list):
        print("Attendees must be a list of dictionaries")
        return

    for item in attendees:
        if not isinstance(item, dict):
            print("Attendees must be a list of dictionaries")
            return

    # Handle empty inputs
    if template == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for i, attendee in enumerate(attendees, start=1):
        new_attendee = {}
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if value is None:
                new_attendee[key] = "N/A"
            else:
                new_attendee[key] = value

        attendee_details = template
        for key, value in new_attendee.items():
            attendee_details = attendee_details.replace(f"{{{key}}}", value)

        filename = f"output_{i}.txt"

        if os.path.exists(filename):
            print(f"{filename}")

        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(attendee_details)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")


if __name__ == "__main__":

    # List of attendees
    attendees = [
        {"name": "Alice", "event_title": "Python Conference",
         "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop",
         "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit",
         "event_date": None, "event_location": "Boston"}
    ]

    # Read the template from a file
    with open('template.txt', 'r', encoding='utf-8') as file:
        template_content = file.read()

    # Call the function with the template and attendees list
    generate_invitations(template_content, attendees)
