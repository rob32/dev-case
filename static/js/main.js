var main = (() => {
  var __defProp = Object.defineProperty;
  var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
  var __getOwnPropNames = Object.getOwnPropertyNames;
  var __hasOwnProp = Object.prototype.hasOwnProperty;
  var __export = (target, all) => {
    for (var name in all)
      __defProp(target, name, { get: all[name], enumerable: true });
  };
  var __copyProps = (to, from, except, desc) => {
    if (from && typeof from === "object" || typeof from === "function") {
      for (let key of __getOwnPropNames(from))
        if (!__hasOwnProp.call(to, key) && key !== except)
          __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
    }
    return to;
  };
  var __toCommonJS = (mod) => __copyProps(__defProp({}, "__esModule", { value: true }), mod);

  // frontend/js/main.js
  var main_exports = {};
  __export(main_exports, {
    toggleCommentForm: () => toggleCommentForm
  });

  // frontend/js/scripts/comment.js
  function toggleCommentForm() {
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
  return __toCommonJS(main_exports);
})();
