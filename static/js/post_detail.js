const h1s = document.querySelectorAll(".post-content h1");
const h2s = document.querySelectorAll(".post-content h2");
const h3s = document.querySelectorAll(".post-content h3");
const h4s = document.querySelectorAll(".post-content h4");
const h5s = document.querySelectorAll(".post-content h5");
const ols = document.querySelectorAll(".post-content ol");
const ps = document.querySelectorAll(".post-content p");
const imgs = document.querySelectorAll(".post-content img");

h1s.forEach((h1) => {
  h1.classList.add("text-5xl");
  h1.classList.add("font-bold");
  h1.classList.add("mt-4");
});
h2s.forEach((h2) => {
  h2.classList.add("text-4xl");
  h2.classList.add("font-bold");
  h2.classList.add("mt-4");
});
h3s.forEach((h3) => {
  h3.classList.add("text-3xl");
  h3.classList.add("font-bold");
  h3.classList.add("mt-4");
});
h4s.forEach((h4) => {
  h4.classList.add("text-2xl");
  h4.classList.add("font-bold");
  h4.classList.add("mt-4");
});
h5s.forEach((h5) => {
  h5.classList.add("text-xl");
  h5.classList.add("font-bold");
  h5.classList.add("mt-4");
});
ols.forEach((ol) => {
  ol.classList.add("list-decimal");
  ol.classList.add("list-inside");
});
ps.forEach((p) => {
  p.classList.add("mt-4");
});
imgs.forEach((img) => {
  img.classList.add("w-fit");
  img.classList.add("mx-auto");
  img.classList.add("mt-4");
});
