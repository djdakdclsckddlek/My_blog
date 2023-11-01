# My_blog Project

블로그를 만들어보자.

<!-- https://www.erdcloud.com/d/Nc268EwQ8d2csQMXe


로그인하고 세션유지시간 1시간
시크릿키 가리기

모바일 화면 글자키우기

404 403 페이지

상세글, 글삭제

댓글, 대댓글
좋아요 글검색



페이지네이션? or 스크롤내리면 추가로딩

썸네일 위에는 round밑에는 round제거

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
-->
