# Django Blog Project

- Django를 이용한 기술블로그를 제작하는 프로젝트 입니다.

## 목차

[1. 목표와 기능](#1-목표와-기능)<br>
[2. 개발 환경 및 배포 URL](#2-개발-환경-및-배포-url)<br>
[3. 개발 일정](#3-개발-일정)<br>
[4. 데이터베이스 모델링(ERD)](#4-데이터베이스-모델링erd)<br>
[5. URL 구조](#5-url-구조)<br>
[6. UI](#6-ui)<br>
[7. 기능 요구사항 목록](#7-기능-요구사항-목록)<br>
[8. 개발하면서 느낀 점](#8-개발과정과-느낀점)<br>

## 1. 목표와 기능

### 1-1. 목표

- 장고를 사용하여 블로그 웹 어플리케이션을 개발.
- 각 사용자에 따라 글을 생성, 업데이트, 삭제할 수 있어야 한다.
- 각 글을 읽고 댓글 및 대댓글을 작성할 수 있어야 한다.
- 모바일을 위한 반응형 페이지 제작

### 1-2. 기능

- 사용자 인증 및 권한 관리
- 블로그 글 생성, 업데이트, 삭제
- 블로그 글 목록 및 상세보기
- 댓글 + 대댓글 생성 및 관리
- 글 작성시 이미지 업로드 및 관리
- 전체 글 검색, 특정 사용자의 글 검색기능

## 2. 개발 환경 및 배포 URL

배포 URL:

Python 3.11.4
Django==4.2.6
Pillow==10.1.0
django-markdown-deux==1.0.6

#### [FrontEnd]

<div>
    <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
    <img src="https://img.shields.io/badge/css3-1572B6?style=for-the-badge&logo=css3&logoColor=white">
    <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=white">
    <img src="https://img.shields.io/badge/Tailwind-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white">
    
</div>

#### [BackEnd]

<div>
    <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
    <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">
</div>

#### [DataBase]

<img src="https://img.shields.io/badge/sqlite3-003B57?style=for-the-badge&logo=sqlite&logoColor=white">

### 2-2. 배포 URL

https://github.com/Blood-donation-day/My_blog

## 3. 개발 일정

<img src="readme/WBS.png">

## 4. 데이터베이스 모델링(ERD)

<img src="readme/ERD.png">
<img src="readme/mindmap.png">

## 5. URL 구조

|    `account`    |      name       |                URL                 | 비고 |
| :-------------: | :-------------: | :--------------------------------: | ---- |
|   `회원가입`    |     Signup      |         `accounts/signup/`         |      |
|    `로그인`     |    UserLogin    |         `accounts/login/`          |      |
|   `로그아웃`    |   UserLogout    |         `accounts/logout`          |      |
|    `내 정보`    |   UserProfile   |         `accounts/profile`         |      |
| `회원정보 변경` |   UserUpdate    |         `accounts/update/`         |      |
| `비밀번호 변경` | Change_Password | `accounts/update/change_password/` |      |

|      `blog`      |     name     |           URL           | 비고 |
| :--------------: | :----------: | :---------------------: | ---- |
|    `글 목록`     |   PostList   |         `blog/`         |      |
|    `인기 글`     | PostPopular  |     `blog/popular/`     |      |
| `사용자 글 목록` | PostListUser | `blog/user/<str:blog>`  |      |
|    `글 상세`     |  PostDetail  |     `blog/<int:pk>`     |      |
|    `글 생성`     |  PostCreate  |     `blog/create/`      |      |
|    `글 수정`     |  PostUpdate  | `blog/update/<int:pk>/` |      |
|    `글 삭제`     |  PostUpdate  | `blog/delete/<int:pk>/` |      |
|  `파일 업로드`   |  PostUpdate  |     ` blog/upload`      |      |

## 6. UI

<img src="readme/signuplogin.png">
<br><br>
<img src="readme/profile_edit.png">
<br><br>
<img src="readme/mainpage.png">
<br><br>
<img src="readme/post_user.png">
<br><br>
<img src="readme/post_create.png">
<br><br>

## 7. 기능 요구사항 목록

- 회원가입, 로그인
  <p align="center"><img src="readme/gif/signup.gif" align="center" width="45%">
  <img src="readme/gif/login.gif" align="center" width="45%"></p>

- 글목록 (PC, Mobile)
<p align="center"><img src="readme/gif/post_list_pc.gif" align="center" width="50%">
  <img src="readme/gif/post_list_mobile.gif" align="center" width="36%"></p>

- 프로필 변경
  <p align="center"><img src="readme/gif/porfile_edit.gif">
- 글 쓰기, 글 수정
   <p align="center"><img src="readme/gif/post_create.gif" align="center" width="45%">
   <img src="readme/gif/post_edit.gif" align="center" width="50%">
   </p>
  사진을 드래그하거나 직접 선택해 업로드 할 수 있습니다.

- 댓글, 대댓글
   <p align="center"><img src="readme/gif/post_comment.gif">

- 사용자 글 검색 (PC, Mobile)

<p align="center"><img src="readme/gif/post_search_pc.gif" align="center" width="65%">
  <img src="readme/gif/post_search_mobile.gif" align="center" width="30%"></p>

## 8. 개발과정과 느낀점

### 이슈들

### 마치며

<!-- https://www.erdcloud.com/d/Nc268EwQ8d2csQMXe



404 403 페이지

(대댓글) 좋아요

페이지네이션

검색과 페이지네이션

































이미지나 파일을 저장할때 uuid로 바꿔서 저장
조회수: {{ post.views | add:-1 }}

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.views -= 1
        return super().form_valid(form)

uieditor 적용부분
script파일 나누기

이미지를 저장하는 부분
 if uploaded_file:
            # 파일을 저장합니다.
            file_name = os.path.join('media/blog/images/', uploaded_file.name)
            with open(file_name, 'wb') as f:
                for chunk in uploaded_file.chunks():
                    f.write(chunk)

            # 파일의 URL을 생성합니다.
            file_url = settings.MEDIA_URL + file_name
이미지이름이 곂치면 기존의 이미지가나옴 >> uuid사용하여 랜덤이미지이름
favcon?

contentimage 모델 삭제
-->
