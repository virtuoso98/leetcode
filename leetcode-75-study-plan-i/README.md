# :books: Leetcode 75 Study Plan

This contains some interesting learning points I've gained from doing the leetcode 75 study plan.

## 205 - Isomorphic Strings

By nature, isomorphic strings means that they are structurally the same - a bijection can be made from 1 string to another. This gives 2 interesting approaches:

- Add `s_to_t` and `t_to_s` mapping if none of that exists and if it does, check if bijection exists. using `dict.get()` catches for `None` cases where only one of the 2 mappings are defined.
- Alternatively, check that the cardinality of the sets created by `s`, `t` and their combined sets are all the same.