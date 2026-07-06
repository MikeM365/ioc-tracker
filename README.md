\# IOC Tracker CLI



A command-line interface (CLI) tool for tracking Indicators of Compromise (IOCs) effectively.



\## Features



\- Add, view, and manage IOCs in a local SQLite database.

\- Supports different IOC types (e.g., IP addresses, URLs, hashes).

\- Easy setup and usage.



\## Prerequisites



\- Python 3.x

\- SQLite (included with Python)



\## Setup



1\. \*\*Clone the Repository:\*\*

&nbsp;  ```bash

&nbsp;  C:\Users\mike_\OneDrive\ioc-tracker\ioc-tracker

&nbsp;  cd ioc-tracker

Create and Activate a Virtual Environment:



bash

python -m venv venv

\# Activate the venv

\# Windows: .\\venv\\Scripts\\activate

\# macOS/Linux: source venv/bin/activate

Install Dependencies:



bash

pip install -r requirements.txt

Set Up the Database:



Run the database setup script:

bash

python database\_setup.py

Usage

To add a new IOC:



bash

python main.py add --type <type> --value <value> --description <description>

To view all IOCs:



bash

python main.py list

Contributing

Fork the repository

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a pull request

License

This project is licensed under the MIT License.



text



