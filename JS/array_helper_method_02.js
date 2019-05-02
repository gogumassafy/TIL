// 4. reduce
/*
    - map은 배열의 각 요소를 변형한다면, reduce는 배열 자체를 변형
    - 배열을 '값 하나'로 줄이는 동작(ex 배열의 합, 배열의 평균..)
    - reduce의 첫번째 매개변수는 '누적값(전 단계의 결과)' 이다.
    - 두번째 매개변수 현재 배열요소, 현재 인덱스, 배열 자체 순으로 들어간다.
*/
// 4-1 총합
const SSAFY = [3, 9, 2, 7]
const sum = SSAFY.reduce((total, x) => total + x, 0)
console.log(sum)

// 4-2 평균
const avg = SSAFY.reduce((total, x) => total + x, 0) / SSAFY.length
// const avg = SSAFY.reduce((average, x) => average + x/SSAFY.length, 0)
console.log(avg)

// 4-3 초기값 생략
// 초기값이 생략되면 누적값은 배열의 첫번째 요소가 초기값이 된다.
const sum_2 = SSAFY.reduce((total, x) => total + x)
console.log(sum_2)

// 5. find
/*
    - 찾은 요소 한가지만 return한다.
    - '조건에 맞는 인덱스가 아니라 요소 자체를 원할 때' 사용
    - 배열 검색 헬퍼들: find, indexOf, lastIndexOf, findIndex, some, every
*/
const USERS = [
    {name: 'Thor'},
    {name: 'Steve Rogers'},
    {name: 'Tony Stark'},
]

const ironMan = USERS.find(function(user) {
    return user.name == 'Tony Stark'
})

// ES5
for (var i = 0; i < USERS.length; i++) {
    if (USERS[i].name === 'Tony Stark') {
        user = USERS[i]
        break
    }
}
console.log(ironMan)

// 5-1 users 중에 admin 권한을 가진 요소를 찾아서 admin 에 저장하자.
const PEOPLE = [
    { id: 1, admin: false },
    { id: 2, admin: false },
    { id: 3, admin: true },
 ]

 const admin = PEOPLE.find(function(person) {
     return person.admin
 })
 console.log(admin)

// 5-2 accounts 중에서 잔액이 12 인 object 를 account 에 저장하자.
const ACCOUNTS = [
    { balance: -10 },
    { balance: 12 },
    { balance: 0 }
]

const account = ACCOUNTS.find(function(acc) {
    return acc.balance === 12
})
console.log(account)

// 6. some & every
/*
    - 기존처럼 대상 배열에서 특정 요소를 뽑거나, 배열을 return 하지 않고, 조건에 대해 boolean 값을 return
    - some : 조건에 맞는 요소를 찾으면 즉시 검색을 멈추고 true / 찾지 못하면 false
    - every : 해당 배열의 모든 요소가 조건에 맞아야 true / 그렇지 않다면 false
        - 즉, every는 조건에 맞지 않는 요소를 찾아야만 검색을 멈추고 false를 return
*/

const arr = [1, 2, 3, 4, 5]
arr.some(x => x%2 === 0) // true



// 6-1 컴퓨터의 램이 16보다 큰 요소가 있는지를 some 과 every로 비교
const COMPUTERS = [
    { name: 'macbook', ram: 16 },
    { name: 'gram', ram: 8 },
    { name: 'series9', ram: 32 },
]

const everyComputer = COMPUTERS.every(function (computer) {
    return computer.ram > 16
})

const someComputer = COMPUTERS.some(function (computer) {
    return computer.ram > 16
})

// 6-2 USERS 배열에서 모두가 hasSubmitted 인지 아닌지를 hasSubmitted 에 저장하라
const USERS1 = [
    { id: 21, hasSubmitted: true },
    { id: 33, hasSubmitted: false },
    { id: 712, hasSubmitted: true},
]

const everyUser = USERS1.every(function (user) {
    return user.hasSubmitted
})

console.log(everyUser)

// 6-3 REQUESTS 배열에서 각 요청들 중 status 가 pending 인 요청이 있으면, inProgress 변수에 true 를 저장하라.
const REQUESTS = [
    { url: '/photos', status: 'complete' },
    { url: '/albums', status: 'pending' },
    { url: '/users', status: 'failed' },
]

const someRequest = REQUESTS.some( request => request.status === 'pending')

console.log(someRequest)