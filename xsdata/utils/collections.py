def unique_sequence(items, key):
    seen = set()
    return [
        item
        for item in items
        if getattr(item, key) not in seen and not seen.add(getattr(item, key))
    ]
