def filter_users_by_state(users: list, state: str) -> list:
    if state == "active":
        return [u for u in users if u["state"] == "Active"]
    elif state == "inactive":
        return [u for u in users if u["state"] == "Inactive"]
    else:  # "all"
        return users