var _ = require('lodash');
let list = ['짜장면', '짬뽕', '볶음밥',]
let number = _.range(1, 46)
let lottery = _.sampleSize(number, 6)
let pick = _.sample(list)
let menu = {
    짜장면: 'https://i.ytimg.com/vi/ZcmPu78rj7w/maxresdefault.jpg',
    짬뽕: 'http://www.whereisit.kr/data/editor/1812/20181220105834_b345b2ec2212303ba57a0cbcd79f2712_g3cf.png',
    볶음밥: 'https://kizmom.hankyung.com/photo/201805/BD.16757778.1.jpg',
}

console.log(`오늘의 메뉴는 ${pick}입니다.`)
console.log(menu[pick])
console.log(menu.짜장면)
console.log(`행운의 번호: ${lottery}`)

let getMin = (a, b) => {
    if (a > b) {
        return b
    }
    return a
}

let getMinFromArray = nums => {
    let min = Infinity
    // nums 배열을 돌면서 min 변수와 비교하여 최소 값을 찾는다.
    for (num of nums) {
        if (min > num) {
            min = num
        }
    }
    return min
}

ssafy = [1, 2, 3, 4, 5]
console.log(getMinFromArray(ssafy))