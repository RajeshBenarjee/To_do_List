# 📝 To-Do List (CLI Based)

A simple command-line To-Do List manager built with Python and JSON for local storage.

## 🚀 Features

- ✅ Add tasks with descriptions
- 📋 List all tasks with status
- 🔁 Toggle completion (complete/incomplete)
- ❌ Delete tasks by ID
- 💾 Automatically saves data in `todo.json`

---

# 🛠️ How to Run

# 1. Clone the repository
git clone https://github.com/RajeshBenarjee/To_do_List.git
cd To_do_List

2. Create todo.json (if not already present)
  json
    {
        "tasks": []
    }
3. Run the app
python app.py


💡 Commands (inside the app)
Command	Description
add <task>	Add a new task
list	Show all tasks
toggle <id>	Mark task as complete/incomplete
delete <id>	Delete a task
help	Show available commands
exit	Exit the application

📁 File Structure
To_do_List/
│
├── app.py           # Main CLI app
├── todo.json        # Stores tasks (local database)
└── README.md        # You're reading it!

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

👤 Author
Rajesh Benarjee
GitHub: @RajeshBenarjee
