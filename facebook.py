import tkinter as tk
from tkinter import messagebox

# Create an empty dictionary to store user information
user_data = {}

# Function to register a new user
def register_user():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    gender = gender_entry.get()
    age = age_entry.get()

    user_info = {
        "Last Name": last_name,
        "Gender": gender,
        "Age": age
    }

    user_data[first_name] = user_info
    messagebox.showinfo("Registration", f"User {first_name} has been registered successfully!")

    # Clear the input fields after registration
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    gender_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)

# Function to search for a user by first name
def search_user():
    search_name = search_entry.get()
    if search_name in user_data:
        user_info = user_data[search_name]
        result_text.set(f"Last Name: {user_info['Last Name']}\nGender: {user_info['Gender']}\nAge: {user_info['Age']}")
    else:
        result_text.set("No user found with that First Name.")

# Create the main application window
app = tk.Tk()
app.title("User Registration and Search")

# Create and arrange widgets
frame_register = tk.Frame(app)
frame_register.pack(pady=10)

tk.Label(frame_register, text="First Name:").grid(row=0, column=0)
tk.Label(frame_register, text="Last Name:").grid(row=1, column=0)
tk.Label(frame_register, text="Gender:").grid(row=2, column=0)
tk.Label(frame_register, text="Age:").grid(row=3, column=0)

first_name_entry = tk.Entry(frame_register)
last_name_entry = tk.Entry(frame_register)
gender_entry = tk.Entry(frame_register)
age_entry = tk.Entry(frame_register)

first_name_entry.grid(row=0, column=1)
last_name_entry.grid(row=1, column=1)
gender_entry.grid(row=2, column=1)
age_entry.grid(row=3, column=1)

register_button = tk.Button(frame_register, text="Register", command=register_user)
register_button.grid(row=4, column=0, columnspan=2)

frame_search = tk.Frame(app)
frame_search.pack(pady=10)

tk.Label(frame_search, text="Search by First Name:").pack()
search_entry = tk.Entry(frame_search)
search_entry.pack()
search_button = tk.Button(frame_search, text="Search", command=search_user)
search_button.pack()

result_text = tk.StringVar()
result_label = tk.Label(frame_search, textvariable=result_text)
result_label.pack()

# Run the main application loop
app.mainloop()
