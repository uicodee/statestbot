from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


def cancel() -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(
            text="Cancel",
            callback_data="cancel"
        )
    )
    return builder.as_markup()
