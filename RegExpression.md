# [Regular Expression](https://regexr.com/)

regular expression processing 은 for문을 돌리는 것과 같다. 

`/   /g` global 슬레쉬 사이에 넣으면 전체에서 찾아준다. 

`a | b` 단어 단위로 매칭시켜 사용. a 또는 b


### Number Nuer Numr

`Nu(be|e|m)r` grouping 예를들어 Number Nuer Numr 을 모두 선택하고 싶을때 공통 Nu r은 동일하지만 중앙이 다를때 사용  


### color colour colouuuur colouuhur coollouuur

colou`?`r : **color colour** colouuuur colouuhur coollouuur 을 바로 앞 문자까지 선택하고 싶을때 사용

colou`*`r : **color colour colouuuur** colouuhur coollouuur 을 바로 앞 문자까지 선택하고 싶을때 사용

colou`+`r : color **colour colouuuur** colouuhur coollouuur유일하게 바로 앞 글자(u)가 하나라도 등장 해야지만 동작함

colou`{1,3}`r :  color **colour** colouuuur colouuhur coollouuur

[a-z] : **color colour colouuuur colouuhur coollouuur** 전체 소문자 알파벳 선택 

[colru]: **color colour colouuuur colouu** h **ur coollouuur** (c|o|l|r|u) 해당 글자 들어간 것 찾아줌


### 예제 문장
```
02-4723-3823
023-423-3823
Man: Is this the right room for an argument?
Other Man: I've told you once.
Man: No you haven't!
023-472-3823
023-4723-3923
034-4723-3833
031-423-3813
023-723-3123
Other Man: Yes I have.
Man: When?
Other Man: Just now.
Man: No you didn't!
Other Man: Yes I did!
Man: You didn't!
Other Man: I'm telling you, I did!
Man: You did not!
Other Man: Oh I'm sorry, is this a five minute argument, or the full half hour?
Man: Ah! (taking out his wallet and paying) Just the five minutes.
Other Man: Just the five minutes. Thank you.
Other Man: Anyway, I did.
Man: You most certainly did not!
Other Man: Now let's get one thing quite clear: I most definitely told you!
Man: Oh no you didn't!
Other Man: Oh yes I did!
```

* Q1. Man ,  Other 만 선택하기

A1. Man|Other

* Q2.I , room 만 선택하기

A2.(I|room)

* Q3.소문자만 선택하기

A3.[a-z]

* Q4.대문자만 선택하기

A4.[A-Z]

* Q5.대 소문자 제외 선택하기

A5.[^a-zA-Z]

* Q6.대 소문자 제외하고 연결되있는 단어단위로 선택하기

A5.[^a-zA-Z]+


### 숫자 찾기

`[0-9]` : 숫자만 선택하기

`[0-9]+` : 숫자만 묶음 단위로 선택하기

`[0-9]+-[0-9]` : 숫자 묶음 단위로 -과 함께 선택하기(숫자로 시작하고 하이픈 단위로 찾음)

예)**02-4723**-3823 

0*-0****

Q6.전화번호만 선택하기(3-4-4)-{n,m}

A6.
