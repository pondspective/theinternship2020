var afterLoad = require("after-load");
afterLoad("https://theinternship.io", function(html) {
  var search = /<img src"/i;
  var result = html.match(search);
  console.log(result);
});
