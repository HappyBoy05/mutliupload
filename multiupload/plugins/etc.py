#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) oVoIndia | oVo-HxBots

import asyncio, random
from config import Config
from telethon import events, Button
from multiupload.fsub import *
from multiupload import anjana

s = ["CAADBAADxgkAAjQF0VL5yl4Td0utTgI",
	"CAADBAADoAsAAv3iYFGE3u_w4y_1zgI",
	"CAADBAADMggAAq0Q0FK1ZIUPLNxGcAI",
	"CAADBAAD7AoAAr8i2VGALarwosnJIgI",
	"CAADBAADrQoAAmzO0VFDq1aGz7rGHgI",
	"CAADBAADbQgAAhI40VH51AABGZuwl74C"]

@anjana.on(events.NewMessage(pattern='^/start'))
async def start(event):
	async with anjana.action(event.chat_id, 'typing'):
		await asyncio.sleep(3)
	user_id = event.sender_id
	xx = await event.get_chat()
	if event.is_private and not await check_participant(user_id, f'@{Config.CHNAME}', event):
		return
	else:
		await anjana.send_file(event.chat_id, random.choice(s), reply_to=event)
		await event.reply(f"Hey [{xx.first_name}]({xx.id}), I am **MultiUploader**", buttons=[
				Button.url('HB4All', 't.me/hb4all')
			])


@anjana.on(events.NewMessage(pattern='^/help'))
async def help(event):
	async with anjana.action(event.chat_id, 'typing'):
		await asyncio.sleep(3)
	user_id = event.sender_id
	xx = await event.get_chat()
	if event.is_private and not await check_participant(user_id, f'@{Config.CHNAME}', event):
		return
	else:
		helpmsg = '''
➖ **Help Menu | MultiUpload Bot**➖
● `/gofile` - Upload files to GoFile
● `/anonfile` - Upload files to AnonFile
● `/ufile` - Upload files to UFile
● `/bayfiles` - Upload files to BayFiles
● `/tsh` - Upload files to TransferSH
● `/tninja` - Upload files to TmNinja
● `/fileio` - Upload files to FileIO
● `/mixdrop` - Upload files to MixDrop
✦ Made with ♥️ by [HB4All](t.me/hb4all)'''
		await event.reply(helpmsg, buttons=[
				Button.url('HB4All Bot', 't.me/hb4all_bot')
			], link_preview=False)
