from tabulate import tabulate

def display_table(data, headers):
    if data:
        print(tabulate(data, headers=headers, tablefmt="pretty"))
    else:
        print("No data available.")

def get_user_input(prompt, cast_type=str):
    try:
        return cast_type(input(prompt))
    except ValueError:
        print(f"Invalid input. Please enter a valid {cast_type.__name__}.")
        return get_user_input(prompt, cast_type)
