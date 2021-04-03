import discord
import asyncio
import datetime
import pytz

client = discord.Client()

token = "ODI0NDYzMzE1NDkyOTI5NTc2.YFvvTA.-4Z-s5eVUwIHYEOEta_bGJ5lZqg"

@client.event
async def on_ready():

    print(client.user.id) 
    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다.')
    game = discord.Game("테리와 대화를 하고싶다면 '테리야 명령어' 를 입력해주세요!") 
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "테리야": 
        await message. channel.send ("저 부르셨어요?") 

    if message.content == "테리야 안녕":
        await message. channel.send ("{}님 반가워요! 저는 테리라고해요!".format(message.author, message.author.mention))
  
    if message.content == "테리야 안녕!":
        await message. channel.send ("{}님 반가워요!!".format(message.author, message.author.mention))

    if message.content == "테리야 빵야":
        await message. channel.send ("으악! 도망가~") 

    if message.content == "테리야 방탄소년단":
        await message. channel.send ("💜방탄오빠들 멋있어요~!💜") 

    if message.content == "테리야 방탄소년단 응원":
        await message. channel.send ("💜김남준! 김석진! 민윤기! 정호석! 박지민! 김태형! 전정국! BTS! 꺄아~💜") 
  

    if message.content == "테리야 귀여워":
        await message. channel.send ("놀리시는거죠..?! (**부끄**)") 

    if message.content == "테리야 명령어":
        embed = discord.Embed(colour=discord.Colour.blue(), title="📋테리의 명령어 목록📋",description="테리야, 테리야 안녕, 테리야 안녕! 테리, 테리야 빵야, 테리야 방탄소년단, 테리야 방탄소년단 응원, 테리야 귀여워, 테리야 잘했어, 테리야 고마워, 테리야 너여자야?, 테리야 사랑해, 테리야 10초타이머, 테리야 지워, 테리야 정보, 테리야 시간 이에요!,") 
        await message.channel.send(embed=embed) 

    if message.content == "테리야 너여자야?":
        await message. channel.send ("그..그럼요!!😫") 

    if message.content == "테리야 도움말":
        await message. channel.send ("테리야 명령어로 다시부탁드려요!") 

    if message.content == "테리야 사랑해":
        await message. channel.send ("저..저도..😖 (**부끄**)") 

    if message.content == "테리야 도움":
        await message. channel.send ("테리야 명령어로 다시부탁드려요!") 

    if message.content == "테리야 초대링크":
        await message. channel.send ("https://discord.com/api/oauth2/authorize?client_id=824463315492929576&permissions=8&scope=bot 여기있어요!") 

    if message.content == "테리야 잘했어":
        await message. channel.send ("네..네에! (부끄)")

    if message.content == "테리야 고마워":
        await message. channel.send ("헤헷, 이거가지고 뭘요!") 

    if message.content == "테리":
        await message. channel.send ("💕테리테리💕")  

    if message.content == "태리야":
        await message. channel.send ("태리가 아니라 테리라구요!! 😤") 
 
    if message.content == "테리야 좋은아침":
        await message. channel.send ("좋은 아침이에요!")

    if message.content == "테리야 10초타이머": 
        await asyncio.sleep(10)
        await message.channel.send(f"{message.author.mention}, 10초가 지났어요!")

    if message.content.startswith ("테리야 지워"):
        i = (message.author.guild_permissions.administrator)

        if i is True:
            amount = message.content[7:]
            await message.channel.purge(limit=1)
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="메시지 삭제 알림", description="최근 디스코드 채팅 {}개가\n관리자 {}님의 요청으로 정삭적으로 삭제되었어요!".format(amount, message.author), color=0x000000)
            embed.set_footer(text="Bot Made by. Jeongyul#9926", icon_url="https://discordapp.com/channels/691615852620939274/703908401381376000/711859989177958410")
            await message.channel.send(embed=embed)
        
        if i is False:
            await message.channel.purge(limit=1)
            await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention))

    if message.content == "테리야 쟤이상해":
        await message. channel.send ("그러게요.. 왜저럴까요..?")

    if message.content == "테리야 귀멸의칼날":
        await message. channel.send ("전집중의 호흡..!")

    if message.content == "테리야 부활해":
        await message. channel.send ("테리는 여기있는데요?")

    if message.content == "테리야 때려":
        await message. channel.send ("예 형님, 모가지를 비틀까요?")

    if message.content == "그래,":
        await message. channel.send ("넵, (**뽀각**)")    
  
    if message.content == "테리야 너바보야?":
        await message. channel.send ("테리 바보아니에요! ``💕 - 3``")   

    if message.content == "테리야 신고해":
        await message. channel.send ("112 전화연결중입니다. (**삐리리-리**)") 

    if message.content == "테리야 잘가":
        await message. channel.send ("테리는 퇴근하러가요! 좋은하루되세요!")

    if message.content == "테리야 울어":    
        await message. channel.send ("ㅠㅜㅜㅠㅜㅠㅜㅠㅜㅠㅜㅠㅜㅠㅜㅠㅜㅜㅠㅜㅠㅜㅠㅜㅠㅜㅠㅜ")

    if message.content.startswith("테리야 투표"):
        vote = message.content[7:].split("/")
        await message.channel.send("투표 - " + vote[0])
        for i in range(1, len(vote)):
            choose = await message.channel.send("```" + vote[i] + "```")
            await choose.add_reaction('👍')        

    if message.content == "테리야 마법":
        await message. channel.send ("윙가르디움레비오우사!")

    if message.content == "테리야 뭐해?":
        await message. channel.send ("열심히 일하는중입니다!") 

    if message.content == "테리야 좋아하는노래":
        await message. channel.send ("테리는 방탄소년단님들의 BLUE&GREY 라는 노래를 좋아해요! 듣고싶으시다면 https://youtu.be/O-C0oV2HXaU 이 링크로 들어가주세요!")

    if message.content == "테리야 좋아하는 가수":
        await message. channel.send ("테리는 방탄소년단님들을 좋아해요! 생각하면 생각할수록..설레는거있죠?! 😍 방탄소년단님들의 유튜브채널을 보고싶다면 https://www.youtube.com/c/bangtantv/featured 이 링크로 들어가주세요!")

    if message.content == "테리야 정율이":
        await message. channel.send ("정율사장님만 생각하면..윽..퇴사하고싶단생각밖에..노코멘트할게요..😥") 
        
    if message.content == "테리야 정율":
        await message. channel.send ("악질사장 정ㅇ..읍으읍")

    if message.content == "테리야 ㅅㅅ":
        await message. channel.send ("세수를 말씀하시는건가요? 테리는 기계라 세수를안해도되요!")

    if message.content == "테리야 Merejin":
        await message. channel.send ("Merejin..? 멍청하신분..? 사장님한테 얘기 많이들었어요!")

    if message.content == "테리야 몇살이야?":
        await message. channel.send ("테리는 몇살인지 잘 모르지만 사장님이 14살이라고 말씀해주셨어요!") 

    if message.content == "테리야 크시알아?":
        await message. channel.send ("헉! 대선배님! 잘알죠!! 크시선배보고 많이배웠어요!")

    if message.content == "테리야 DM": # 메세지 감지
        await message.channel.send ("{} | {}, 반가워요!".format(message.author, message.author.mention))
        await message.author.send ("{} | {} 님, 반가워요!".format(message.author, message.author.mention))

    if message.content == "테리야 정보": # 메세지 감지
        embed = discord.Embed(title="정보", description="",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x62c1cc)

        embed.add_field(name="자기소개", value="안녕하세요! 저는 테리라고해요! 저는 당신의 제일친한 친구가되고싶어요! 노력할테니 예쁘게봐주세요!!", inline=False)
        embed.add_field(name="초대", value="테리를 서버에 초대하고싶으시다면 'https://discord.com/api/oauth2/authorize?client_id=824463315492929576&permissions=8&scope=bot' 이곳에서 초대를해주세요!", inline=False)

        embed.add_field(name="도움말", value="테리에 대해 궁금하다면 '테리야 명령어' 또는 Jeongyul#7980로 DM을 보내주세요!", inline=True)
        
        embed.set_footer(text="Bot Made by. Jeongyul#7980", icon_url="https://media.discordapp.net/attachments/804287392281395270/827120965627543552/1.png?width=567&height=567")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/804287392281395270/827120965627543552/1.png?width=567&height=567")
        await message.channel.send (embed=embed)

    if message.content == "테리야 수고많았어": # 메세지 감지
        await message.channel.send ("{}님 덕분인걸요! 감사해요!".format(message.author, message.author.mention))

    if message.content.startswith("테리야 시간"):
        a = datetime.datetime.today().year
        b = datetime.datetime.today().month
        c = datetime.datetime.today().day
        d = datetime.datetime.today().hour
        e = datetime.datetime.today().minute
        await message.channel.send (str(a) + "년 " + str(b) + "월 " + str(c) + "일 " + str(d) + "시 " + str(e) + "분 이에요!") 

    if message.content == "테리야 정율정보": # 메세지 감지
        embed = discord.Embed(title="정보", description="",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x000000)

        embed.add_field(name="자기소개", value="안녕하세요! 저는 정율이라고하는 테리개발자입니다!", inline=False)
        embed.add_field(name="정보", value="즐겨하는 게임은 메이플스토리2, 마인크래프트 입니다!", inline=False)
        embed.add_field(name="그외", value="테리를 서버에 초대하고싶으시다면 'https://discord.com/api/oauth2/authorize?client_id=824463315492929576&permissions=8&scope=bot' 이곳에서 초대를해주세요!", inline=False)

        embed.add_field(name="도움말", value="테리에 대해 궁금하다면 '테리야 명령어' 또는 Jeongyul#7980로 DM을 보내주세요!", inline=True)

        embed.set_footer(text="Bot Made by. Jeongyul#7980", icon_url="https://cdn.discordapp.com/attachments/804287392281395270/827479234560917514/20210402_173431.jpg")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/804287392281395270/827479234560917514/20210402_173431.jpg")
        await message.channel.send (embed=embed)

    if message.content == "테리야 여리":
        await message.channel.send ("악질사장 김여ㄹ..읍읍")



client.run(token) 
