def sort_voltage_and_kwh_by_time(dictionary_of_time_voltage_kwh):
    sorted_dictionary = {}
    sorted_dictionary["Time"], sorted_dictionary["Voltage"], sorted_dictionary["KWH"] = zip(
        *sorted(zip(dictionary_of_time_voltage_kwh["Time"], dictionary_of_time_voltage_kwh["Voltage"], dictionary_of_time_voltage_kwh["KWH"])))
    return sorted_dictionary
