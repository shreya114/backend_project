import tkinter as tk
from tkinter import messagebox

class FlightBookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flight Ticket Booking System")
        self.root.geometry("600x400")

        # Create frames
        self.login_frame = tk.Frame(self.root)
        self.user_frame = tk.Frame(self.root)
        self.search_frame = tk.Frame(self.root)

        # Initialize login frame
        self.init_login_frame()

    def init_login_frame(self):
        self.login_frame.pack(fill=tk.BOTH, expand=True)
        tk.Label(self.login_frame, text="Username:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self.login_frame, text="Password:").grid(row=1, column=0, padx=10, pady=5)

        self.username_entry = tk.Entry(self.login_frame)
        self.password_entry = tk.Entry(self.login_frame, show="*")

        self.username_entry.grid(row=0, column=1, padx=10, pady=5)
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(self.login_frame, text="Login", command=self.login).grid(row=2, column=0, columnspan=2, padx=10, pady=5)
        tk.Button(self.login_frame, text="Sign Up", command=self.sign_up).grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    def login(self):
        # Implement login functionality
        # For simplicity, let's just show a messagebox indicating successful login
        messagebox.showinfo("Login", "Login successful!")
        # After successful login, show search frame
        self.login_frame.pack_forget()
        self.init_search_frame()

    def sign_up(self):
        # Implement sign up functionality
        # For simplicity, let's just show a messagebox indicating successful sign up
        messagebox.showinfo("Sign Up", "Sign up successful!")

    def init_search_frame(self):
        self.search_frame.pack(fill=tk.BOTH, expand=True)
        tk.Label(self.search_frame, text="Search Flights", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.search_frame, text="Date:").pack(pady=5)
        self.date_entry = tk.Entry(self.search_frame)
        self.date_entry.pack(pady=5)
        tk.Label(self.search_frame, text="Time:").pack(pady=5)
        self.time_entry = tk.Entry(self.search_frame)
        self.time_entry.pack(pady=5)
        tk.Button(self.search_frame, text="Search", command=self.search_flights).pack(pady=10)
        tk.Button(self.search_frame, text="Logout", command=self.logout).pack(pady=10)

    def search_flights(self):
        # Implement flight search functionality
        # For now, let's just show a messagebox with search results
        search_date = self.date_entry.get()
        search_time = self.time_entry.get()
        messagebox.showinfo("Search Results", f"Flights available on {search_date} at {search_time}")

    def logout(self):
        # Implement logout functionality
        # For now, let's just go back to the login frame
        self.search_frame.pack_forget()
        self.init_login_frame()

if __name__ == "__main__":
    root = tk.Tk()
    app = FlightBookingApp(root)
    root.mainloop()
