# Django
- 여러가지 도구를 가진 WEB framework
- Multi Platform 제작( Desktop, Smart Phone, Tablet)을 위해 REST를 사용
- 기본 Django의 형태 Template <-> View <-> Model
- REST의 방식 CRUD
- ORM : Django 와 DB의 연결고리

# 가상환경 구축
- 순수 파이썬으로 구축
    - 가상환경을 모아두는 폴더 생성
        - mkdir venvs
    - 해당 폴더로 이동
        - cd venvs
    - 가상환경 생성
        - python -m venv morning_p
- 가상환경 활성화 시키는 파일 위치까지 이동
    - cd ./morning_p/Scripts
- 가상환경 활성화
    - activate(Window) or . activate(Mac, Linux)
- 최종 프롬포트 형태
    - (web_p) : 윈도우
    - (web_p) $ : 맥/리눅스 사용자 계정
    - (web_p) # : 맥/리눅스 루트 계정

# 가상환경 구축 V.2
- virtualenv venv
- source venv/Scripts/activate
- touch .gitignore
- 참고
    - https://www.toptal.com/developers/gitignore/

# Django 설치
python 3.11.3
- 기존 python version
django 4.2.3 (python 3.11.3 맞춤)
- python -m pip install django==4.2.3
- pip install django

# Django 프로젝트 만들기
- django-admin startproject morning_bot .
- 구조
    - mysite/Django 
    - manage.py 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인의 유틸리티
    - mysite/ 디렉토리 내부에는 프로젝트를 위한 실제 Python 패키지들이 저장
        - __init__.py Python으로 하여금 이 디렉토리를 패키지처럼 다루라고 알려주는 용도의 단순한 빈 파일
        - settings.py 현재 Django 프로젝트의 환경 및 구성을 저장
        - urls.py 현재 Django project 의 URL 선언을 저장
        - asgi.py 재 프로젝트를 서비스하기 위한 ASGI-호환 웹 서버의 진입점
        - wsgi.py 현재 프로젝트를 서비스하기 위한 WSGI 호환 웹 서버의 진입점

## 장고 서버 테스트
- cd morning_bot
- 서버실행 
    - python manage.py runserver
- 메세지 : The install worked successfully! Congratulations! 
- 포트변경 : python manage.py runserver 8080
- IP 변경 : python manage.py runserver 0.0.0.0:8000

## Django rest framework
- pip install djangorestframework
- pip install markdown
- pip install django-filter
- pip install djangorestframework markdown django-filter
- setting.py -> installe_app -> rest_framework



## 앱 생성
- python manage.py startapp reporter
- reporter/view.py 에서 작업
- 기본 테스트 코드 작업
    - python manage.py runserver
    - http://localhost:8000/reporter/

### path() 인수: route
- route 는 URL 패턴을 가진 문자열 입니다.  요청이 처리될 때, Django 는 urlpatterns 의 첫 번째 패턴부터 시작하여, 일치하는 패턴을 찾을 때 까지 요청된 URL 을 각 패턴과 리스트의 순서대로 비교합니다.

- 패턴들은 GET 이나 POST 의 매개 변수들, 혹은 도메인 이름을 검색하지 않습니다. 예를 들어, https://www.example.com/myapp/ 이 요청된 경우, URLconf 는 오직 myapp/ 부분만 바라 봅니다. https://www.example.com/myapp/?page=3, 같은 요청에도, URLconf 는 역시 myapp/ 부분만 신경씁니다.

### path() 인수: view
- Django 에서 일치하는 패턴을 찾으면, HttpRequest 객체를 첫번째 인수로 하고, 경로로 부터 ‘캡처된’ 값을 키워드 인수로하여 특정한 view 함수를 호출합니다. 나중에 이에 대한 간단한 예제를 살펴보겠습니다.

### path() 인수: kwargs
- 임의의 키워드 인수들은 목표한 view 에 사전형으로 전달됩니다. 그러나 이 튜토리얼에서는 사용하지 않을겁니다.

### path() 인수: name
- URL 에 이름을 지으면, 템플릿을 포함한 Django 어디에서나 명확하게 참조할 수 있습니다. 이 강력한 기능을 이용하여, 단 하나의 파일만 수정해도 project 내의 모든 URL 패턴을 바꿀 수 있도록 도와줍니다.

## 데이터베이스 테이블 생성
- python manage.py migrate
- DB 정의 : polls/models.py 작성
- 모델 활성화
    - mysite/settings.py -> INSTALLED_APPS -> "polls.apps.PollsConfig" 추가
- 생성 준비 및 확인 : python manage.py makemigrations polls
- 생성 쿼리문 확인 : python manage.py sqlmigrate polls 0001
- python manage.py migrate
- DB 생성 : python manage.py migrate

## API 사용
- python 쉘 실행 : python manage.py shell

## 관리자(super user) 생성
- python manage.py createsuperuser
- 관리자 페이지 확인 : 
    - python manage.py runserver
    -  http://127.0.0.1:8000/admin/
- 관리 사이트 app 추가 -> polls/admin.py