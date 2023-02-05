from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def queue_markup(
    _,
    DURATION,
    CPLAY,
    videoid,
    played: Union[bool, int] = None,
    dur: Union[bool, int] = None,
):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    geez = math.floor(percentage)
    if 0 < geez <= 10:
        bar = "▮▯▯▯▯▯▯▯▯▯"
    elif 10 < geez < 20:
        bar = "▯▮▯▯▯▯▯▯▯▯"
    elif 20 <= geez < 30:
        bar = "▯▯▮▯▯▯▯▯▯▯"
    elif 30 <= geez < 40:
        bar = "▯▯▯▮▯▯▯▯▯▯"
    elif 40 <= geez < 50:
        bar = "▯▯▯▯▮▯▯▯▯▯"
    elif 50 <= geez < 60:
        bar = "▯▯▯▯▯▮▯▯▯▯"
    elif 60 <= geez < 70:
        bar = "▯▯▯▯▯▯▮▯▯▯"
    elif 70 <= geez < 80:
        bar = "▯▯▯▯▯▯▯▮▯▯"
    elif 80 <= geez < 95:
        bar = "▯▯▯▯▯▯▯▯▮▯"
    else:
        bar = "▯▯▯▯▯▯▯▯▯▮"

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
    not_dur = [
        [
            InlineKeyboardButton(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data="close",
            ),
        ]
    ]
        [
            InlineKeyboardButton(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data="close",
            ),
        ],
    ]
    upl = InlineKeyboardMarkup(
        not_dur if DURATION == "Unknown" else dur
    )
    return upl


def queue_back_markup(_, CPLAY):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"queue_back_timer {CPLAY}",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl
