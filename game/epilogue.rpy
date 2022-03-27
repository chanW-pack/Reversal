init python:
  pause = Pause(1)

label epilogue:

play sound "audio/sound/epilogue_drone.wav" 

scene bg_black with pause

"      "

$ renpy.pause(2.5, hard = True)

stop sound fadeout 1.0

"" "......"

play sound "audio/sound/epilogue_drone.wav"   #웅 !소리 늘리고 ...일때 확실히 멈추게

$ renpy.pause(3.5, hard = True)

stop sound fadeout 1.0

"" "하...."

scene bg_myroom with fade

play music "audio/music/bg_Berlin Dream.mp3"

$ renpy.pause(2, hard = True)

ch_me "씨X"

"" "매일 아침 일어날때마다 저 ㅈ같은 소리가 나를 반긴다."

"" "남들은 아직 조금더 자고싶을 오전5시 30분 .. 나에게는 기상시간이다."

"" "매일같이 들리는 환청과 환각으로 나의 생활은 이미 오래전부터 남들과는 사뭇다른 삶을 살아오고있다. "

ch_me "축축해.."

"" "매일아침 일어나면 언제나 오줌을 지렸다거나 땀을 흘렸는지 확인해본다."

"" "그러나 언제나 뽀송뽀송한 이불이다."

ch_me "아 오늘은 더 자고싶은데..."

stop music

play sound "audio/sound/epilogue_drone.wav" fadein 1.0

"" ".."

$ renpy.pause(3.5, hard = True)

stop sound fadeout 2.5

play music "audio/music/bg_Berlin Dream.mp3"

"" "평소라면 1분이나 2분이라도 밍기적거리며 일어났을 아침이지만 오늘따라 심해지는 환청때문에 나는 침대에서 일어날수박에 없었다" 

"" "나는 침대에서 일어나 책상에있는 핸드폰으로 매일듣는 노래를 재생시켰다."

play music "audio/music/bg_Moon Landing.mp3" fadein 1.5 volume 0.4

"" "... ... ..."

$ renpy.pause(2, hard = True)

"" "머리를 비우고 매일듣는 노래를 듣다보니 환청은 점점 멀어지는 것을 느낀다."

ch_me "벌써 2년 가까이 하는 일과지만 익숙해 질수가 없네"

stop music

play sound "audio/sound/phone1.wav" volume 0.5  #-우웅(핸드폰 소리)  여기 소리가안남 낼꼭바꾸기

with hpunch

"" "~~~"

$ renpy.pause(0.5, hard = True)

stop sound fadeout 1

"" "이시간에 맞춰 연락올사람은 {color=#FE2EF7} 민지 {/color} 말곤없다."  # {b} 글자 {/b} //굵게  {color= #컬러코드 } 글자 {/color} //색

"" "카톡내용~~~응애응애~ (대충 학교 늦지말라고 하는거)"

ch_me "넹~"

# ch_he "주 잘잤어?"
# ch_me "응 환청만 없었으면 잘잤지"
# ch_he "오늘도 그 환청이야? 그 바람소리같다는.."
# ch_me "어 매일 똑같지 뭐 이제 2년이나 돼서 슬슬 적응도 되가는 중이야"
# ch_he "그러면서 매일 학교에서 졸고있나요 주?"
# ch_me "음;; 솔직히 아무리 시간이 지나도 적응못할것같다..."


#---0725
# 어렸을때부터 친구였던 @@ 다른사람들은 환각과 환청이있는 나를 피하기 급급했지만 @@만은 아니었다 나의 이야기를 들어주고 고통을 이해해주는 사람은 @@이 유일했다..불쌍한 내인생ㅠ

# 주-그럼 이따가 학교에서 보자
# @@-그랭 늦지말고 오세요~


play sound "audio/sound/ZOOM0007.mp3" 
scene bg_black with pause             #부스럭부스럭 and 뚜벅뚜벅소리 (까만화면에서)
$ renpy.pause(1, hard = True)
stop sound 

scene bg_roomday with fade
$ renpy.pause(1, hard = True)

scene bg_park with fade
play music "audio/music/bg_klankbeeld river.mp3"
$ renpy.pause(2, hard = True)

"" "학교에 가기전 간단하게 아침밥을 때운뒤 세안후 학교갈 준비를 하고 7시 정도에 집에서 나간다" 
"" "학교가기전까지 1시간의 시간 이시간을 나는 공원에 앉아 사람들을 관찰한다 출근하는 사람들을 보다보면 매일 보이는 사람들이 지나다니는걸 알 수 있다 "

ch_me "저 형은 오늘 지각인가"

"" "이렇게 사람들을 보다보면 다른 사람들의 아침패턴을 알 수 있다. 다른 사람들의 아침패턴을 알고 있다는 것 만으로도 왠지 모르게 기분이 고양된다." 
"" "그리고 이시간만이 나에게 유일하게 환청과 환각이 없이 뚜렷한 시간이다."



scene bg_schoolday with fade
play music "audio/music/bg_school song.mp3" fadein 1.5 volume 0.4 # <학교>
$ renpy.pause(2, hard = True)

scene bg_hallway with fade
$ renpy.pause(1, hard = True)

#show friend nomal with dissolve   fade =화면전체 disslove 캐릭터만웨이브`
show Heroine with dissolve 
ch_he "주 오늘은 늦지 안고 잘 왔네?"
ch_me "오늘은 사람들이 다들 빠르게 출근하더라고"
ch_he "오늘도 공원에서 사람구경한거야?"
ch_me "공원에서의 시간만이 가장 정신이 뚜렷하니까"
ch_he "음 다음에는 나도같이 갈래?"
ch_me "별로 재미없을탠데"
ch_he "주가 가장 좋아하는 시간을 같이 있고싶거든^^"
ch_me "니 맘대로 해라"

# 0802

"" "말은 이렇게 했지만 민지가 나를 생각해줬다는 것을 알 수 있다."

ch_he "그럼 곧 수업시간이니까 나중에 봐~"
ch_me "그래"

scene bg_classroom with fade
$ renpy.pause(1, hard = True)
"" "    <수업시간>     "
"선생님" "여기서는 이런식으로 대입해서..."
"" "오늘은 날씨가 좋네.."
"선생님" "그럼 17번 나와서 이문제 풀어볼까?"
"선생님" "....."
"선생님" "17번?? 17번 종선이구나 종선아"
ch_me "에? 아 네.."
"선생님" "수업시간에 멍때리는거보니 이미 다 알고있는 내용이겠지? 한번 나와서 풀어보렴"
ch_me "아.. 네"

"" "수업시간에는 주로 멍을때리거나 잠을잔다. 선생님이 싫다거나 수업이 재미없어서가 아니다 그냥 내가 다 알고 있는 내용 일뿐이라 시시해서 그런거다."

"선생님" "오 정확하게 풀었네 그래 다음부터는 수업시간에 멍때리지 말고 열심히 들어라!"
ch_me "네 알겠습니다."

"" "어렸을때부터 열정적인 부모님덕에 항상 공부는 열심히 해왔다 지금도 집에서 꾸준히 과외를 들으며 학교진도정도는 앞서 나간지도 오래다"
"" "하지만 이상하게도 공부와 병행하는 운동은 아무리 노력을 해도 실력이 늘어날 기세도 않보인다"

#여기서 끝??