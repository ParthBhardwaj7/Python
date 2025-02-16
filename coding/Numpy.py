#Numpy
#NumPy, which stands for Numerical Python, is an open-source Python library consisting of multidimensional and single-dimensional array elements
#NumPy includes a wide range of mathematical functions for basic arithmetic, linear algebra, Fourier analysis, and more.
# NumPy performs numerical operations on large datasets efficiently.
# NumPy supports multi-dimensional arrays, allowing for the representation of complex data structures such as images, sound waves, and tensors in machine learning models.
# It supports the writing of concise and readable code for complex mathematical computations.
# NumPy integrates with other libraries to do scientific computation; these are SciPy (for scientific computing), Pandas (for data manipulation and analysis), and scikit-learn (for machine learning).
# Many scientific and numerical computing libraries and tools are built on top of NumPy.
# Its widespread adoption and stability make it a standard choice for numerical computing tasks.
# Aspect	NumPy	List
# Memory Storage	NumPy uses a contiguous block of memory, which improves cache efficiency and access speed.	Python lists consist of pointers to objects, leading to more memory fragmentation and slower access.
# Data Types	NumPy supports homogeneous data types (all elements are of the same type), leading to more efficient memory use.	Python lists can contain heterogeneous data types (elements can be of different types), resulting in higher memory overhead.
# Operations	NumPy uses vector operations that leverage SIMD (Single Instruction, Multiple Data) for parallel processing.	Python lists rely on loop-based operations, which are slower due to the overhead of Python's interpreted nature.
# Efficiency	NumPy is written in C and optimized for performance, reducing the execution time of numerical operations.	Python lists are executed as Python byte-code, which is generally slower compared to compiled C code.
# Memory Usage	NumPy requires less memory due to fixed data types and contiguous storage.	Python lists use more memory because each element is a separate Python object with additional overhead.
# Broadcasting	NumPy supports broadcasting, allowing operations on arrays of different shapes without creating additional copies.	Python lists do not support broadcasting, making element-wise operations less efficient.
# Performance	Better cache utilization due to contiguous memory storage, leading to faster access and processing.	Poor cache utilization because of scattered memory allocation, slowing down access.
# Functionality	NumPy provides a rich set of mathematical functions and tools optimized for array operations.	Python lists are Limited to basic operations and lack advanced mathematical capabilities.
import numpy as np
a=np.array([12,23,43,23,23])
print(a)
print(np.__version__)
#Creating 2D array
a=np.array([[1,2,3],[23,5,26]])
print(a)
a=np.array([1,2,3,4,5],ndmin=2)#array have to forced to have this amount of dimension
print(a)
print("shape",a.shape)

a=np.array([1,2,3,4,5])
b=np.array([12,23,34,45,24])



