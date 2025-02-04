def add_margins(box, margin_size):
    box["height"] += 2*margin_size
    box["width"] += 2*margin_size
    box["y"] -= margin_size
    box["x"] -= margin_size
    return box
