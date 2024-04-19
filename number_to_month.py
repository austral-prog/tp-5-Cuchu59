def number_to_month(month):
    
    mon_list = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    
    a = mon_list[month_Num - 1] if (month > 0 and month < 13) else "error"
    return a
