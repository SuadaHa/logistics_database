import sqlite3
import tkinter as tk
from tkinter import messagebox

DB_NAME = "northshore.db"

def connect():
    return sqlite3.connect(DB_NAME)

def create_tables():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        address TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Shipments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        status TEXT,
        location TEXT,
        FOREIGN KEY(customer_id) REFERENCES Customers(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT,
        quantity INTEGER,
        warehouse TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Drivers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        license TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Vehicles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT,
        capacity INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Incidents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT,
        severity TEXT
    )
    """)

    conn.commit()
    conn.close()

def add_customer():
    name = entry_customer_name.get()
    address = entry_customer_address.get()

    if not name or not address:
        messagebox.showerror("Error", "Please fill all fields")
        return

    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Customers (name, address) VALUES (?, ?)", (name, address))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Customer added")


def add_shipment():
    customer_id = entry_ship_customer.get()
    status = entry_ship_status.get()
    location = entry_ship_location.get()

    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Shipments (customer_id, status, location) VALUES (?, ?, ?)",
        (customer_id, status, location)
    )
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Shipment added")


def view_shipments():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Shipments")
    rows = cursor.fetchall()
    conn.close()

    output.delete("1.0", tk.END)
    for row in rows:
        output.insert(tk.END, f"{row}\n")


def add_inventory():
    item = entry_item.get()
    qty = entry_qty.get()
    warehouse = entry_warehouse.get()

    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Inventory (item_name, quantity, warehouse) VALUES (?, ?, ?)",
        (item, qty, warehouse)
    )
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Inventory added")


def add_incident():
    desc = entry_inc_desc.get()
    severity = entry_inc_sev.get()

    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Incidents (description, severity) VALUES (?, ?)",
        (desc, severity)
    )
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Incident logged")

create_tables()

root = tk.Tk()
root.title("Northshore Logistics System")
root.geometry("650x500")

tk.Label(root, text="Customer Name").grid(row=0, column=0)
entry_customer_name = tk.Entry(root)
entry_customer_name.grid(row=0, column=1)

tk.Label(root, text="Address").grid(row=1, column=0)
entry_customer_address = tk.Entry(root)
entry_customer_address.grid(row=1, column=1)

tk.Button(root, text="Add Customer", command=add_customer).grid(row=2, column=1)

tk.Label(root, text="Customer ID").grid(row=3, column=0)
entry_ship_customer = tk.Entry(root)
entry_ship_customer.grid(row=3, column=1)

tk.Label(root, text="Status").grid(row=4, column=0)
entry_ship_status = tk.Entry(root)
entry_ship_status.grid(row=4, column=1)

tk.Label(root, text="Location").grid(row=5, column=0)
entry_ship_location = tk.Entry(root)
entry_ship_location.grid(row=5, column=1)

tk.Button(root, text="Add Shipment", command=add_shipment).grid(row=6, column=1)
tk.Button(root, text="View Shipments", command=view_shipments).grid(row=6, column=2)

tk.Label(root, text="Item").grid(row=7, column=0)
entry_item = tk.Entry(root)
entry_item.grid(row=7, column=1)

tk.Label(root, text="Quantity").grid(row=8, column=0)
entry_qty = tk.Entry(root)
entry_qty.grid(row=8, column=1)

tk.Label(root, text="Warehouse").grid(row=9, column=0)
entry_warehouse = tk.Entry(root)
entry_warehouse.grid(row=9, column=1)

tk.Button(root, text="Add Inventory", command=add_inventory).grid(row=10, column=1)

tk.Label(root, text="Incident Description").grid(row=11, column=0)
entry_inc_desc = tk.Entry(root)
entry_inc_desc.grid(row=11, column=1)

tk.Label(root, text="Severity").grid(row=12, column=0)
entry_inc_sev = tk.Entry(root)
entry_inc_sev.grid(row=12, column=1)

tk.Button(root, text="Log Incident", command=add_incident).grid(row=13, column=1)

output = tk.Text(root, height=10, width=80)
output.grid(row=14, column=0, columnspan=3)

root.mainloop()
