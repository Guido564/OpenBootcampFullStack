function fibonacci(num) {
    if (num == 0) {
        return 0
    }
    if (num == 1) {
        return 1
    } else {
        return (fibonacci(num - 2) + fibonacci(num - 1))
    }
}

console.log(fibonacci(9))

function fibonacciLista(num) {
    if (num === 1) return [1]
    if (num === 2) return [1, 1]
    let list = [1, 1]
    for (let i = 2; i < num; i++) {
        list.push(list[i - 1] + list[i - 2])
    }
    return list
}

console.log(fibonacciLista(6))