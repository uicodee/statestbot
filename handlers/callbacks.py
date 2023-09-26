from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

router = Router()


@router.callback_query(F.data == "cancel")
async def on_cancel(callback: types.CallbackQuery, state: FSMContext) -> None:
    await state.clear()
    await callback.message.delete()
