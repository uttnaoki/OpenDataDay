var imageArr = [
  './file/image/image1.jpeg',
  './file/image/image2.jpeg',
  './file/image/image3.jpeg'
];

var jsArr = [
  './file/file1.js',
  './file/file2.js',
  './file/file3.js'
];

var imagenum = 0;
var filenum = 0;
/*
document.write('<img src="./file/image/image1.jpeg">');
document.write("aaaa");
*/

$(document).ready(function() {
  $('#file').attr('src', jsArr[filenum])
  $(#btn).click(function() {
    if (filenum == jsArr.length - 1) {
      filenum = 0;
    } else {
      filenum++;
    }
    $('#file').attr('src', jsArr[filenum]);
  })
})

/*
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
*/
