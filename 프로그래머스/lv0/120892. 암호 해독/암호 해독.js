function solution(c, code) {
    var answer = '';
    for(let i=0;i<c.length;i++){
        // console.log((i+1)%code, c[i])
        if((i+1)%code === 0){
            answer+=c[i]
        }
    }
    return answer;
}