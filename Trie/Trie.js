/**
 * Initialize your data structure here.
 */

function TreeNode(word) {
    (this.val = word), (this.children = {}), (this.isWord = false);
}

let Trie = function () {
    this.root = new TreeNode("");
};

/**
 * Inserts a word into the trie.
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function (word) {
    let parent = this.root;
    for (let i = 0; i < word.length; i += 1) {
        let char = word[i];
        if (!(char in parent.children)) {
            parent.children[char] = new TreeNode("");
        }
        parent = parent.children[char];
        if (i == word.length - 1) {
            parent.isWord = true;
        }
    }
};

/**
 * Returns if the word is in the trie.
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function (word) {
    let parent = this.root;
    for (let i = 0; i < word.length; i += 1) {
        let char = word[i];
        if (!(char in parent.children)) {
            return false;
        }
        parent = parent.children[char];
    }
    return parent.isWord;
};

/**
 * Returns if there is any word in the trie that starts with the given prefix.
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function (prefix) {
    let parent = this.root;
    for (let i = 0; i < prefix.length; i += 1) {
        let char = prefix[i];
        if (!(char in parent.children)) {
            return false;
        }
        parent = parent.children[char];
    }
    return true;
};

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
