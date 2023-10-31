# My_blog Project

블로그를 만들어보자.

<!-- https://www.erdcloud.com/d/Nc268EwQ8d2csQMXe


로그인하고 세션유지시간 1시간
시크릿키 가리기

[글생성, 글수정]

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
-->
