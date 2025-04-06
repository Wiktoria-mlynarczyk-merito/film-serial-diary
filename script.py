import tkinter as tk
from tkinter import ttk, messagebox


GENRES = sorted(["Akcja", "Dramat", "Komedia", "Sci-Fi", "Horror",
                 "Kryminalny", "Fantasy", "Thriller", "Dokumentalny", "Animowany",
                 "Romans", "Przygodowy", "Musical", "Western", "Historyczny", "Film familijny", "Film biograficzny"])


film_entries = []
series_entries = []


def add_entry():
    title = title_entry.get()
    year = year_entry.get()
    director = director_entry.get()
    rating = rating_entry.get()
    genre = genre_combo.get()
    category = category_var.get()
    watch_date = watch_date_entry.get()

    if not title or not year or not director or not rating or not genre or not category:
        messagebox.showwarning("Błąd", "Uzupełnij wszystkie pola!")
        return

    if not year.isdigit() or not rating.isdigit():
        messagebox.showwarning("Błąd danych", "Rok i ocena muszą być liczbami!")
        return

    entry = f"{title} ({year}), Reżyser: {director}, Ocena: {rating}/10, Gatunek: {genre}"
    if watch_date:
        entry += f", Obejrzano: {watch_date}"

    if category == "Film":
        film_entries.append(entry)
        film_listbox.insert(tk.END, entry)
    else:
        series_entries.append(entry)
        series_listbox.insert(tk.END, entry)


    title_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)
    director_entry.delete(0, tk.END)
    rating_entry.delete(0, tk.END)
    genre_combo.set("")
    category_var.set("")
    watch_date_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Dzienniczek Filmowy")
root.geometry("700x650")
root.configure(bg="#2c2f33")

style = ttk.Style()
style.theme_use("clam")
style.configure("TNotebook", background="#2c2f33", borderwidth=0)
style.configure("TNotebook.Tab", background="#7289da", foreground="white", padding=10)
style.map("TNotebook.Tab", background=[("selected", "#99aab5")])

notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

film_frame = tk.Frame(notebook, bg="#23272a")
series_frame = tk.Frame(notebook, bg="#23272a")

notebook.add(film_frame, text="Lista Filmów")
notebook.add(series_frame, text="Lista Seriali")


fields_frame = tk.Frame(root, bg="#2c2f33")
fields_frame.pack(pady=10)

title_label = tk.Label(fields_frame, text="Tytuł:", bg="#2c2f33", fg="white")
title_label.grid(row=0, column=0, sticky="e")
title_entry = tk.Entry(fields_frame, width=40)
title_entry.grid(row=0, column=1, pady=2)

year_label = tk.Label(fields_frame, text="Rok:", bg="#2c2f33", fg="white")
year_label.grid(row=1, column=0, sticky="e")
year_entry = tk.Entry(fields_frame, width=40)
year_entry.grid(row=1, column=1, pady=2)

director_label = tk.Label(fields_frame, text="Reżyser:", bg="#2c2f33", fg="white")
director_label.grid(row=2, column=0, sticky="e")
director_entry = tk.Entry(fields_frame, width=40)
director_entry.grid(row=2, column=1, pady=2)

rating_label = tk.Label(fields_frame, text="Ocena (1-10):", bg="#2c2f33", fg="white")
rating_label.grid(row=3, column=0, sticky="e")
rating_entry = tk.Entry(fields_frame, width=40)
rating_entry.grid(row=3, column=1, pady=2)

genre_label = tk.Label(fields_frame, text="Gatunek:", bg="#2c2f33", fg="white")
genre_label.grid(row=4, column=0, sticky="e")
genre_combo = ttk.Combobox(fields_frame, values=GENRES, width=38)
genre_combo.set("")
genre_combo.grid(row=4, column=1, pady=2)

type_label = tk.Label(fields_frame, text="Kategoria:", bg="#2c2f33", fg="white")
type_label.grid(row=5, column=0, sticky="e")
category_var = tk.StringVar()
category_combo = ttk.Combobox(fields_frame, textvariable=category_var, values=["Film", "Serial"], width=38)
category_combo.grid(row=5, column=1, pady=2)
category_combo.set("")

watch_date_label = tk.Label(fields_frame, text="Data obejrzenia (*opcjonalnie):", bg="#2c2f33", fg="white")
watch_date_label.grid(row=6, column=0, sticky="e")
watch_date_entry = tk.Entry(fields_frame, width=40)
watch_date_entry.grid(row=6, column=1, pady=2)


add_button = tk.Button(root, text="Dodaj wpis", command=add_entry, bg="#43b581", fg="white", width=20)
add_button.pack(pady=10)


film_listbox = tk.Listbox(film_frame, width=100, height=10, bg="white")
film_listbox.pack(pady=10)

series_listbox = tk.Listbox(series_frame, width=100, height=10, bg="white")
series_listbox.pack(pady=10)


root.mainloop()
