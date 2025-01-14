from typing import Annotated

from fastapi import APIRouter, Depends

from src.common.dto import UserSchema
from src.database import DBGateway
from src.api.common.providers import Stub


user_router = APIRouter(prefix='/user', tags=['user'])


@user_router.post('/create')
async def create_user(db: Annotated[DBGateway, Depends(Stub(DBGateway))], data: UserSchema) -> UserSchema:
    async with db:
        await db.manager.create_transaction()
        await db.user().create(**data.model_dump())
        
    return data
