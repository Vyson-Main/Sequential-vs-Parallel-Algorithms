# Sequential-vs-Parallel-Algorithms

# Nathaniel Beatisula - Reflection
# Through this activity, I realized that parallel algorithms aren't automatically faster than sequential ones; their efficiency heavily depends on the size of the dataset being processed. While the sequential approach was straightforward and actually performed better on the small 1,000-element list due to low overhead , writing the parallel implementation highlighted the complexities of process coordination. The biggest challenge was correctly partitioning the data, managing the worker queues in Python, and merging the sorted chunks back into a single accurate output. Ultimately, this experience reinforced that parallelism is incredibly powerful for large-scale data workflows, but only when the computational gain outweighs the cost of synchronization.


# Chrisa Lene Joy Bautista - Reflection
# When Parallelism Was Beneficial or Unnecessary
# Based on our results, parallelism wasn't clearly beneficial in any of the cases we tested on this machine, but I understand why it can be, based on the trend we saw. With a truly massive dataset tens of millions of elements and on a machine with more cores, the computation time for each chunk would grow large enough that splitting it across multiple cores would give a real advantage over doing it all on one.
# For searching, I think parallelism would only make sense if you were searching through something much more expensive than a simple integer comparison for example, searching through very large text documents or doing pattern matching where each comparison itself takes significant time.
# If I had to summarize what I learned. Parallelism isn't a free speed boost. It's a tool that only pays off when the work you're dividing is heavy enough to justify the cost of dividing it. For anything small or fast, sequential is almost always better.
