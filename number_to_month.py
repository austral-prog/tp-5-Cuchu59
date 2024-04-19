def number_to_month(month):
    mon_list = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    a = mon_list[month - 1] if (month > 0 and month < 13) else "error"
    return a
