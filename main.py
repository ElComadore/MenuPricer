import tkinter as tk


def edit_ingredients(main_window, ingredients: dict):
    def setup(window):
        def add_to_list():
            lbl_message['text'] = "memes"
            if ent_name.get() != "" and ent_price.get != "" and ent_price.get().isnumeric():
                if ent_name.get() not in ingredients:
                    if "Empty" in ingredients:
                        ingredients.pop("Empty", None)
                        opt_ingredients['menu'].delete(0)
                    ingredients[ent_name.get()] = Ingredient(ent_name.get(), ent_price.get())
                    lbl_message['text'] = "Added " + ent_name.get() + " to the list!"

                    opt_ingredients['menu'].add_command(label=ent_name.get(),
                                                        command=lambda value=ent_name.get(): option.set(value))

                    ent_name.delete(first=0, last=len(ent_name.get()))
                    ent_price.delete(first=0, last=len(ent_price.get()))
                else:
                    lbl_message['text'] = "That's already on the list!"
            elif ent_name.get() == "" or ent_price.get() == "":
                lbl_message['text'] = "Make sure to fill all the fields!"
            else:
                lbl_message['text'] = "Make sure the price is numeric!"

        def remove_from_list():
            if option.get() != "Empty":
                ingredients.pop(option.get(), None)
                i = opt_ingredients['menu'].index(option.get())
                opt_ingredients['menu'].delete(i)
                lbl_remove['text'] = "Removed " + option.get()
            else:
                lbl_remove['text'] = "There's nothing to remove!"
            if len(list(ingredients.keys())) > 0:
                option.set(list(ingredients.keys())[0])
            else:
                option.set("Empty")

        # The Adding Item Portion
        frm_add = tk.Frame(master=window)
        ent_name = tk.Entry(master=frm_add)
        lbl_name = tk.Label(master=frm_add, text="Name of ingredient")

        ent_price = tk.Entry(master=frm_add)
        lbl_price = tk.Label(master=frm_add, text="Price per kilo")

        btn_append = tk.Button(master=frm_add, text="Add ingredient", command=add_to_list)
        lbl_message = tk.Label(master=frm_add, text="")

        lbl_name.grid(row=0, column=0)
        ent_name.grid(row=0, column=1)
        lbl_price.grid(row=1, column=0)
        ent_price.grid(row=1, column=1)
        btn_append.grid(row=2, column=0)
        lbl_message.grid(row=2, column=1)

        # The Removing Item Portion
        frm_remove = tk.Frame(master=window)

        option = tk.StringVar(master=frm_remove)
        OPTIONS = list(ingredients.keys())
        option.set(OPTIONS[0])

        opt_ingredients = tk.OptionMenu(frm_remove, option, *OPTIONS)
        lbl_ingredients = tk.Label(master=frm_remove, text="Select an ingredient")
        btn_remove = tk.Button(master=frm_remove, text="Remove ingredient", command=remove_from_list)
        lbl_remove = tk.Label(master=frm_remove, text="")

        lbl_ingredients.grid(row=0, column=0)
        opt_ingredients.grid(row=0, column=1)
        btn_remove.grid(row=1, column=0)
        lbl_remove.grid(row=1, column=1)

        # Positioning frames
        frm_add.grid(row=0, column=0)
        frm_remove.grid(row=0, column=1)

    in_window = tk.Toplevel(main_window)
    in_window.title("Edit the ingredient list")
    in_window.grab_set()
    in_window.focus_set()
    setup(in_window)
    in_window.mainloop()

    return


def edit_menu_items(main_window):
    return


def edit_wages(main_window):
    return


def edit_misc(main_window):
    return


class MenuItem:
    def __init__(self, name: str, ingredient_amounts: list, number_served: int, price=None):
        self.name = name
        self.ingredients = ingredient_amounts
        self.served = number_served

        if price is not None:
            self.price = price
        else:
            self.price = 0

        self.base_cost = 0
        for i in range(0, len(self.ingredients)):
            self.base_cost += self.ingredients[i][0].price*self.ingredients[i][1]
        return


class Ingredient:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        return


def main_window_setup(main_window: tk.Tk, ingredients: dict, menu: dict, wages):
    # Welcome Frame
    frm_welcome = tk.Frame(master=main_window)
    lbl_welcome = tk.Label(master=frm_welcome, text="Hello!")
    lbl_welcome.grid(row=0)

    # Ingredient button
    btn_edit_ingredient = tk.Button(master=main_window, text="Edit ingredients",
                                    command=lambda: edit_ingredients(main_window, ingredients))

    # Menu Item Button
    btn_edit_menu_item = tk.Button(master=main_window, text="Edit menu items",
                                   command=lambda: edit_menu_items(main_window))

    # Wage Button
    btn_set_wages = tk.Button(master=main_window, text="Edit wages",
                              command=lambda: edit_wages(main_window))

    # Misc Button
    btn_edit_misc = tk.Button(master=main_window, text="Edit misc",
                              command=lambda: edit_misc(main_window))

    # Positioning
    frm_welcome.grid(row=0, column=0)
    btn_edit_ingredient.grid(row=1, column=0)
    btn_edit_menu_item.grid(row=1, column=1)
    btn_set_wages.grid(row=1, column=2)
    btn_edit_misc.grid(row=1, column=3)

    return


def main():
    ingredients = {"Empty": None}
    menu = {"Empty": None}
    wages = 0

    main_window = tk.Tk()
    main_window.title("Menu Pricer")
    main_window.resizable(width=True, height=True)

    main_window_setup(main_window, ingredients, menu, wages)

    main_window.mainloop()

    return


main()
