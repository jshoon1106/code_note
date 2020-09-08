function solution(arr) {
    let min = arr[0];
    for (let i = 0; i < arr.length-1; i++) {
        if (min > arr[i+1]) {
            min = arr[i+1];
            arr[i+1] = arr[0];
            arr[0] = min;
        }
    }
}
