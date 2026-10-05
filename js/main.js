// Cursor-follow cover preview on the work index (fine pointers only).
(function () {
  if (!window.matchMedia('(hover: hover) and (pointer: fine)').matches) return;

  var rows = document.querySelectorAll('.row[data-cover]');
  if (!rows.length) return;

  var preview = document.createElement('img');
  preview.className = 'preview';
  preview.alt = '';
  document.body.appendChild(preview);

  rows.forEach(function (row) {
    row.addEventListener('mouseenter', function () {
      preview.src = row.dataset.cover;
      preview.classList.add('on');
    });
    row.addEventListener('mouseleave', function () {
      preview.classList.remove('on');
    });
    row.addEventListener('mousemove', function (e) {
      var x = Math.min(e.clientX + 24, window.innerWidth - preview.offsetWidth - 16);
      var y = Math.min(e.clientY + 24, window.innerHeight - preview.offsetHeight - 16);
      preview.style.transform = 'translate(' + x + 'px,' + y + 'px)';
    });
  });
})();
