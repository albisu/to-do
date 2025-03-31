# To-Do List Application

This is a simple GUI-based To-Do List application that allows users to create projects or groups, and within those groups, create tasks and subgroups. The application is designed to help users manage their tasks efficiently.

## Features

- Create and manage projects/groups
- Add, remove, and update tasks within each group
- Navigate between different groups
- User-friendly graphical interface

## Project Structure

```
to-do-list-app
├── src
│   ├── main.py               # Entry point of the application
│   ├── gui
│   │   ├── app_window.py     # Main application window
│   │   └── components
│   │       ├── task_list.py   # Task management component
│   │       └── group_list.py   # Group management component
│   ├── models
│   │   ├── group.py          # Group model
│   │   └── task.py           # Task model
│   ├── controllers
│   │   ├── group_controller.py # Logic for managing groups
│   │   └── task_controller.py  # Logic for managing tasks
│   └── utils
│       └── helpers.py        # Utility functions
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd to-do-list-app
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.