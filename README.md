# Django Blog Project

- Django를 이용한 기술블로그를 제작하는 프로젝트 입니다.

## 목차

[1. 목표와 기능](#1-목표와-기능)<br>
[2. 개발 환경 및 배포 URL](#2-개발-환경-및-배포-url)<br>
[3. 개발 일정](#3-개발-일정)<br>
[4. URL 구조](#4-url-구조)<br>
[5. 기능 요구사항 목록](#5-기능-요구사항-목록)<br>
[6. 데이터베이스 모델링(ERD)](#6-데이터베이스-모델링erd)<br>
[7. UI](#7-ui)<br>
[8. 기능](#8-기능)<br>
[9. 개발하면서 느낀 점](#9-개발하면서-느낀-점)<br>

## 1. 목표와 기능

### 1-1. 목표

- 장고를 사용하여 블로그 웹 어플리케이션을 개발한다.
- 각 사용자에 따라 글을 생성, 업데이트, 삭제할 수 있어야 한다.
- 각 글을 읽고 댓글을 작성할 수 있어야 한다.

### 1-2. 기능

- 사용자 인증 및 권한 관리
- 블로그 글 생성, 업데이트, 삭제
- 블로그 글 목록 및 상세보기
- 댓글 + 대댓글 생성 및 관리
- 글 작성시 이미지 업로드 및 관리
- 전체 글 검색, 특정 사용자의 글 검색기능

## 2. 개발 환경 및 배포 URL

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

## 4. URL 구조

## 5. 기능 요구사항 목록

## 6. 데이터베이스 모델링(ERD)

## 7. UI

## 8. 기능

## 9. 개발하면서 느낀 점

<!-- https://www.erdcloud.com/d/Nc268EwQ8d2csQMXe


로그인하고 세션유지시간 1시간
시크릿키 가리기

404 403 페이지

(대댓글) 좋아요

페이지네이션

































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

contentimage 모델 삭제
-->
