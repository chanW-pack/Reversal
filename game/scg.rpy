init python:
    player_name = "FlaSh"                 #플레이어 이름설정할때
    ch_me = Character("player_name", color="#2E64FE",dynamic = True)

define ch_me = Character("종선", color="#9AFE2E") #플레이어 기본
    
define ch_Fr = Character("친구", color="#9AFE2E" , image = "friend")  #친구

define ch_he = Character("민지", color="#FE2EF7") # 메인 히로인

init:
   image friend nomal:
    im.FactorScale("scg/friend/friend.png", 1.5)
    yalign 0.0

   image friend angry:
    im.FactorScale("scg/friend/friend_angry.png", 1.5)
    yalign 0.0 

   image friend happy:
    im.FactorScale("scg/friend/friend_happy.png", 1.5)
    yalign 0.0

   image friend sad:
    im.FactorScale("scg/friend/friend_sad.png", 1.5)
    yalign 0.0

   image friend sosm:
    im.FactorScale("scg/friend/friend_sosmile.png", 1.5)
    yalign 0.0

   image friend wow:
    im.FactorScale("scg/friend/friend_wow.png", 1.5)
    yalign 0.0

   image friend wowsm:
    im.FactorScale("scg/friend/friend_wowsmile.png", 1.5)
    yalign 0.0  

   image Heroine :
    im.FactorScale("scg/H.png", 0.5)
    yalign 0.0
define narrator = Character(None, kind = nvl) #독백노벨ver(나레이터)

define ch_main1 = Character("박은지" , color="#9AFE2E" )  #메인히로인 1
