import json


def read_users():
    try:
        with open("db/users.json", "r") as file:
            data = json.load(file)
            users = data["users"]
            return users
    except FileNotFoundError:
        print("❌ users.json не знайдено!")
        return []
    except Exception as e:
        print(f"❌ Помилка: {e}")
        return []


def read_total_users():
    with open("db/users.json", "r") as file:
        data = json.load(file)
        total = {
            "total": data["total"],
            "total_active": data["total_active"],
            "total_inactive": data["total_inactive"],
        }
        return total


def write_users(users):
    with open("db/users.json", "w") as file:
        total = len(users)
        total_active = len([u for u in users if u["state"] == "Active"])
        total_inactive = len([u for u in users if u["state"] == "Inactive"])
        data = {
            "users": users,
            "total": total,
            "total_active": total_active,
            "total_inactive": total_inactive,
        }
        json.dump(data, file)
