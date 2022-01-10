function solution(message, K) {
    var result = message.substring(0,K)
    if ((K >=1 && K <= 500) && message != "") {
        if (result.length > K || result.slice(-1) == " " ) {
            console.log("Empty String")
        }else {
            console.log(result)
        }
    }
}

solution("To crop or not to crop", 21)