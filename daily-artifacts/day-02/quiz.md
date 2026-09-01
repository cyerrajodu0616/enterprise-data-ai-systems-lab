# Day 02 Quiz Attempt

These entries preserve reasoning supplied from the completed session. They do not imply code or lab execution.

## 1. Traditional join choice

**Question:** With 1B ORDERS and 5M CUSTOMERS, no indexes and no ordering, what would you choose?

**My reasoning:** Row count alone was insufficient; projected size and compute/memory matter. I initially preferred hash join. Nested loop appeared to require repeated expensive access, while sort-merge would add sort CPU, memory, and I/O.

## 2. Broadcast feasibility

**Question:** Why broadcast CUSTOMERS when ORDERS is 1 TB?

**My reasoning:** Moving the smaller relation can avoid redistributing the 1 TB relation. CUSTOMERS becomes the build side and ORDERS probes it. The full probe relation does not need to fit in memory at once.

## 3. Projection and filtering

**Question:** What if CUSTOMERS grows from about 150 MB to 6 GB only because many columns are selected, and only NJ/active customers plus two attributes are needed?

**My reasoning:** Row count is not data size. Filter and project before Exchange/join, then reassess the relation and join strategy.

## 4. Sort-Merge prerequisites

**Question:** Why does `Sort` follow `Exchange hashpartitioning(join_key)`?

**My reasoning:** Exchange brings equal keys to corresponding partitions, but hash partitioning does not order rows within each partition. Sort provides the ordering needed to merge.

## 5. Skew diagnosis

**Question:** One task is much slower and HOT is frequent. Should we add executors or increase shuffle partitions?

**My reasoning:** First inspect task/partition and key-frequency evidence. More executors do not split one hot-key partition. More normal shuffle partitions may help generally oversized partitions, but all HOT records still hash together.

## 6. Salting

**Question:** How can selective salting preserve correctness?

**My reasoning:** Salt only the hot fact key and replicate the matching dimension row across the same salt values; join on `(customer_id, salt)`. Choose buckets from hot-key volume, task evidence, available parallelism, and replication cost—not executor count alone.

## 7. AQE

**Question:** Does AQE need to know that customer HOT is semantically special?

**My reasoning:** No. Runtime evidence that one shuffle partition is disproportionately large may be sufficient for adaptive skew handling. AQE is not automatic salting.

## 8. Cardinality

**Question:** Three rows on each side share key 101. How many output rows, and what should be checked first?

**My reasoning:** Nine rows because output per key is left count times right count. First verify whether N:M is intended; do not immediately tune Spark.

## 9. Correctness before optimization

**Question:** Expected SALES N:1 CUSTOMERS, but C999 has 25 active customer records. What next?

**My reasoning:** Investigate why the uniqueness invariant failed, determine the valid record from business/versioning rules, restore and validate N:1, rerun the workload, and only then investigate legitimate skew.

## 10. Hidden assumption

**Question:** What assumption could invalidate a join-strategy answer?

**My reasoning:** Assuming the build key is unique. If it is not, output can multiply. I should ask for expected cardinality and verify actual per-key counts.
