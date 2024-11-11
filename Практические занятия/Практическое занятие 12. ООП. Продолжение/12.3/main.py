import tkinter as tk
from tkinter import messagebox

class IceCreamStand:
    def __init__(self, restaurant_name, cuisine_type, flavors, location, working_hours):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.flavors = flavors
        self.location = location
        self.working_hours = working_hours

    def add_flavor(self, flavor):
        if flavor not in self.flavors:
            self.flavors.append(flavor)
        else:
            messagebox.showinfo("Ошибка", f"Сорт мороженого '{flavor}' уже есть в списке!")

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
        else:
            messagebox.showinfo("Ошибка", f"Сорт мороженого '{flavor}' не найден в списке!")

    def display_flavors(self):
        return "\n".join(self.flavors)

class IceCreamStandApp:
    def __init__(self, root, ice_cream_stand):
        self.root = root
        self.ice_cream_stand = ice_cream_stand

        self.root.title("Кафе Мороженое")
        self.root.geometry("400x400")

        self.title_label = tk.Label(self.root, text=f"{self.ice_cream_stand.restaurant_name} - {self.ice_cream_stand.cuisine_type}")
        self.title_label.pack()

        self.flavors_listbox = tk.Listbox(self.root, height=10, width=40)
        self.flavors_listbox.pack(pady=10)
        self.update_flavors_listbox()

        self.flavor_entry = tk.Entry(self.root, width=30)
        self.flavor_entry.pack(pady=5)

        self.add_flavor_button = tk.Button(self.root, text="Добавить сорт", command=self.add_flavor)
        self.add_flavor_button.pack(pady=5)

        self.remove_flavor_button = tk.Button(self.root, text="Удалить сорт", command=self.remove_flavor)
        self.remove_flavor_button.pack(pady=5)

    def add_flavor(self):
        flavor = self.flavor_entry.get()
        if flavor:
            self.ice_cream_stand.add_flavor(flavor)
            self.update_flavors_listbox()
            self.flavor_entry.delete(0, tk.END)

    def remove_flavor(self):
        flavor = self.flavor_entry.get()
        if flavor:
            self.ice_cream_stand.remove_flavor(flavor)
            self.update_flavors_listbox()
            self.flavor_entry.delete(0, tk.END)

    def update_flavors_listbox(self):
        self.flavors_listbox.delete(0, tk.END)
        for flavor in self.ice_cream_stand.flavors:
            self.flavors_listbox.insert(tk.END, flavor)

if __name__ == "__main__":
    ice_cream_stand = IceCreamStand("Сладкий Рай", "Десерты", ["Ваниль", "Шоколад", "Клубника"], "Центр города", "9:00 - 22:00")

    root = tk.Tk()
    app = IceCreamStandApp(root, ice_cream_stand)
    root.mainloop()
