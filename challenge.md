# Challenge - FindParent

We are building a command line tool to navigate the file system. We want to add a command that given two file paths, can find the first parent folder that contains both paths.

So for example: 

```jsx

findParent "a/b/c" "a/b/d"
-> "/a/b"
```

Because filesystems might have aliases, we cannot use the file path to find the parent folder at a glance. (i.e. /var might be pointing to /a/b). We need to find the parent folder by navigating the filesystem.

**Challenge**

Given an input that represents a filesystem, and two files, find the closest folder that contains both file paths.

### **Boilerplate**

```tsx
function findParent() {
  //implement this function
}

class FileNode {
	children: Array<FileNode>
	name: string
	
	constructor(name) {
    this.children = [];
    this.name = name;
  }

  addChild(file: FileNode) {
    this.children.push(file)
  }
}

/*
Example input

root ->
  a ->
    c
    d
  b    
*/

const root = new FileNode('root')
const [a,b,c,d] = ['abcd'].split('').map(char => new FileNode(char))      

root.addChild(a)
root.addChild(b)
a.addChild(c)
a.addChild(d)

findParent(root, a, b)
//-> root

findParent(root, c, d)
//-> a

```

**We expect you to:**

1. Provide an elegant and performant implementation of this function
2. An explanation of the algorithm used and a correct implementation

**Tips:**

1. You can solve this challenge in any language of your choosing
2. Create more test cases to ensure correctness beyond the example in the boilerplate
3. Feel free to accommodate the input and format to your convenience - we care about the function implementation the most