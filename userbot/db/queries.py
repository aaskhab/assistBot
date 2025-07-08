from sqlalchemy import select, insert

from assistBot.db.engine import get_session
from assistBot.db.models import Assistant, Dialog, Message

async def add_dialog(peer_id: int, peer_username: str, text: str, event_id):
    async with get_session() as session:
        stmt = select(Dialog).where(Dialog.peer_id == peer_id)
        dialog = await session.execute(stmt)

        if not dialog:
            dialog = Dialog(peer_id=peer_id, peer_username=peer_username)
            session.add(dialog)
            await session.flush()
        
        msg = Message(
            dialog_id=dialog.id,
            from_owner=False,
            text=text,
            telegram_message_id=event_id
        )
        session.add(msg)
        await session.commit()