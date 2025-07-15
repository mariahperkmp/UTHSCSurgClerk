
import streamlit as st
import json

# Load data
def load_data(file_name):
    try:
        with open(file_name, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save data
def save_data(file_name, data):
    with open(file_name, 'w') as f:
        json.dump(data, f)

# Study Planner
def study_planner():
    st.header("📅 Study Planner")
    planner_data = load_data('planner_data.json')
    
    task = st.text_input("Add a new task")
    if st.button("Add Task"):
        planner_data.append({"task": task})
        save_data('planner_data.json', planner_data)
    
    st.subheader("Tasks")
    for item in planner_data:
        st.write(item["task"])

# Habit Tracker
def habit_tracker():
    st.header("📈 Habit Tracker")
    tracker_data = load_data('tracker_data.json')
    
    habit = st.text_input("Log a new habit")
    if st.button("Log Habit"):
        tracker_data.append({"habit": habit})
        save_data('tracker_data.json', tracker_data)
    
    st.subheader("Habits")
    for item in tracker_data:
        st.write(item["habit"])

# Quiz Tool
def quiz_tool():
    st.header("🧠 Quiz Tool")
    quiz_data = load_data('quiz_data.json')
    
    question = st.text_input("Add a new question")
    answer = st.text_input("Add the answer")
    if st.button("Add Question"):
        quiz_data.append({"question": question, "answer": answer})
        save_data('quiz_data.json', quiz_data)
    
    st.subheader("Questions")
    for item in quiz_data:
        st.write(f"Q: {item['question']}")
        st.write(f"A: {item['answer']}")

# Main app
def main():
    st.title("🩺 Surgery Clerkship Study App")
    
    menu = ["Study Planner", "Habit Tracker", "Quiz Tool"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice == "Study Planner":
        study_planner()
    elif choice == "Habit Tracker":
        habit_tracker()
    elif choice == "Quiz Tool":
        quiz_tool()

if __name__ == '__main__':
    main()
