### Python Tutorial
This is a concise python tutorial for beginners. The purpose is to provide an 
introduction to Python while keeping enough interest. 

This is an "internet book" in the sense that it refers to many internet links
for details. There are already many excellent resources on the internet by
experts and seasoned practitioners, there is no point to reinvent wheels.

What we do here is to outline certain topics in Python that in our view are
fundamental to beginners:
- Introduce the concepts of programming
- Python specified syntax and building blocks.
- How to translate conceptual thinking into code.

We limit topics to 10, and the scope of topics to how to use in practice, 
plus important programming concepts and concerns. The goal is to let readers
get a feel on Python programming and can explore further in the future. 

Official Python tutorial is here:
https://docs.python.org/3.8/tutorial/index.html

A simple-to-follow tutorial is at
https://www.w3resource.com/python/python-tutorial.php 

[Why we pick Python](docs/why_python/why_python.md)

[Python Installation](docs/python_installation.md)  

[IntelliJ Setup](docs/intellij/intellij_setup.md)  

#### Chapter 1. [Numbers](src/tutorials/chapter_01_numbers/numbers.md)
___
- Integers
- Real and Complex Numbers
- Integer Representation
- Real Number Representation
- Data Types
- Other Numbers
- Math functions

#### Chapter 2. Strings
___
- Regular Expression

#### Chapter 3. Collections
___
- List and Tuple
- Dictionary
- Set
- Named Tuple
- Comprehension
- Deep Copy

#### Chapter 4. Booleans and Flow Controls
___
- Boolean 
- If
- For
- While

#### Chapter 5. Functions and Lambdas
___
- Functions are reusable code
- Logging
- Exceptions
- Performance Profiling
- As code gets more complex, we need unit tests
    - simple test cases
    - run in IDE 
    - default naming is test_*, can be overwritten.
- packages and modules
    - package paths have to be uniquely globally. If one lib uses a path, then
      this path can't be used elsewhere in the global. So it's better to create
      top unique package name. Python does not do package merging. This is a
      big drawback in my view.

#### Chapter 6. More Functions
___
- Generators
- Decorators


#### Chapter 7. Classes and Testing
___
- Inheritance
- Pickle
- More Unit Tests
    - setup() and teardown()
    - mock
    - test coverage
    - run via command line

#### Chapter 8. More Classes
___
- Data Class
- Enums
- Iterator
- Decorator

#### Chapter 9. Date and Time
___
- date and time
- arrow/delorean

#### Chapter 10. Files and IO
___
- argparse
- File IO
- pillow
- subprocess

- tar file example: https://stackoverflow.com/questions/20135019/add-multiple-files-from-multiple-directories-to-unique-tar-gz-archives-using-py

- Visualize code execution: https://pythontutor.com/

- https://github.com/chinesehuazhou/python-whydo
- https://github.com/zhiwehu/Python-programming-exercises

### Others
Parallel Computing:
[Ray](https://github.com/ray-project/ray), Dask, Dispy, Pandaral-lel, Joblib
- parallel computing: https://people.orie.cornell.edu/vc333/orie5270/lectures/weeks9-10/
- https://www.infoworld.com/article/3542595/6-python-libraries-for-parallel-processing.html
- https://www.infoworld.com/article/3526429/how-to-use-asyncio-in-python.html
- https://www.infoworld.com/article/3454442/get-started-with-async-in-python.html
- https://www.marktechpost.com/2020/03/29/uber-open-sources-fiber-a-python-distributed-computing-library-for-modern-computer-clusters/
- 






- Python 3.10 features: https://blog.csdn.net/cqcre/article/details/120714815?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_title~default-0.no_search_link&spm=1001.2101.3001.4242

- https://www.infoworld.com/article/3600993/5-great-libraries-for-profiling-python-code.html

- https://www.toutiao.com/a6838935202333458947/
