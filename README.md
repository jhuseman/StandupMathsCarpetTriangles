# StandupMathsCarpetTriangles

This is my solution for Matt Parker's [Rug Puzzle](https://youtu.be/HViA6N3VeHw) challenge.  It's just a simple python script I wrote to calculate the total number of triangles on the rug, for any arbitrary size of rug following the pattern described in the video.

See [this pdf](StandupMathsCarpetTrianglesProblem.pdf) for details of my solution.

The code for the solution is written in [CarpetTriangles.py](CarpetTriangles.py).  Just change the call to `total_triangles(width, height, down_right)` at the bottom to suit the dimensions of the carpet to calculate.  The `down_right` variable is a boolean value to represent if the top left square has the diagonal going "down and to the right" (`True`) or "down and to the left" (`False`).

With this code, the output of the following are:
```python
print total_triangles(20, 18, True)  # Full-size carpet
7860
print total_triangles(15, 13, False) # Carpet shown on store
3178
print total_triangles(5, 2, True)    # small segment created by Matt Parker
43
```
