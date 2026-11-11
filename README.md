# 📝 To-Do List Web Application

## 📌 Project Description

The To-Do List Web Application is a task management system developed using Python Flask, HTML, and CSS.

It allows users to add, view, edit, and delete their daily tasks through a simple and user-friendly web interface. Tasks are stored in a text file to maintain the task list even after closing the application.

## 🚀 Features

- Add new tasks.
- View all available tasks.
- Edit existing tasks.
- Delete unwanted tasks.
- Display tasks in a numbered format.
- Show the total number of tasks.
- Automatically save tasks in a text file.
- Load previously saved tasks when restarting the application.
- Responsive and attractive user interface.
- Input validation to prevent empty tasks.

## 🛠️ Technologies Used

- Python
- Flask
- HTML5
- CSS3
- Jinja2
- File Handling

## 📂 Project Structure

```text
To-Do-Web-App/
│
├── app.py
│
├── tasks.txt
│
├── templates/
│   ├── index.html
│   └── edit.html
│
└── static/
    └── style.css
```

## ⚙️ Installation and Setup

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Navigate to the Project Folder

```bash
cd To-Do-Web-App
```

### Step 3: Install Flask

```bash
pip install flask
```

### Step 4: Run the Application

```bash
python app.py
```

### Step 5: Open in Browser

Visit:

```text
http://127.0.0.1:5000
```

## 📖 How to Use

1. Open the application in your browser.
2. Enter a task in the input field.
3. Click the Add Task button.
4. View all added tasks in the task list.
5. Click Edit to modify an existing task.
6. Click Save Changes to update the task.
7. Click Delete to remove an unwanted task.
8. Check the total task count displayed on the page.

## 📊 Application Features

| Feature | Description |
|---------|-------------|
| Add Task | Creates a new task |
| View Tasks | Displays all saved tasks |
| Edit Task | Updates existing tasks |
| Delete Task | Removes selected tasks |
| Task Counter | Displays the total number of tasks |
| File Storage | Saves tasks in tasks.txt |

## 💾 Data Storage

The application uses Python file handling to store tasks in `tasks.txt`.

- Tasks are automatically saved when added.
- Updated tasks are saved after editing.
- Deleted tasks are removed from the file.
- Previously saved tasks are loaded when the application starts.

## 🎯 Project Objective

The main objective of this project is to develop a simple and effective task management application while learning Python Flask, CRUD operations, HTML, CSS, and file handling.

## 👨‍💻 Author

Developed as a Python Web Development Project.

BY
Gogu Prasad
B. Tech Final Year(CSE)
