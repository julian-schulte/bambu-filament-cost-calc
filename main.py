# BASIC CALCULATION FUNCTIONS

def calc_material_cost(filament_price_per_kg, filament_usage_in_g):
    return (filament_price_per_kg / 1000) * filament_usage_in_g


def calc_energy_cost(energy_cost_per_kwh, printer_watts_per_h, total_print_time_in_h):
    return ((energy_cost_per_kwh / 1000) * printer_watts_per_h) * total_print_time_in_h


def calc_labor_cost(hourly_wage_in_euro, total_manual_work_in_h):
    return hourly_wage_in_euro * total_manual_work_in_h


def calc_total_cost_per_plate(material_cost, energy_cost, labor_cost):
    return material_cost + energy_cost + labor_cost


def calc_total_cost_incl_margin(total_cost_per_plate, buffer_as_percentage, profit_margin_as_percentage):
    return total_cost_per_plate * (1 + buffer_as_percentage / 100) * (1 + profit_margin_as_percentage / 100)


def calc_final_price_per_piece(total_cost_incl_margin, total_models_per_plate):
    return total_cost_incl_margin / total_models_per_plate

def get_valid_input(prompt, min_value=0):
    while True:
        try:
            input_value = float(input(prompt).replace(",", "."))
            if input_value < min_value:
                print(f"Please enter a number >= {min_value}.")
            else:
                return input_value
        except ValueError:
            print(f"Please enter a valid number.")


def main():
    # GET VARIABLES FROM USER
    filament_price_per_kg = get_valid_input("Enter Filament price/kg:")
    filament_usage_in_g = get_valid_input("Enter Filament usage in grams:")
    total_print_time_in_h = get_valid_input("Enter total print time in hours:")
    energy_cost_per_kwh = get_valid_input("Enter energy cost per kWh in Euro:")
    total_manual_work_in_h = get_valid_input("Enter total manual work in hours:")
    hourly_wage_in_euro = get_valid_input("Enter hourly wage in Euro:")
    total_models_per_plate = int(get_valid_input("Enter total models per plate:", min_value=1))
    buffer_as_percentage = get_valid_input("Enter buffer as percentage:")
    profit_margin_as_percentage = get_valid_input("Enter profit margin as percentage:")
    printer_watts_per_h = int(get_valid_input("Enter printer watts per hour:"))

    # CALCULATE AND PRINT
    material_cost = calc_material_cost(filament_price_per_kg, filament_usage_in_g)
    print(f"Material cost: {material_cost:.2f}€")
    energy_cost = calc_energy_cost(energy_cost_per_kwh, printer_watts_per_h, total_print_time_in_h)
    print(f"Energy cost: {energy_cost:.2f}€")
    labor_cost = calc_labor_cost(hourly_wage_in_euro, total_manual_work_in_h)
    print(f"Labor cost: {labor_cost:.2f}€")
    total_cost_per_plate = calc_total_cost_per_plate(material_cost, energy_cost, labor_cost)
    print(f"Total cost per plate: {total_cost_per_plate:.2f}€")
    total_cost_incl_margin = calc_total_cost_incl_margin(total_cost_per_plate, buffer_as_percentage, profit_margin_as_percentage)
    print(f"Cost incl.  {buffer_as_percentage}% Buffer and {profit_margin_as_percentage}% profit margin: {total_cost_incl_margin:.2f}€")
    final_price_per_piece = calc_final_price_per_piece(total_cost_incl_margin, total_models_per_plate)
    print(f"Final price per piece: {final_price_per_piece:.2f}€")


if __name__ == "__main__":
    main()





