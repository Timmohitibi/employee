# Employee Management System

### Description
This is a simple Employee Management System built using **CustomTkinter** and **Tkinter** in Python. It allows users to add, update, delete, and view employee records stored in a database.

### Features
- Add new employees with ID, Name, Role, Gender, and Status.
- Update existing employee details.
- Delete employees from the system.
- Display employee data in a TreeView.
- User-friendly graphical interface using CustomTkinter.

### Requirements
Ensure you have the following installed before running the application:

- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- CustomTkinter
- SQLite3 (or any other database you intend to use)

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-repo/employee-management.git
   cd employee-management
   ```
2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```
3. **Install required dependencies:**
   ```bash
   pip install customtkinter
   ```

### Running the Application
Run the Python script:
```bash
python lab.py
```

### Usage
1. Enter employee details (ID, Name, Role, Gender, Status).
2. Click **"Add Employee"** to save the details.
3. Click on an employee in the table to update or delete their details.
4. Click **"Clear"** to reset input fields.
5. Changes are saved automatically in the database.

### Troubleshooting
- If you get a `ModuleNotFoundError: No module named 'tkinter'`, install it using:
  ```bash
  sudo apt install python3-tk -y  # For Debian/Ubuntu
  ```
- If `customtkinter` is not found, install it via:
  ```bash
  pip install customtkinter
  ```

### Contribution
Feel free to fork the repository and submit pull requests for improvements.

### License
This project is licensed under the MIT License.

## Author: Timothy Itibi

