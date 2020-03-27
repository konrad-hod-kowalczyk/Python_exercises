def delete_nth(order,max_e):
    motive = []
    for o in order:
        if motive.count(o) < max_e: motive.append(o)
    return motive
