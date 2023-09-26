from aiogram import Router, types
from aiogram.fsm.context import FSMContext

from states import UserForm

router = Router()


@router.message(UserForm.name)
async def on_name(message: types.Message, state: FSMContext) -> None:
    # {'name': message.text, 'surname': message.text}
    await state.update_data(name=message.text)
    await message.answer(
        text="Familiyangizni kiriting"
    )
    await state.set_state(UserForm.surname)


@router.message(UserForm.surname)
async def on_surname(message: types.Message, state: FSMContext) -> None:
    await state.update_data(surname=message.text)
    await message.answer(
        text="Iltimos yoshingizni kiriting"
    )
    await state.set_state(UserForm.age)


@router.message(UserForm.age)
async def on_age(message: types.Message, state: FSMContext) -> None:
    await state.update_data(age=message.text)
    data = await state.get_data()
    await message.answer(
        text=f"Ismingiz: {data.get('name')}\n"
             f"Familiyangiz: {data.get('surname')}\n"
             f"Yoshingiz: {data.get('age')}"
    )
    await state.clear()
    