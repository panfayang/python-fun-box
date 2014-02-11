"""
As of 7/6/13, I could not think of a good algorithm to solve this. But here is a list of things I thought of:

1. There are only two possible ways to go after each direction, which is to its left/right. This might relate
    to binary trees. However, after drawing, I don't know what to do next.

2. If we assume the instruction starts from the origin, we can put the polygon in a x-y plane. From there,
    It might be possible to use Scipy, Numpy or Pylab to draw it out and calculate from the graph. Although
    I could not find anything helpful after some research, I will look at them in greater details.

3. After some sketches, I found the area can only be calculated after we obtain an enclosed area. Therefore,
    there might not be a fast algorithm which calculates the area as the computer reads the input.

4. The order of the instruction matters a lot. A switch of items in input results in a different shape.

Fayang Pan
7/6/13
"""
