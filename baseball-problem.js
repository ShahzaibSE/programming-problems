let ops = ["5", "2", "C", "D", "+"]

function playBaseBall(ops){
    var record = [];
    try{
        for(let i=0;i<ops.length;i++){
            if(!isNaN(Number(ops[i]))) {
                record.push(Number(ops[i]));
            }
            if(ops[i] == "C") {
                record.pop()
            }
            if(ops[i] == "D") {
                var previousVal = record.length == 1 ? record[0] : record[i-1]
                record.push(previousVal * 2)
            }
            if(ops[i] == "+"){
                var newRecord = [...record]
                var previousVal1 = record.length == 1 ? record.pop(0) : record.pop(i-1)
                var previousVal2 = record.pop(i-2) 
                var totalPreviousValues = previousVal1 + previousVal2
                newRecord.push(totalPreviousValues)
            }
        }
        return newRecord.reduce((previousVal, currentVal)=>previousVal+currentVal)
    }catch(e){
        throw e
    }
}

console.log(playBaseBall(ops))