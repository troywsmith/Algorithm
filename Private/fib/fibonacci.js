const fibonacci = (n) => {
    let sequence = [0, 1];
    let sum;
    for (let i=2; i<n; i++) {
        sum = sequence[sequence.length - 1] + sequence[sequence.length - 2];
        sequence.push(sum);
    }
    return sequence;
};

console.log(fibonacci(10));