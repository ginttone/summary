# paginator

```python
from django.core.paginator import Paginator

objects = ['john', 'paul', 'george', 'ringo', 'jane', 'mag']

page = Paginator(objects,2) #한 화면에 2컨텐츠 씩 디스플레이 된다
print(type(page))
```

debug console

```
page.count
Out[3]: 6
page.num_pages
Out[4]: 3
page.page(2)
Out[5]: <Page 2 of 3>
page2 = page.page(2)
type(page2)
Out[7]: django.core.paginator.Page
page2.object_list
Out[8]: ['george', 'ringo']
page2.has_next()
Out[9]: True <- 뒷 페이지가 있다.
page2.has_previous()
Out[10]: True <- 앞 페이지가 있다.
```



## 적용

board/views.py

```python
from django.core.paginator import Paginator

def list_paginator(request):
    conn = sqlite3.connect('db.sqlite3')
    conn.row_factory = sqlite3.Row
    curs = conn.cursor() #명령어 잡아오는 아이
    curs.execute('select*from polls_economics pe')
    data = curs.fetchall()
    for row in data:
        print(row['title'],row['href'])
    return 0
```

console

```
type(row)
Out[1]: sqlite3.Row
type(data)
Out[2]: list
```

web_config/urls.py

```python
path('board/list_paginator', boardviews.list_paginator),
```



manage.py 실행

```
http://127.0.0.1:8000/board/list_paginator
```



board/views.py

```python
from django.core.paginator import Paginator
def list_paginator(request):
    conn = sqlite3.connect('db.sqlite3')
    conn.row_factory = sqlite3.Row
    curs = conn.cursor() #명령어 잡아오는 아이
    curs.execute('select * from polls_economics pe')
    data = curs.fetchall()
    for row in data:
        print(row['title'],row['href'])
    paginator = Paginator(data,5) #페이지에 5개 출력해줘
    result = dict()
    result['paginator'] = paginator
    # request.GET['page'] #리퀘스트에서 던진 page == ?page
    page_number = request.GET.get('page',1)#첫 페이지가 없으면 1로 초기화 시켜줌
    result['page_object'] = paginator.get_page(page_number)#첫번째 페이지 내용을 page_object에 넘기기
    return render(request, 'board/list_paginator.html', context=result)
```



templates/board/list_paginator.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
    integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

<body>
<div class="container">

    <table class="table table-striped">
        <thead>
            <tr>
                <th>title</th>
                <th>links</th>
            </tr>
        </thead>
        <tbody>
            {% for row in page_object %}
            <tr>
                <td>{{row.title}}</td>
                <td>{{row.href}}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>

    <ul class="pagination">
        <li class="page-item active"><a class="page-link" href="#">Page {{page_object.number}} of {{paginator.num_pages}} </a></li>
        <li class="page-item"><a class="page-link" href="?page={{page_object.next_page_number}}">Next</a></li>
    </ul>
</div>
</body>
</html>
```

# DB 

[DB](https://vuerd.github.io/vuerd/) 는 설계도이다.

png로 저장해서 사용해도됨.

sqlDDL 로 구문저장도 가능



1. 

 ```sqlite
CREATE TABLE category_table
(
  id            INTEGER NOT NULL,
  category_name TEXT    NOT NULL,
  PRIMARY KEY (id)
);

 ```



2. 

 ```sqlite
CREATE TABLE public_date_table
(
  id          INTEGER NOT NULL,
  public_date TEXT    NOT NULL,
  PRIMARY KEY (id)
);

 ```



3. 제약조건이 들어간 테이블 만들기`-` key가 없을 때 (무결성)

 ```sqlite
CREATE TABLE economics_table
(
  id          INTEGER NOT NULL,
  create_date    TEXT    NOT NULL,
  href           TEXT    NOT NULL,
  title          TEXT    NOT NULL,
  id_category    INTEGER NOT NULL,
  id_public_date INTEGER NOT NULL,
  PRIMARY KEY (id),
   FOREIGN KEY (id_category)
    REFERENCES public_date_table (id),
   FOREIGN KEY (id_public_date)
    REFERENCES public_date_table (id)
);
 ```



----

```python
insert into economics_table (
    create_date,
    href,
    id_category,
    id_public_date,
    title)
values (
    ':create_date',
    ':href',
    2,
    3,
    ':title')
;
```



```sqlite
select * from economics_table et
inner join category_table ct
on et.id_category = ct.id;
```

# 스크레핑

```
python -m pip install schedule
```

특정 데이터 테이블에 담은 후 원본은 지운다. 

계속해서 RDB에 차곡차곡 넣어 사용한다.

[scheduling.py](https://schedule.readthedocs.io/en/stable/)

```python
import schedule
import time

def job01():
    print("job01() working...")

def job02(param01,param02):
    print("job02() working...",param01,param02)

#연습 1분단위지만 연습끝나면 시간단위로 등록
schedule.every(1).minutes.do(job01)
#하루에 한번 특정시간에 돌리고 싶을 때
schedule.every().day.at('14:30').do(job01)
#펑션의 파라메터를 넘겨줘야 할 때
schedule.every(1).minutes.do(job02,'p01','p02')

while True:
    schedule.run_pending()
    time.sleep(1)
```

