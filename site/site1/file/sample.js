var imageArr = [
  './file/image/image1.jpeg',
  './file/image/image2.jpeg',
  './file/image/image3.jpeg'
];
var imagenum = 0;

$(document).ready(function() {
  $('#image').attr('src', imageArr[imagenum]);
  $('#btn').click(function() {
    if (imagenum == imageArr.length - 1) {
      imagenum = 0;
    } else {
      imagenum++;
    }
    $('#image').attr('src', imageArr[imagenum]);
  });
});
/*
$(function() {
    $('#btn').click(function() {
      imagenum++;
      if (imagenum == 4) imagenum = 1;

      if (imagenum == 1) {
        document.write('<script type="text/javascript" charser="utf-8" src="./file/image1.js"></script>');
      } else if (imagenum == 2) {
        document.write('<script type="text/javascript" charser="utf-8" src="./file/image2.js"></script>');
      } else if (imagenum == 3) {
        document.write('<script type="text/javascript" charser="utf-8" src="./file/image3.js"></script>');
      }
    })
  })
  */
