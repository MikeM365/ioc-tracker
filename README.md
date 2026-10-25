# IOC Tracker CLI

A command-line tool for tracking Indicators of Compromise (IOCs) in a local SQLite database.

## Description

IOC Tracker CLI lets you record, view, and search Indicators of Compromise — IP addresses, domains, and file hashes — each with a source describing where it was identified. Data is stored locally in SQLite with no external services required.

## Features

- Add new IOCs with type (IP, Domain, or Hash), value, and source
- View all stored IOCs
- Search IOCs by keyword
- Interactive command-line menu — no arguments needed
- Local SQLite database, no external dependencies beyond the Python standard library

## Requirements

- Python 3.x
- SQLite (included with Python)

## Installation

1. Clone the repository and `cd` into `ioc-tracker`
2. Create and activate a virtual environment with `python -m venv venv` and `source venv/bin/activate`
3. Install dependencies with `pip install -r requirements.txt`
4. Run `python database_setup.py` to set up the database

## Usage

Run `python main.py` to open the interactive menu:

1. **Add new IOC** — prompts for the IOC type (IP, Domain, or Hash), its value, and a source describing where it was identified
2. **View all IOCs** — lists every IOC currently stored
3. **Search IOCs** — prompts for a search term and returns matching records
4. **Exit** — closes the program

## License

MIT License.

## Author

Mike McGregor
