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
  const url = "/blog/upload";

  fetch(url, {
    method: "POST",
    headers: {
      "X-CSRFToken": csrftoken,
    },
    body: createFormData(blob),
  })
    .then((response) => {
      if (response.status === 200) {
        return response.json();
      } else {
        throw new Error(
          "이미지 업로드에 실패하였습니다. 다음에 다시 시도해주세요."
        );
      }
    })
    .then((data) => {
      callback(data.url);
    })
    .catch((error) => {
      callback(alert(error.message));
    });
};

const createFormData = (blob) => {
  const formData = new FormData();
  formData.append("images", blob);
  return formData;
};

const submit = document.querySelector(".submit");
const content = document.querySelector(".content");
const postsave = document.querySelector(".post_save");
postsave.addEventListener("click", () => {
  editorcontent = editor.getMarkdown();
  content.value = editorcontent;
  submit.click();
});
