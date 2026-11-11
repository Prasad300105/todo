from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

FILE_NAME = "tasks.txt"


# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return [task.strip() for task in file.readlines()]
    return []


# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


# Home page
@app.route("/")
def home():
    tasks = load_tasks()
    return render_template("index.html", tasks=tasks)


# Add task
@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task", "").strip()

    if task:
        tasks = load_tasks()
        tasks.append(task)
        save_tasks(tasks)

    return redirect(url_for("home"))


# Edit task
@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit_task(index):

    tasks = load_tasks()

    if index < 0 or index >= len(tasks):
        return redirect(url_for("home"))

    if request.method == "POST":

        updated_task = request.form.get("task", "").strip()

        if updated_task:
            tasks[index] = updated_task
            save_tasks(tasks)
            return redirect(url_for("home"))

        return render_template(
            "edit.html",
            task=tasks[index],
            index=index,
            error="Task cannot be empty!"
        )

    return render_template(
        "edit.html",
        task=tasks[index],
        index=index
    )


# Delete task
@app.route("/delete/<int:index>", methods=["POST"])
def delete_task(index):

    tasks = load_tasks()

    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)

    return redirect(url_for("home"))


# Run application
if __name__ == "__main__":
    app.run(debug=True)