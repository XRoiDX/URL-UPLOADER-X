class Translation(object):
    START_TEXT = """Hi {},
ɪ'ᴍ ᴜʀʟ x ᴜᴘʟᴏᴀᴅᴇʀ!
ʏᴏᴜ ᴄᴀɴ ᴜᴘʟᴏᴀᴅ ʜᴛᴛᴘ/ʜᴛᴛᴘs ᴅɪʀᴇᴄᴛ ʟɪɴᴋ, 
ᴜsɪɴɢ ᴛʜɪs ʙᴏᴛ!
/help ꜰᴏʀ ᴍᴏʀᴇ ᴅᴇᴛᴀɪʟs!"""
    FORMAT_SELECTION = "sᴇʟᴇᴄᴛ ᴛʜᴇ ᴅᴇsɪʀᴇᴅ ꜰᴏʀᴍᴀᴛ: <a href='{}'>ꜰɪʟᴇ sɪᴢᴇ ᴍɪɢʜᴛ ʙᴇ ᴀᴘᴘʀᴏxɪᴍᴀᴛᴇ</a> \nɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴇᴛ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ, sᴇɴᴅ ᴘʜᴏᴛᴏ ʙᴇꜰᴏʀᴇ ᴏʀ ǫᴜɪᴄᴋʟʏ ᴀꜰᴛᴇʀ ᴛᴀᴘᴘɪɴɢ ᴏɴ ᴀɴʏ ᴏꜰ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴs.\nʏᴏᴜ ᴄᴀɴ ᴜsᴇ /deletethumbnail ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴀᴜᴛᴏ-ɢᴇɴᴇʀᴀᴛᴇᴅ ᴛʜᴜᴍʙɴᴀɪʟ."
    SET_CUSTOM_USERNAME_PASSWORD = """ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴘʀᴇᴍɪᴜᴍ ᴠɪᴅᴇᴏs,ᴘʀᴏᴠɪᴅᴇ ɪɴ ᴛʜᴇ ꜰᴏʟʟᴏᴡɪɴɢ ꜰᴏʀᴍᴀᴛ:
URL | filename | username | password"""
    DOWNLOAD_START = "📥Dᴏᴡɴʟᴏᴀᴅɪɴɢ Pʟᴇᴀsᴇ ᴡᴀɪᴛ..."
    UPLOAD_START = "📤 Uᴘʟᴏᴀᴅɪɴɢ Pʟᴇᴀsᴇ ᴡᴀɪᴛ..."
    RCHD_TG_API_LIMIT = "Dᴏᴡɴʟᴏᴀᴅᴇᴅ ɪɴ {} seconds.\nDᴇᴛᴇᴄᴛᴇᴅ ꜰɪʟᴇ sɪᴢᴇ: {}\nSᴏʀʀʏ. ʙᴜᴛ, ɪ ᴄᴀɴɴᴏᴛ ᴜᴘʟᴏᴀᴅ ꜰɪʟᴇs ɢʀᴇᴀᴛᴇʀ ᴛʜᴀɴ 2ɢʙ ᴅᴜᴇ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴘɪ ʟɪᴍɪᴛᴀᴛɪᴏɴs"
    AFTER_SUCCESSFUL_UPLOAD_MSG = "ᴛʜᴀɴᴋs ꜰᴏʀ ᴜsɪɴɢ ᴛʜɪs ʙᴏᴛ\n\n<b>Jᴏɪɴ : @XRoid_BotZ</b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ɪɴ {} sᴇᴄᴏɴᴅs.\nUᴘʟᴏᴀᴅᴇᴅ ɪɴ {} sᴇᴄᴏɴᴅs.\n\n@XRoid_BotZ"
    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    CUSTOM_CAPTION_UL_FILE = "{}"
    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    HELP_USER = """How to Use Me? Follow These steps!
    
1. Send url (example.domain/File.mp4 | New Filename.mp4).
2. Send Image As Custom Thumbnail (Optional).
3. Select the button.
   SVideo - Give File as video with Screenshots
   DFile  - Give File (video) as file with Screenshots
   Video  - Give File as video without Screenshots
   File   - Give File without Screenshots

If bot didn't respond, contact @Sources_Codes"""
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = """Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
You can use /rename command after receiving file to rename it with custom thumbnail support.
"""
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
