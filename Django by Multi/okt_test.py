from konlpy.tag import Okt

txt = "아버지가방에들어가신다."
okt = Okt()

sentence = okt.morphs(txt)

sentence

#python -m pip install JPype1==1.2.0
