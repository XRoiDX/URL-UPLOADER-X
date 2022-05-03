

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Button(object):

      BUTTONS01 = InlineKeyboardMarkup( [ [ InlineKeyboardButton(text="📁 𝗬𝗧𝗦", callback_data='00'),
                                            InlineKeyboardButton(text="🔍 𝘚𝘦𝘢𝘳𝘤𝘩", switch_inline_query_current_chat="!1 ") ],
                                          [ InlineKeyboardButton(text="📁 𝗔𝗡𝗜𝗠𝗘", callback_data='00'),
                                            InlineKeyboardButton(text="🔍 𝘚𝘦𝘢𝘳𝘤𝘩", switch_inline_query_current_chat="!2 ") ],
                                          [ InlineKeyboardButton(text="📁 1337x", callback_data='00'),
                                            InlineKeyboardButton(text="🔍 𝘚𝘦𝘢𝘳𝘤𝘩", switch_inline_query_current_chat="!3 " ) ],
                                          [ InlineKeyboardButton(text="📁 𝗧𝗛𝗘 𝗣𝗜𝗥𝗔𝗧𝗘 𝗕𝗔𝗬", callback_data='00'),
                                            InlineKeyboardButton(text="🔍 𝘚𝘦𝘢𝘳𝘤𝘩", switch_inline_query_current_chat="!4 ") ],
                                          [ InlineKeyboardButton(text="❌ CANCEL ❌", callback_data="X0") ] ] )
