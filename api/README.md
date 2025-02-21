# API Data Exporter

## Description
This project retrieves employee task data from a REST API and exports it in different formats: CSV and JSON.

## Features
- Fetches employee task data using a REST API.
- Displays completed tasks.
- Exports an employee's tasks to a CSV file.
- Exports an employee's tasks to a JSON file.
- Exports all employees' tasks into a single JSON file.

## Requirements
- Node.js
- Axios (for API requests)
- File System (fs) module

## Installation
1. Clone this repository:
   ```sh
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```sh
   cd <project_directory>
   ```
3. Install dependencies:
   ```sh
   npm install axios
   ```

## Usage
Run the script with an employee ID as an argument:
```sh
node script.js <employeeId>
```
For example:
```sh
node script.js 2
```

## Output Files
- `<employeeId>.csv` - Contains all tasks of the given employee in CSV format.
- `<employeeId>.json` - Contains all tasks of the given employee in JSON format.
- `todo_all_employees.json` - Contains tasks of all employees in JSON format.

## Author
Francis Mutabazi

## License
This project is licensed under the MIT License.
