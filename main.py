import tkinter as tk
from tkinter import ttk


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

                    tree_ingredients.insert('', index='end', values=(ent_name.get(), ent_price.get()))

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

                for child in tree_ingredients.get_children():
                    if option.get() in tree_ingredients.item(child)['values']:
                        tree_ingredients.delete(child)
                        break

            else:
                lbl_remove['text'] = "There's nothing to remove!"
            if len(list(ingredients.keys())) > 0:
                option.set(list(ingredients.keys())[0])
            else:
                option.set("Empty")

        frm_buttons = tk.Frame(master=window)
        frm_catalog = tk.Frame(master=window)

        # The ingredient catalog
        scr_ingredients = tk.Scrollbar(master=frm_catalog)
        scr_ingredients.pack(side=tk.RIGHT, fill=tk.Y)

        tree_ingredients = ttk.Treeview(master=frm_catalog, columns=(1, 2), show='headings',
                                        yscrollcommand=scr_ingredients.set)
        scr_ingredients.config(command=tree_ingredients.yview)

        tree_ingredients.heading(1, text='Ingredient')
        tree_ingredients.heading(2, text='Price per kilo')

        for key in ingredients.keys():
            if key != 'Empty':
                tree_ingredients.insert('', 'end', values=(ingredients[key].name, ingredients[key].price))

        tree_ingredients.pack()

        # The Adding Item Portion
        frm_add = tk.Frame(master=frm_buttons)
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
        frm_remove = tk.Frame(master=frm_buttons)

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

        frm_catalog.grid(row=0, column=0)
        frm_buttons.grid(row=1, column=0)

    in_window = tk.Toplevel(main_window)
    in_window.title("Edit the ingredient list")
    in_window.grab_set()
    in_window.focus_set()
    setup(in_window)
    in_window.mainloop()

    return


def edit_menu_items(main_window, ingredients: dict, menu: dict):
    def setup(window):
        def add_to_list(w):
            def add_ingredient():
                if option.get() != "None" and ent_ingredient_amount.get() != "" and ent_ingredient_amount.get().isnumeric():
                    tree_recipe.insert('', index='end', values=(option.get(), ent_ingredient_amount.get()))

                    ent_ingredient_amount.delete(0, len(ent_ingredient_amount.get()))
                return

            def remove_ingredient():
                if option.get() != "None" and len(tree_recipe.get_children()) > 0:
                    for child in tree_recipe.get_children():
                        if option.get() in tree_recipe.item(child)['values']:
                            tree_recipe.delete(child)
                return

            def save_recipe():
                if ent_recipe_name != '' and ent_recipe_amount != '' and ent_recipe_amount.get().isnumeric():
                    atoms = list()
                    base_cost = 0

                    for child in tree_recipe.get_children():
                        atoms.append((ingredients[tree_recipe.item(child)['values'][0]],
                                      tree_recipe.item(child)['values'][1]))
                        base_cost += float(atoms[-1][0].price) * atoms[-1][1]

                    menu[ent_recipe_name.get()] = MenuItem(ent_recipe_name.get(),
                                                           atoms,
                                                           float(ent_recipe_amount.get()),
                                                           price=0)
                    add_win.grab_release()
                    tree_menu.insert('', index='end', values=(ent_recipe_name.get(), base_cost, ent_recipe_amount.get(), 0))
                    add_win.destroy()
                return

            add_win = tk.Toplevel(w)
            add_win.title("Add a menu item")
            add_win.grab_set()
            add_win.focus_set()

            frm_recipe = tk.Frame(master=add_win)
            frm_recipe_buttons = tk.Frame(master=add_win)

            # The recipe table
            scr_recipe = tk.Scrollbar(master=frm_recipe)
            scr_recipe.pack(side=tk.RIGHT, fill=tk.Y)

            tree_recipe = ttk.Treeview(master=frm_recipe, columns=(1, 2), show='headings',
                                       yscrollcommand=scr_recipe.set)
            tree_recipe.heading(1, text="Ingredient")
            tree_recipe.heading(2, text="Amount (kg)")

            scr_recipe.config(command=tree_recipe.yview)
            tree_recipe.pack()

            # Adding ingredients
            lbl_ingredient_opt = tk.Label(master=frm_recipe_buttons, text="Ingredient")
            OPTIONS = list(ingredients.keys())
            option = tk.StringVar(master=frm_recipe_buttons)
            option.set("None")
            opt_ingredients = tk.OptionMenu(frm_recipe_buttons, option, *OPTIONS)

            lbl_ingredient_amount = tk.Label(master=frm_recipe_buttons, text="Amount (kg)")
            ent_ingredient_amount = tk.Entry(master=frm_recipe_buttons)

            btn_recipe_add = tk.Button(master=frm_recipe_buttons, text='Add ingredient', command=add_ingredient)

            lbl_ingredient_opt.grid(row=0, column=0)
            opt_ingredients.grid(row=1, column=0)
            lbl_ingredient_amount.grid(row=0, column=1)
            ent_ingredient_amount.grid(row=1, column=1)
            btn_recipe_add.grid(row=2, column=1)

            # Removing ingredients
            btn_recipe_remove = tk.Button(master=frm_recipe_buttons, text="Remove ingredient",
                                          command=remove_ingredient)

            btn_recipe_remove.grid(row=3, column=1)

            # Saving recipe
            lbl_empty = tk.Label(master=frm_recipe_buttons, text="    ")

            lbl_recipe_name = tk.Label(master=frm_recipe_buttons, text="Recipe name")
            ent_recipe_name = tk.Entry(master=frm_recipe_buttons)

            lbl_recipe_amount = tk.Label(master=frm_recipe_buttons, text="Expected amount")
            ent_recipe_amount = tk.Entry(master=frm_recipe_buttons)

            btn_recipe_save = tk.Button(master=frm_recipe_buttons, text="Save to menu", command=save_recipe)

            lbl_empty.grid(row=2, column=2)
            lbl_recipe_name.grid(row=1, column=3)
            ent_recipe_name.grid(row=1, column=4)
            lbl_recipe_amount.grid(row=2, column=3)
            ent_recipe_amount.grid(row=2, column=4)
            btn_recipe_save.grid(row=3, column=4)

            # Positioning frames
            frm_recipe.grid(row=0, column=0)
            frm_recipe_buttons.grid(row=1, column=0)

            add_win.mainloop()

        def remove_from_list(w):
            return

        frm_menu = tk.Frame(master=window)
        frm_buttons = tk.Frame(master=window)

        # The menu catalog
        scr_menu_v = tk.Scrollbar(master=frm_menu)
        scr_menu_v.pack(side=tk.RIGHT, fill=tk.Y)
        scr_menu_h = tk.Scrollbar(master=frm_menu, orient='horizontal')
        scr_menu_h.pack(side=tk.BOTTOM, fill=tk.X)

        tree_menu = ttk.Treeview(master=frm_menu, columns=(1, 2, 3, 4), show='headings', yscrollcommand=scr_menu_v.set,
                                 xscrollcommand=scr_menu_h.set)

        scr_menu_v.config(command=tree_menu.yview)
        scr_menu_h.config(command=tree_menu.xview)

        tree_menu.heading(1, text='Menu Item')
        tree_menu.heading(2, text='Base Cost')
        tree_menu.heading(3, text='Expected Consumption')
        tree_menu.heading(4, text='Price')

        tree_menu.pack()

        # The Adding Item Portion
        btn_add = tk.Button(master=frm_buttons, text="Add menu item", command=lambda: add_to_list(window))

        # The Removing Item Portion
        btn_remove = tk.Button(master=frm_buttons, text="Remove menu item", command=lambda: remove_from_list(window))

        # The Positioning Portion
        frm_menu.grid(row=0)

        frm_buttons.grid(row=1)
        btn_add.grid(row=0, column=0)
        btn_remove.grid(row=0, column=1)

    menu_window = tk.Toplevel(main_window)
    menu_window.title("Edit the menu")
    menu_window.grab_set()
    menu_window.focus_set()
    setup(menu_window)
    menu_window.mainloop()


def edit_wages(main_window):
    return


def edit_misc(main_window):
    return


class MenuItem:
    def __init__(self, name: str, ingredient_amounts: list, number_served: float, price=None):
        self.name = name
        self.ingredients = ingredient_amounts
        self.served = number_served

        if price is not None:
            self.price = price
        else:
            self.price = 0

        self.base_cost = 0
        for i in range(0, len(self.ingredients)):
            self.base_cost += float(self.ingredients[i][0].price)*float(self.ingredients[i][1])
        return


class Ingredient:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        return


def main_window_setup(main_window: tk.Tk, ingredients: dict, menu: dict, wages):
    # Welcome Frame
    frm_welcome = tk.Frame(master=main_window)

    photo = tk.PhotoImage(file='Hello.png')
    lbl_welcome = tk.Label(master=frm_welcome, text="Hello!", image=photo, compound='top')
    lbl_welcome.grid(row=0, sticky='NSEW')
    lbl_welcome.image = photo

    frm_buttons = tk.Frame(master=main_window)
    # Ingredient button
    btn_edit_ingredient = tk.Button(master=frm_buttons, text="Show/edit ingredients",
                                    command=lambda: edit_ingredients(main_window, ingredients))

    # Menu Item Button
    btn_edit_menu_item = tk.Button(master=frm_buttons, text="Show/edit menu items",
                                   command=lambda: edit_menu_items(main_window, ingredients, menu))

    # Wage Button
    btn_set_wages = tk.Button(master=frm_buttons, text="Show/edit wages",
                              command=lambda: edit_wages(main_window))

    # Misc Button
    btn_edit_misc = tk.Button(master=frm_buttons, text="Show/edit misc",
                              command=lambda: edit_misc(main_window))

    # Positioning
    frm_welcome.grid(row=0, column=0, sticky='NSEW')

    frm_buttons.grid(row=1, column=0)

    btn_edit_ingredient.grid(row=0, column=0, sticky='NSEW')
    btn_edit_menu_item.grid(row=0, column=1, sticky='NSEW')
    btn_set_wages.grid(row=0, column=2, sticky='NSEW')
    btn_edit_misc.grid(row=0, column=3, sticky='NSEW')

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
