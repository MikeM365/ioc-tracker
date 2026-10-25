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

git clone <repo-url>
cd ioc-tracker
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python database_setup.py


## Usage

Run `python main.py` and follow the on-screen menu:

=== IOC Tracker CLI ===

Add new IOC
View all IOCs
Search IOCs
Exit

- **Add new IOC** prompts for the IOC type (IP, Domain, or Hash), its value, and a source describing where it was identified.
- **View all IOCs** lists every IOC currently stored.
- **Search IOCs** prompts for a search term and returns matching records.

## License

MIT License.

## Author

Mike McGregor
