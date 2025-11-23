/**
 * Definition for a binary tree node.
 */
class TreeNode {
    constructor(val, left, right) {
        this.val = (val === undefined ? 0 : val);
        this.left = (left === undefined ? null : left);
        this.right = (right === undefined ? null : right);
    }
}

/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrderBottom = function(root) {
    if (!root) return [];
    
    const ans = [];
    const queue = [root];
    
    while (queue.length > 0) {
        const levelSize = queue.length;
        const level = [];
        
        for (let i = 0; i < levelSize; i++) {
            const cur = queue.shift();
            level.push(cur.val);
            
            if (cur.left) queue.push(cur.left);
            if (cur.right) queue.push(cur.right);
        }
        
        ans.push(level);
    }
    
    // Reverse the result to get bottom-up order
    return ans.reverse();
};

export { TreeNode, levelOrderBottom };
