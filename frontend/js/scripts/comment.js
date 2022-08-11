export function toggleCommentForm() {
  let btn = document.getElementById("expandable-btn");
  let div = document.getElementById("expandable-div");

  if (div.style.display === "block") {
    div.style.display = "none";
    btn.innerText = "Leave a comment";
  } else {
    div.style.display = "block";
    btn.innerText = "Hide Comment Form";
  }
}
