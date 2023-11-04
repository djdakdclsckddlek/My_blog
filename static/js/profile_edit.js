// 프로필변경 스크립트
// 기존 버튼을 숨긴 후 이미지를 클릭하면 버튼 이벤트 호출
const profile_img = document.querySelector(".profile_img");
const profile_button = document.querySelector(".profile_img_select");

profile_img.addEventListener("click", () => {
  profile_button.click();
});

profile_button.addEventListener("change", () => {
  const file = profile_button.files[0];
  const reader = new FileReader();

  reader.onload = () => {
    profile_img.src = reader.result;
  };

  reader.readAsDataURL(file);
});
