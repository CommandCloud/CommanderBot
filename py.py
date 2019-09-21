import discord
import random
import datetime
import os

client = discord.Client()

@client.event
async def on_ready():
    print("==================================================================")
    print()
    print("커맨더 봇 (", client.user.id, ") 이 준비되었습니다.")
    print()
    print("==================================================================")
    print()
    print("이제 이 아래로 로그가 표시됩니다.")
    print()
    game = discord.Game("'커맨아 도움' 입력하면 조씁니다!　　　　　　　　　　　　　　　　　　　　　　　　　　　")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if "시발" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "시1발" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "시1234발" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "ㅅㅂ" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "ㅆㅂ" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "ㅅㅃ" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "ㅆㅃ" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "ㅅ1ㅂ" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "ㅅ1234ㅂ" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "새끼" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "새ㄲ1" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "새ㄲl" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "새ㄲI" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "새1끼" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "새1234끼" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "좆" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "ㅅl발" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "ㅅㅣ발" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "병신" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "병1신" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "병1234신" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "ㅄ" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "ㅂㅅ" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "ㅅ발" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "시ㅂ" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "새꺄" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "엿" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "애미" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "애비" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "느금" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "느그" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "섹스" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "tlqkf" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "sex" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "ㅅㅅ" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "쎅쓰" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "쎅스" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "보지" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "보ㅈ1" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "보1지" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "보1234지" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "자지" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "자ㅈ1" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "자1지" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "자1234지" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if "씨발" in message.content:
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : 부적절한 단어로 판단되어 메세지가 삭제됐습니다.")
        await message.delete()
        await message.channel.send("어우 말이 뭐그렇게 험해요;; 다음부턴 바르고 고운말 씁시다 " + message.author.name + "님?")

    if message.content.startswith("커맨아 도움"):
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : '커맨아 도움' 명령어가 실행되었습니다.")
        author = message.guild.get_member(message.author.id)
        embed = discord.Embed(color=0x00FF00)
        embed.add_field(name="커맨아 도움", value="이 도움말을 출력합니다", inline=False)
        embed.add_field(name="커맨아 (할말)", value="커맨더 봇이 당신의 물음에 답합니다!\n( 예 : 커맨아 ㅎㅇ, 커맨아 뒤져 등 )", inline=False)
        embed.add_field(name="커맨아 해든이 (해든이가 먹을 음식)", value="커맨더 봇이 해든이에게 해든이 음식을 먹여줍니다!", inline=False)
        embed.add_field(name="커맨아 따라해 (내용)", value="커맨더 봇이 당신의 말을 따라합니다!", inline=False)
        embed.add_field(name="커맨아 골라 (항목1)/(항목2)/(항목3) ㆍㆍㆍ", value="봇이 당신 대신에 항목들 중에서 골라줍니다!", inline=False)
        embed.add_field(name="커맨아 소개", value="커맨더 봇이 자기소개를 합니다!\n또한 커맨아 소개 리무루 등을 입력하여\nLIU의 다른 멤버들의 소개도 들어볼 수 있습니다.")
        embed.add_field(name="커맨아 embed (제목)/(설명)", value="커맨더 봇이 embed를 만들어줍니다!", inline=False)
        embed.add_field(name="자세한 사항?", value="봇 제작자인 __커맨드 구름#9254__ 이분한테 DM으로 연락주시면 됩니다")
        await author.send(embed=embed)
        await message.channel.send("도움말 DM으로 전달했거든여? 개인메세지 한번 확인해보세영")

    if message.content.startswith("커맨아 ㅎㅇ"):
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : '커맨아 ㅎㅇ' 명령어가 실행되었습니다.")
        rdhi = random.randrange(1, 6)
        if rdhi == 1:
            await message.channel.send("ㅇㅇ " + message.author.name + "님 ㅎㅇㅎㅇ")
        if rdhi == 2:
            await message.channel.send("인사 오지게 박겠습니다 " + message.author.name + " 행님")
        if rdhi == 3:
            await message.channel.send("커맨더 봇 등-장")
        if rdhi == 4:
            await message.channel.send("우ㅘㅏ아앙ㅇ앙ㅇ " + message.author.name + "님 팬이에여ㅓ엉ㅇ 싸인해주세ㅕ어어엉ㅇ")
        if rdhi == 5:
            await message.channel.send("안녕하세요. (진-지)")

    if message.content.startswith("커맨아 하이"):
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : '커맨아 하이' 명령어가 실행되었습니다.")
        rdhi = random.randrange(1, 6)
        if rdhi == 1:
            await message.channel.send("ㅇㅇ " + message.author.name + "님 ㅎㅇㅎㅇ")
        if rdhi == 2:
            await message.channel.send("인사 오지게 박겠습니다 " + message.author.name + " 행님")
        if rdhi == 3:
            await message.channel.send("커맨더 봇 등-장")
        if rdhi == 4:
            await message.channel.send("우ㅘㅏ아앙ㅇ앙ㅇ " + message.author.name + "님 팬이에여ㅓ엉ㅇ 싸인해주세ㅕ어어엉ㅇ")
        if rdhi == 5:
            await message.channel.send("안녕하세요. (진-지)")

    if message.content.startswith("커맨아 안녕"):
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : '커맨아 안녕' 명령어가 실행되었습니다.")
        rdhi = random.randrange(1, 6)
        if rdhi == 1:
            await message.channel.send("ㅇㅇ " + message.author.name + "님 ㅎㅇㅎㅇ")
        if rdhi == 2:
            await message.channel.send("인사 오지게 박겠습니다 " + message.author.name + " 행님")
        if rdhi == 3:
            await message.channel.send("커맨더 봇 등-장")
        if rdhi == 4:
            await message.channel.send("우ㅘㅏ아앙ㅇ앙ㅇ " + message.author.name + "님 팬이에여ㅓ엉ㅇ 싸인해주세ㅕ어어엉ㅇ")
        if rdhi == 5:
            await message.channel.send("안녕하세요. (진-지)")

    if message.content.startswith("커맨아 해든이"):
        msg = message.content[8:]
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : '커맨아 해든이' 명령어가 실행되었습니다. 해든아!", msg, "먹어라~")
        rdhd = random.randrange(1, 5)
        if rdhd == 1:
            await message.channel.send("해든아~ 해든아~ " + msg + " 먹어라~")
        if rdhd == 2:
            await message.channel.send("우리 해든이 " + msg + "먹어야지?^^")
        if rdhd == 3:
            await message.channel.send("여러분들 해든이가 " + msg + " 먹으러 갔데요~!")
        if rdhd == 4:
            await message.channel.send("해냈다! 새우짱!\n허어어어어어어ㅓ억ㄱㄱ\n상상도 못한 해든이 " + msg + "\nㄴ( 해든이 " + msg + " )ㄱ")
        if rdhd == 5:
            await message.channel.send("예~ 췌키라웃\n우리 해든이 " + msg + " 먹네~\n맨날 쎈척하려고 " + msg + " 먹으며 쇼미를 보네~\n이예에스")

    if message.content.startswith("커맨아 뒤져"):
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : '커맨아 뒤져' 명령어가 실행되었습니다.")
        rddt = random.randrange(1, 6)
        if rddt == 1:
            await message.channel.send("네??")
        if rddt == 2:
            await message.channel.send("ㅈㅅ 한데 싫어요 ㅅㄱㅂ")
        if rddt == 3:
            await message.channel.send("저는 죽기 시러오")
        if rddt == 4:
            await message.channel.send("저는 죽기에는 아직 할일이 많다구요!")
        if rddt == 5:
            await message.channel.send("싫은데 내가 왜")

    if message.content.startswith("커맨아"):
        if len(message.content) == 3:
            print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : '커맨아' 명령어가 실행되었습니다.")
            rdah = random.randrange(1, 6)
            if rdah == 1:
                await message.channel.send("네?")
            if rdah == 2:
                await message.channel.send("누구 저 불렀나요?")
            if rdah == 3:
                await message.channel.send("말할거면 제대로 마라세요")
            if rdah == 4:
                await message.channel.send("ㅇ?")
            if rdah == 5:
                await message.channel.send("왜부르노")

    if message.content.startswith("커맨아 따라해"):
        try:
            if message.author.id != 617999186738020353:
                msg = message.content[8:]
                print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : '커맨아 따라해' 명령어가 실행되었습니다. ( 봇이 따라한 내용 :", msg, ")")
                await message.channel.send(msg)
            else:
                print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : '커맨아 따라해' 명령어를 사용하려 했는데 안타깝게 실패했습니다")
                await message.delete()
                await message.channel.send("명령어를 이용해서\n내 기능을 사용하려 하다니\n상상도 못했군")
        except discord.errors.HTTPException:
            print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : '커맨아 따라해' 명령어를 사용하던 도중 오류가 발생했습니다")
            await message.channel.send("최소한 어떤 메세지는 적어주셔야 제가 따라하든 말든 하죠;;")

    if message.content.startswith("커맨아 골라"):
        choice = message.content.split("/")
        a = choice[0].replace("커맨아 골라 ", "")
        del choice[0]
        choice.insert(0, a)
        choicenumber = random.randint(0, len(choice)-1)
        choiceresult = choice[choicenumber]
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : '커맨아 골라' 명령어가 실행되었습니다.\n항목 :", choice, "\n봇이 고른 항목 :", choiceresult)
        await message.channel.send("흐음...\n저는 `" + choiceresult + "` 이거 고름")

    if message.content.startswith("커맨아 소개"):
        if len(message.content) == 6:
            print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : '커맨아 소개' 명령어가 실행되었습니다.")
            await message.channel.send("내 소개를하지 나는 키190m 몸무게 370kg 보다시피 건장한 체격이다.\n또한 윗몸 일으키기 분당300회 팔굽혀펴기 분당200회를 할수있다.")
            await message.channel.send("나로 말하자면 검도5단 유도7단 태권도보라띠 합기도3단 주부9단 눈치100단 무단횡단 황단 경단 구구단 자진모리장단 바위처럼단단 로켓단 복싱6년 도배2년 우유배달6년 드래곤플라이트8만점 무에타이14년 포장이사5년으로 보다시피 살아있는 인간변기라 할수있지.")
            await message.channel.send("이미iq152에 도-달하는 나의화려한경력(서울대,연세대,고려대,성균관대,경찰대,붕대,뒤져서 나오면 100원에 한대)앞에 무릎을 꿇지않는자는없다.")

    if message.content.startswith("커맨아 소개 리무루"):
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : '커맨아 소개' 명령어가 실행되었습니다.")
        await message.channel.send("리무루라는 ~~씹덕~~..\n아니아니 리무루라는 슬라임은\n키 50cm 에 몸무게 1kg 입니다.\n네 맞아요 바로 ~~씹덕~~ 아니아니 슬라임입니다!")

    if message.content.startswith("커맨아 소개 럭키"):
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : '커맨아 소개' 명령어가 실행되었습니다.")
        await message.channel.send("럭키는 LIU 최고의 트롤이라고 말할 수 있습니다.\n럭키는 운터급 수준의 트롤로 항상 우리에게 노답을 안겨줍니다!")
        await message.channel.send("럭키가 트롤인 이유가 뭐냐구요?")
        await message.channel.send("네 맞습니다, 태어날 때부터 상추여서 그랬다고 합니다!")

    if message.content.startswith("커맨아 embed"):
        try:
            split = message.content.split("/")
            a = split[0].replace("커맨아 embed ", "")
            del split[0]
            split.insert(0, a)
            title = split[0]
            Explanation = split[1]
            print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : '커맨아 embed' 명령어가 실행되었습니다.\n제목 :", title, "\n설명 :", Explanation)
            embed = discord.Embed(color=0x00FFAE)
            embed.add_field(name=title, value=Explanation)
            await message.channel.send(embed=embed)
        except IndexError:
            print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : '커맨아 embed' 명령어를 사용하던 도중 오류가 발생했습니다.")
            await message.channel.send("아저씨, 제목만 입력하고 설명은 입력 안하셨어요!\n`커맨아 embed 제목/설명`\n이런식으로 입력하세요 ㅇㅋ?")

    if message.content.startswith("커맨아 소개 재우"):
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : '커맨아 소개' 명령어가 실행되었습니다.")
        await message.channel.send("재우님은 건축실력이 뛰어난 건축가입니다!\nLIU 멤버들 중에서 건축 실력이 공룡급이라고 할 수 있죠.\n그래서 그런지 잠수를 ㅈㄴ탑니다!")

    if message.content.startswith("커맨아 소개 새우짱"):
        print(str(datetime.datetime.today().year) + "/" + str(datetime.datetime.today().month) + "/" + str(datetime.datetime.today().day), str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second), "|", message.author.name, "(", message.author.id, ") : '커맨아 소개' 명령어가 실행되었습니다.")
        await message.channel.send("우짱님은 건축실력이 뛰어난 건축가입니다!\nLIU 멤버들 중에서 건축 실력이 공룡급이라고 할 수 있죠.\n그래서 그런지 잠수를 ㅈㄴ탑니다!")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
