function solution(arr) {
    var answer = 0;
    let ans = []
    for(let i=0;i<arr.length-1;i++){
        for(let j=i+1;j<arr.length;j++){
            ans.push(arr[i]*arr[j])
        }
    }
    return Math.max(...ans);
}