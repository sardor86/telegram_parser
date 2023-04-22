from aiogram.dispatcher import Dispatcher
from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher.storage import FSMContext

from tgbot.states import DeleteGroup
from models import Groups


async def start_delete_group(callback: CallbackQuery) -> None:
    await DeleteGroup.get_group.set()
    await callback.message.edit_text('Отправте сылку на группу')


async def get_group_link(message: Message, state: FSMContext) -> None:
    if await Groups().delete_group(message.text):
        await message.reply('Группа удалена')
    else:
        await message.reply('Группа не существует в базе')
    await state.finish()


def register_delete_group_handler(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(start_delete_group,
                                       lambda callback: callback.data == 'delete_group')

    dp.register_message_handler(get_group_link,
                                state=DeleteGroup.get_group)
