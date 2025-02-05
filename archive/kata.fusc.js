// https://www.codewars.com/kata/570409d3d80ec699af001bf9

/*
fusc(0) = 0
fusc(1) = 1
fusc(2n) = fusc(n)
fusc(2n + 1) = fusc(n) + fusc(n + 1)
*/

function fusc(n) {
    if (n == 0 || n == 1) {
        return n
    }
    if (n % 2 == 0) {
        return fusc(n / 2)
    } else {
        return fusc((n - 1) / 2) + fusc((n + 1) / 2)
    }
}

console.log(fusc(10))
