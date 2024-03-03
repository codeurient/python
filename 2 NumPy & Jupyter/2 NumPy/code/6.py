import numpy as np

qutu0 = np.array(25)

qutu1 = np.array(    [1, 2, 3, 4, 5]    )

qutu2 = np.array(    [[1, 2, 3],        [4, 5, 6]]    )

qutu3 = np.array(    [[[1, 2],       [3, 4]],       [[5, 6], [7, 8]]]    )

qutu4 = np.array(    [[[[1, 2], [3, 4]],        [[5, 6], [7, 8]]],        [[[1, 2], [3, 4]],        [[5, 6], [7, 8]]]]    )

# ndim() metodu ilə NumPy array-inin nece ölçülü olduğunu öyrənə bilərik.
print(  np.ndim(qutu0)  ) #! 0
print(  np.ndim(qutu1)  ) #! 1
print(  np.ndim(qutu2)  ) #! 2
print(  np.ndim(qutu3)  ) #! 3
print(  np.ndim(qutu4)  ) #! 4