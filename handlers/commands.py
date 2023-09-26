from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from states import UserForm

router = Router()


@router.message(Command(commands=['start']))
async def on_start(message: types.Message, state: FSMContext) -> None:
    await message.answer(
        text=f"Salom, {message.from_user.full_name}\n"
             f"Iltimos ismingiz kiriting"
    )
    await state.set_state(UserForm.name)
