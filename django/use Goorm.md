# Goorm 사용

#### - 전체흐름 

django

django-admin startproject

python manage.py startapp home

*/views.py

web_config/urls.py

template/*.html



## 1. pycharm에서 설정

pycharm 프로젝트 안의 gitignore 더블클릭  후 

commit 에서 unversionde file 확인

환경파일들이 있는데(.idea) 여기서 idea에 있는 파일들을 

 gitignore파일로 만들경우 그 파일을 사용아예 안하게 됨

그래서 ''환경파일의 묶음 폴더''이름을 gitignore에 기술 

```
.idea
```

후 컨트롤s 해서 저장 하면 Default changelist에 gitignore만 남는다.



* github에 올라간 파일 삭제하기

탐색기에서 .idea(환경파일들) 삭제하기 위해

git push한 파일에 들어가  .idea폴더를 삭제 하고

pycharm commit에서 바뀐부분 선택 후 commit push를 한다.

해당 pycharm project을 껏다가 다시 키고

.gitignore열고 .idea넣고 파일을 저장하면 올리지 않아야 할 부분이 안뜸.

그상태로 Dafalult에있는 .gitignore을 push하면 끝.



## 2. Goorm 사이트로 이동

### 1)컨테이너 생성

* IDE

  * 대시보드

    * 새컨테이너생성

      * 공개범위:Private

      * 템플릿: Github 

        git인증하기 -> 올리고 싶은 git file 선택<u>:multi-django</u>

      * 이름 수정:<u> test05</u>

      * 설명: <u>django container</u>

      * 소프트웨어 스텍: django선택

    * 생성하기

    * (유효하지 않은 리전입니다 : 지역 부분 설정:서울(한국) 하면 됨)

    * 컨테이너 실행하기



### 2) test05 컨테이너 브라우저(최초)

왼쪽 상단을 보면 VS TOOL 과 같이 항목이 나누어져있다.

#### 서버의 실행 (git에서 pull해온 것 띄우기 )

* 오른쪽 상단 재생버튼 = runserver

* 하단에 에러 뜬것 확인

터미널 / 검색/ 리소스 모니터/ 린트/ **new run django**

**종료** :                                      **편집**:

```
mand_line
    utility.execute()
  File "/usr/local/lib/python3.7/site-packages/django/core/management/__init__.py", line 375, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/usr/local/lib/python3.7/site-packages/django/core/management/base.py", line 336, in run_from_argv
    connections.close_all()
  File "/usr/local/lib/python3.7/site-packages/django/db/utils.py", line 224, in close_all
    connection.close()
  File "/usr/local/lib/python3.7/site-packages/django/db/backends/sqlite3/base.py", line 248, in close
    if not self.is_in_memory_db():
  File "/usr/local/lib/python3.7/site-packages/django/db/backends/sqlite3/base.py", line 367, in is_in_memory_db
    return self.creation.is_in_memory_db(self.settings_dict['NAME'])
  File "/usr/local/lib/python3.7/site-packages/django/db/backends/sqlite3/creation.py", line 12, in is_in_memory_
db
    return database_name == ':memory:' or 'mode=memory' in database_name
TypeError: argument of type 'PosixPath' is not iterable
root@goorm:/workspace/test05(master)#
```



* **편집**: 클릭하면 위에 스크립트 확인 됨

* **스크립트**: 마이그랜트 빼기

  && 부터 앞 부분을 지움(지울부분) -이 부분을 지워야 DB에서 문제안생김

```
${python.set.compiler} ${python.set.main.path} migrate && 
```



* **저장후실행**: 클릭 하면 아래처럼 되면 됨

```
System check identified no issues (0 silenced).
July 14, 2021 - 01:13:54
Django version 2.2.4, using settings 'web_config.settings'
Starting development server at http://0.0.0.0:80/
Quit the server with CONTROL-C.
```



* **편집**: URL부분 끝에 **복사하기**버튼 클릭(제3자가 이 서버로 들어올 수 있는 주소)



* 새로운 윈도우 브라우저 열고 **주소 복붙 엔터** 하면 실행된 것 확인가능

```
https://test-ssgom.run.goorm.io/
```

![](md-images/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202021-07-14%20103505-1626226530803.jpg)

* GOORM컨테이너로 돌아와 종료 버튼 클릭 하면고 브라우저 닫으면 종료완료!

컨테이너 에서 ... 말줄임표에서 설정들어가면 정지 됨(test05가 흑색이되면 종료)

컨테이너 에서 ... 말줄임표에서 삭제 누르고 컨테이너 이름 넣으면 삭제됨



## 2. test09 (만들어둔) 컨테이너 서버사용-순환구조 만들기

* 오른쪽 상단 재생버튼에 마우스 올려두면 저장해둔 **new run django** 클릭

* **로컬 내용**을 바꾸고 이 **서버에  적용**하기

  * pycharm project(<u>multi_django</u>)으로 돌아가기

    * home 에 views.py 수정(여기는 main 입니다->여기는 <u>master</u> 입니다)

      ```python
      from django.shortcuts import render
      
      # Create your views here.
      
      from django.http import HttpResponse
      
      def index(request):
          path=request.path
          resultstr=''
          if path =='/home':
              resultstr='<h1>여기는 home 입니다.</h1>'
          else:
              resultstr= '<h1>여기는 master 입니다.</h1>'
          return HttpResponse(resultstr)
      
      def index01(request):
          result = {'first':'juhee','second':'kim'}
          return render(request,'index.html',context=result)
      
      def index02(request):
          result = {'first':request.GET['first'],'second':request.GET['second']}
          return render(request,'index.html',context=result)
      ```

    * 변경내용 git push하기

      commit messege넣고 commit push

* git 브라우저 reload하면 바뀐부분 확인가능

* 바뀐부분을 goorm에 적용
  * 왼쪽 상단에서 git 관리 클릭

    * pull :클릭

      종료 :클릭

      시작 :클릭

    * URL 브라우저에 띄우면 바뀐 부분 확인 가능



참고) pycharm에서 manage가  debug와 run 실행 안된다면 이렇게 실행되게 만든다.

오른쪽 상단 run하고싶은 부분 mange 열고

->  edit Configuration

->  Environment 열기

​	Parameters: <u>runserver</u>

​	python interpreter : Python 3.6(python) 설정: Python Defult 되있는 것을 설정하는 것이 좋음

->  run 클릭



## 4. pycharm 과 goorm로 브라우저 띄운상태

* [CSS:Examples 화면](https://www.w3schools.com/w3css/w3css_templates.asp)  부트스트렙같은 것을 실습할 수 있게 내가 원하는 기능 사용할 수 있게만든 곳 

  여기서 DEMO소스 받아오기

* Try it yourself 클릭

  소스 복사 

* pycharm project에서templates 폴더  아래 index.html에 붙혀넣기 후 저장

* index01브라우저에서 열기 :  http://127.0.0.1:8000/index01



## 5. HTML브라우저에 이미지가 깨진다면?

static 에 이미지 있는지 확인한다! (없다면: static 폴더 만들어서 이미지,내가 원하는 내용 넣기)

* Pycharm project(multi_django) 루트에 static 폴더 만들기

  static: 다운로드파일, 업로드파일, css, 이미지파일 등 이 들어감
  * static 밑에 images 폴더 만들기 

* 브라우저에서 이미지를 다운로드 받기(다른 이름으로 저장)

  탐색기 2개 열고 이미지파일 받아둔것 현 진행중인 images에 복붙

  다운로드 탐색기->

  C:\Develops\multi_django\static\images 탐색기로 이미지 받음

* static폴더에 있는 파일들은 백엔드 단에 있는 function을 거치지 않고 그 내용을 볼 수 있게 한 것

  `http://127.0.0.1:8000/static/images/newyork.jpg` 넣으면 이미지 열려야하는데 django에서 막아둬서 안 열려 그래서 보려면

  * web_config 의 settings 가서 일부내용추가 후 저장

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [   BASE_DIR / "static",		]
```

* 브라우저에 uri에 서버url `http://127.0.0.1:8000/static/images/newyork.jpg`을 넣으면 확인 완료

* 브라우저에 깨진 이미지 복구 혹은 체크

  브라우저에서 깨진 이미지 파일에 스크레핑 하듯이 검사

  브라우저에서 이미지.jpg있는지 검사. 

  파이참에서 index.html 부분 변경(/w3images/이미지.jpg -> /static/images/이미지.jpg)

  ```python
  <p>Name</p>
          <img src="/static/images/bandmember.jpg" class="w3-round w3-margin-bottom" alt="Random Name" style="width:60%">
        </div>
        <div class="w3-third">
          <p>Name</p>
          <img src="/static/images/bandmember.jpg" class="w3-round w3-margin-bottom" alt="Random Name" style="width:60%">
        </div>
        <div class="w3-third">
          <p>Name</p>
          <img src="/static/images/bandmember.jpg" class="w3-round" alt="Random Name" style="width:60%">
        </div>
  ```

  

* 브라우저의 여러이미지 중앙에 계속 뿌리는 이미지 부분

  브라우저에서 mySlides w3-display-container w3-center 찾고

  파이참 index.html에 이미지 위치 넣어주기 

```python
<div class="mySlides w3-display-container w3-center">
    <img src="/static/images/ny.jpg" style="width:100%">
```

​		파이참에서 이제까지 한 것 모두 commit push



* goorm가서 test09 실행(브라우저에  연동된 것 확인 )

git관리 가서 pull

오른쪽 재생 -> new run django 클릭

편집 uri 복사해서 브라우저에서 오픈

'https://test-qsqzy.run.goorm.io/'

index01 바꾼 부분 uri

'https://test-qsqzy.run.goorm.io/index01'



주의) 구름 컨테이너 켜놔야지 url정상 작동하고 무료는 컨테이너 닫으면 종료되!



수업중) 구글드라이버 에 된 부분 올리기 [team project 워크 시트](https://docs.google.com/spreadsheets/d/1r8ylhAr7bfMuCqWVRISXAiGPrQiokdLJbSnUWJKNMjI/edit#gid=0)





## 6.Folium(맵 구현)

### 초기설정

* 프로젝트에 브라우저에 보여주고 싶은 maps폴더 생성 

Terminal 에 입력해서 maps 생성, folium 설치

```
python manage.py startapp maps

python -m pip install folium
```

 

### 입력

maps -> views.py 입력

```python
def home(request):

    return render(request, template_name='maps/home.html')
```



templates-> maps폴더(생성) ->home.html(생성)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>maps home</title>
</head>
<body>
 <h1>maps home</h1>
</body>
</html>
```



web_config -> urls.py 추가

```python
from django.contrib import admin
from django.urls import path
from home import views
from maps import views as mapsviews #views라는 이름이 중복될까봐 이름을 정해줌

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.index),
    path('',views.index),
    path('index01',views.index01),
    path('index02',views.index02),
    path('maps/home',mapsviews.home),
]
```



Folium 쓰려면 위도와경도 잡아와야해 

* views.py 수정

```python
from django.shortcuts import render

# Create your views here.
import folium #위도와 경도를 잡아와야해

def home(request):
    mf = folium.Map([35.3369, 127.7306], zoom_start= 10)#lat_long위도경도 지정 및 얼만큼의 사이즈인지 알려줌
    mf = mf._repr_html_() #한글로 바꿔주는 방법
    first = 'hwasa'
    result = {'mapfolium':mf, 'f01':first} #변수로 딕셔너리형태로 해서 넘겨주려고 준비
    return render(request, template_name='maps/home.html',context=result)
```

rendering이 될 때 function과 html 이둘을 연결해주는 애는 context이다.

result가 딕셔너리로 묶어서 context에 전달해주면 , context가 function과 html을 연결시켜준다.

result의 딕셔너리 키(f01)는 html에서 렌더링되서 사용가능 (  result['f01']={{ f01 }} )

변수가 렌더링됬다는 것을 **{{**변수값 사용할 때**}}**, **{%**코드구문 사용할 때**%}** 를 사용해서 표현해줌.

* home.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>maps home</title>
</head>
<body>
 <h1>maps home</h1>
 <h2>{{ f01 }}</h2> 
 <h2>{{ mapfolium | safe }}</h2>
</body>
</html>
```



##  7. DB 와 SQL lite 

오늘의 목표 : 접근해서 값 가져와서, 화면에 디스플레이 하기

#### SQL lite 사용

Terminal 프로포트 깨끗하게 만들는 명령어 : **cls**

명령어 **dir** :  db.sqlite3 확인

파이참에서 sqlite쓰려고 database navigator 설치 

 ```
 파이참에서 sqlite3 DB를 sql로 다루기 위해서는 'Database Navigator'라는 툴을 설치해야 한다. 설치하는 방법은 [설정]-[Plugin]에서 Database Navigator로 검색하면 된다. 설치하고 나면 플러그인을 실행하기 위해 재시작을 해야 한다.
 ```

* 왼쪽 중간쯤 DB Browser 클릭 

  `+`버튼 누르고 sqlite클릭

화면 열리면 datapase files 의 sqlite클릭하면 오른쪽에 ... 클릭 

지금 하고있는 프로젝트  multi_django의 db.splite3 클릭 

경로 바뀐것 확인후 test connection 클릭 했을때 was successful하고 ok누르면 연결됨

connection 아래 consoles의 connection 열고

.help입력



* schemas 밑에 tables가 없을 땐 

migrate 생성해야해서 terminals에 dir확인해서 manage.py가  있는지 보고

migrate생성 명령어 입력한다  python manage.py migrate



* auth_user로 로그인 관리

쿼리 문을 직접 날려서 하자. 



* 열려있는 db끄기connection->desconnect



* 연결하기

**python manage.py createsuperuser**

Username: <u>**admin**</u>
Email address: **<u>admin@gamil.com</u>**
Password:
Password (again):
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: **y**
Superuser created successfully.

runserver: http://127.0.0.1:8000/admin

하면 로그인창 뜨고 거기에 만든 admin넣으면됨 

![](md-images/%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C-1626245117549.jpg)

![](md-images/%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C%20(1)-1626245197612.jpg)



![screencapture-127-0-0-1-8000-admin-auth-user-2-change-2021-07-14-15_47_17](md-images/screencapture-127-0-0-1-8000-admin-auth-user-2-change-2021-07-14-15_47_17-1626245458886.png)

![](md-images/%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C%20(3)-1626245427659-1626245437830.jpg)





connection 활성화 시키고

consoles -> connention 더블클릭해서 열고

schemas->auth_user 오른쪽 클릭 Extract SQL Statement-> Select statement

완료



엑셀 시트 같은것으로 표현 해보기 

terminal 로 업무창 열기: **python manage.py startapp polls**



* project에서 polls -> **models.py** 

  엑셀의 시트= 데이터베이스의  테이블 = 장고의 클래스

  클래스는 남의 기능을 흡수(상속)받을 수 있는 기능이 있다. (예: 다른 클래스 가져와서 내 추가기능 넣을수 있음)

```python
from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=100)
    public_date = models.DateTimeField()
    votes = models.BigIntegerField()
```

-------



#### class->db에 넣기 

* web_config -> settings 

INSTALLED_APPS에 추가 : 의미) polls ->app.py안에 있는 polls사용 하겠다

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls.apps.PollsConfig',
]
```

* terminal-> **python manage.py makemigrations polls**

```
Migrations for 'polls':
  polls\migrations\0001_initial.py
    - Create model Question
```

* polls-> migrations-> **0001_initial.py생성**이됨

```python
# Generated by Django 3.2.3 on 2021-07-14 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=100)),
                ('public_date', models.DateTimeField()),
                ('votes', models.BigIntegerField()),
            ],
        ),
    ]

```

auto_created=True  유니크한 값이다 . 



* spl문으로 바꾸기2

terminal -> python manage.py sqlmigrate polls 0001

```
CREATE TABLE "polls_question" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
 "question_text" varchar(100) NOT NULL, "public_date" datetime NOT NULL, "votes
" bigint NOT NULL);
COMMIT;
```

* 준비 끝

  

동작

* 적용

**python manage.py migrate**

```
C:\Develops\multi_django>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, polls, sessions
Running migrations:
  Applying polls.0001_initial... OK
```



(아래는 0715 수정예정)

## 7. select 문으로 유무 확인 

* schemas->  tables오른쪽 클릭 reload 하면 tables(12)가 됨

* polls_question->extract-> insert 

```
insert into polls_question (
values (
    time('now'),
    
    'what is ?',
    
    0)
;
```



* polls_question->extract-> select

