const csrftoken = document.querySelector('[name="csrfmiddlewaretoken"]').value;
const editor = new toastui.Editor({
  el: document.querySelector("#contents"),
  height: "550px",
  initialEditType: "markdown",
  previewStyle: "vertical",
  hooks: {
    addImageBlobHook: (blob, callback) => uploadImages(blob, callback),
  },
});

const uploadImages = (blob, callback) => {
  let xhr = new XMLHttpRequest();

  //이미지, csrf토큰을 가지고 /blog/upload로 POST요청
  xhr.open("POST", "/blog/upload", true);
  xhr.setRequestHeader("X-CSRFToken", csrftoken);

  const formData = new FormData();
  formData.append("images", blob);

  xhr.send(formData);

  // 받은 imageURL을 이미지의 src로 사용
  xhr.onload = function () {
    if (xhr.status === 200) {
      const imageUrl = JSON.parse(xhr.responseText).url;
      callback(imageUrl);
    } else {
      callback(
        alert("이미지 업로드에 실패하였습니다. 다음에 다시 시도해주세요.")
      );
    }
  };
};

const submit = document.querySelector(".submit");
const content = document.querySelector(".content");
const postsave = document.querySelector(".post_save");
postsave.addEventListener("click", () => {
  editorcontent = editor.getMarkdown();
  content.value = editorcontent;
  submit.click();
});
