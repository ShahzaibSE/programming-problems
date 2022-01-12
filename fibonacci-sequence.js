function generateFibonacciSeq(n){
    let n1 = 0, n2 = 1;
    let fib_seq = [];
    fib_seq.push(n1);
    fib_seq.push(n2)
    for(let i=1; i<n; i++){
        nextVal = n1 + n2;
        n1 = n2;
        n2 = nextVal;
        fib_seq.push(nextVal);
    }
    console.log(fib_seq);
    return fib_seq
}

console.log(generateFibonacciSeq(20));