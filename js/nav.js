(function () {
  var toggle = document.querySelector(".navtoggle");
  var nav = document.getElementById("site-nav");
  if (!toggle || !nav) return;
  toggle.addEventListener("click", function () {
    toggle.classList.toggle("active");
    var ul = nav.querySelector("ul");
    if (ul) ul.classList.toggle("show");
  });
})();
