function plusMinus(arr){
   let positives = 0;
   let negatives = 0; 
   let zeros = 0;
   for(let i = 0; i<arr.length; i++){
       if(arr[i]>0 && arr[i]<=100){
           console.log("Number is positive")
           positives++
       }else if(arr[i]<=100 && arr[i]<0) {
           console.log("Number is negative")
           negatives++
       }else {
           console.log("It's a zero")
           zeros++
       }
   }
   console.log(positives/arr.length.toPrecision(3));
   console.log(negatives/arr.length.toPrecision(3));
   console.log(zeros/arr.length.toPrecision(3));
}

plusMinus([1,1,0,-1,-1])

// --- HackerRank Challenge Status: Completed -- //