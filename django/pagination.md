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

