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

# Alyssa Euana Luna - Reflection
# In this activity, I learned the difference between sequential and parallel algorithms. At first, I thought parallel would always be faster because it does many things at the same time. But after trying it out, I realized that’s not always true.
# When we used a small dataset, the sequential approach actually worked better. It was easier to understand and didn’t need extra steps. Everything just runs in order, so it felt more simple and less confusing. The parallel version was harder because we had to split the data, process each part, and then combine the results again. These extra steps made it feel more complicated and sometimes even slower.
# We also found it challenging to make sure everything worked correctly in the parallel version. It was easy to make small mistakes, especially when combining the results back together.
# Overall, I learned that parallel algorithms are not always the best choice. They are useful when working with large data or heavy tasks, but for small and simple problems, sequential is usually better because it is easier and faster to use.
