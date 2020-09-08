request = require('request');
console.log("it works");
request(url, function (err, res, html) {
    if (!err) {
        var $ = cheerio.load(html);
    }
})

// request(url, function (err, res, html) {
//     if (!err) {
//         var $ = cheerio.load(html);
//     }
// })
// node.js는 js 파일이지만 html 위에서 실행을 하지 않고 독립적으로 실행한다
// 정확히는 node.js 문법이 들어간 js 파일은 js에서 인식을 하지 못한다
// request 모듈을 인식을 하지 못한다. 왜 이러는지는 모르겠다
// 지웠다가 새로 깔아야겠다