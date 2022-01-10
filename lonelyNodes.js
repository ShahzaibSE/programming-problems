var getLonelyNodes = function(root) {
    if (root === null) return []
    
    const lonelyNodes = []
    const queue = [root]
    
    while (queue.length > 0) {
      const head = queue.shift()
      if (head.left !== null) {
        if (head.right === null) {
          lonelyNodes.push(head.left.val)
        }
        queue.push(head.left)
      }
  
      if (head.right !== null) {
        if (head.left === null) {
          lonelyNodes.push(head.right.val)
        }
        queue.push(head.right)
      }
    }
    
    return lonelyNodes
  }

getLonelyNodes([7,1,4,6,null,5,3,null,null,null,null,null,2])  