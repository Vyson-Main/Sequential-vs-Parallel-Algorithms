# Sequential-vs-Parallel-Algorithms

# Nathaniel Beatisula - Reflection
# Through this activity, I realized that parallel algorithms are not always faster than sequential ones, especially when the dataset is small. In this activity, the sequential version felt simpler and even performed better when working with the 1,000 element list because everything runs in a direct and uncomplicated way. The parallel version, on the other hand, felt more complicated and slower in a way because there were more steps involved before getting the final result.
# One of the hardest parts for me was trying to make everything work together properly. Splitting the data and making sure each part was handled correctly took more effort than I expected. It also felt a bit stressful trying to combine everything back into one correct output, since small mistakes could easily affect the final result.
# To conclude, this activity helped me understand that parallel processing is not always the better choice. It made me realize that sometimes simpler is better, especially when the task is not that big. But I also saw that parallelism can be really helpful when working with larger data, where doing things at the same time actually makes a noticeable difference.



# Chrisa Lene Joy Bautista - Reflection
# When Parallelism Was Beneficial or Unnecessary
# Based on our results, parallelism wasn't clearly beneficial in any of the cases we tested on this machine, but I understand why it can be, based on the trend we saw. With a truly massive dataset tens of millions of elements and on a machine with more cores, the computation time for each chunk would grow large enough that splitting it across multiple cores would give a real advantage over doing it all on one.
# For searching, I think parallelism would only make sense if you were searching through something much more expensive than a simple integer comparison for example, searching through very large text documents or doing pattern matching where each comparison itself takes significant time.
# If I had to summarize what I learned. Parallelism isn't a free speed boost. It's a tool that only pays off when the work you're dividing is heavy enough to justify the cost of dividing it. For anything small or fast, sequential is almost always better.


# Trisha Aira R. Pabonita - Reflection
# In this activity, I saw that sequential execution is easier to implement, while parallel execution is more complex because it involves splitting data, managing processes, and combining results.
# For performance, sequential worked better on small datasets since it has no extra overhead. However, parallel execution can be faster for large datasets because the work is divided across processes.
# I also had challenges in dividing the data correctly and merging the results into one accurate output. This made parallel implementation harder than sequential.
# Overall, I learned that parallelism has extra costs like process management and synchronization. It is useful for large and heavy tasks, but for small problems, sequential execution is still the better choice.


# Liberty Case M. Calo- Reflection

# Through this activity, I learned that parallelism introduces significant overhead that doesn't always justify the added complexity. While I expected parallel search to be faster on large datasets, the results showed that process creation, data partitioning, and queue synchronization consume more time than the actual search work—especially on smaller datasets.
# The main challenge was coordinating multiple processes: mapping local indices back to global positions, managing the queue safely, and merging results correctly. This complexity is why parallel algorithms are harder to implement and debug compared to sequential approaches.
# Overall, parallelism is a powerful tool, but only for truly heavy workloads. For small-to-medium datasets and lightweight operations, sequential execution is simpler and faster. This reinforced that choosing the right algorithm requires understanding both the problem scale and the real costs of synchronization.
