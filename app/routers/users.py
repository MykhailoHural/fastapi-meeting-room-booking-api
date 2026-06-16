from fastapi import status, APIRouter
from datetime import datetime, timezone
from app.schemas.user import User, UserCreate, StateFilter
from app.repositories.user_repo import read_users, read_total_users, write_users
from app.services.user_service import filter_users_by_state

router = APIRouter()

@router.get("/users")
async def get_users(state: StateFilter = StateFilter.all) -> list[User]:
    users = read_users()
    return filter_users_by_state(users,state)


@router.get("/users/total")
async def get_users_total() -> dict:
    users = read_total_users()
    return users


@router.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(users_data: UserCreate) -> User:
    now = datetime.now(timezone.utc).isoformat()
    users = read_users()
    new_user_id = users[-1]["id"] + 1
    new_user = {
        "id": new_user_id,
        "first_name": users_data.first_name.strip(),
        "last_name": users_data.last_name.strip(),
        "role": users_data.role,
        "created_at": now,
        "created_by": "system",
        "state": "Active",
    }

    users.append(new_user)
    write_users(users)
    return new_user
