// // let 블록 스코프 예제
// {
//     let x = '정운지'
//     console.log(x) // 정운지
//     {
//         let x = 1
//         console.log(x) // 1
//     }
//     console.log(x) // 정운지
// }
// // console.log(x) // 에러
// console.log(typeof x) // undefined

// // let을 var로 바꾸면 결과가 전혀 달라짐.

// let foo
// let bar = undefined

// foo
// bar

// baz

// if (x != 1) {
//     console.log(y)
//     var y = 3
//     if (y === 3) {
//         var x = 1
//     }
//     console.log(y)
// }
// if (x === 1) {
//     console.log(y)
// }
