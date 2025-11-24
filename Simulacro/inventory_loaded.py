# Default preloaded products for first run (requirement: at least 5 products).

def default_inventory_rows():
    header = ["id","name","brand","category","price","stock","warranty"]
    rows = [
        header,
        ["1","Wireless Mouse","LogiTech","Accessories","25.99","40","12"],
        ["2","Gaming Keyboard","Razer","Accessories","79.99","20","24"],
        ["3","4K Monitor","Samsung","Displays","299.99","15","18"],
        ["4","Bluetooth Speaker","Sony","Audio","59.99","30","12"],
        ["5","USB-C Charger","Anker","Power","19.99","50","6"],
    ]
    return rows

