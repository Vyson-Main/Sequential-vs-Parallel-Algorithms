# Sequential-vs-Parallel-Algorithms

# Nathaniel Beatisula - Reflection
# Through this activity, I realized that parallel algorithms aren't automatically faster than sequential ones; their efficiency heavily depends on the size of the dataset being processed. 
# While the sequential approach was straightforward and actually performed better on the small 1,000-element list due to low overhead , writing the parallel implementation highlighted the 
# complexities of process coordination. The biggest challenge was correctly partitioning the data, managing the worker queues in Python, and merging the sorted chunks back into a single 
# accurate output. Ultimately, this experience reinforced that parallelism is incredibly powerful for large-scale data workflows, but only when the computational gain outweighs the cost of 
# synchronization.
