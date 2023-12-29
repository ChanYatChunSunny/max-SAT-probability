from typing import List, Optional

def _pr_clause_satisfied(vals: List[Optional[bool]], clause_vars: List[int], clause_negateds: List[bool]) -> float:
    """
    Pr(clause is satisifed) = 1 - (The product of Pr(val = false) for each non-negated literal * The product of Pr(val = true) for each negated literal)

    Args:
        vals (List[Optional[bool]]): The assignment of each value, None represents it is undetermined.
        clause_vars (List[int]): A storing the index of each literal.
        clause_negateds (List[bool]): A list storing whether each literal is negated.

    Returns:
        float: The probability that this clause is satisifed.
    """
    ret = 1.0
    #First obtain the unsatisifed probability
    for i in range(len(clause_negateds)):
        #When the value of the variable is undetermined, the chance is 50/50
        if vals[clause_vars[i]] == None:
            ret *= 0.5
        else:
            #When val is false and it is not negated, then it is false
            #Val is false and negated, then it is true
            #Val is true and not negated, then it is true
            #Val is true and negated, then it is false
            #So it is xor
            var_eval = vals[clause_vars[i]] ^ clause_negateds[i]

            if var_eval:
                #0 times anything is 0
                return 0.0
            else:
                ret *= 1.0
    #obtain the satisifed probability
    ret = 1 - ret
    return ret

def expected(vals: List[Optional[bool]], vars: List[List[int]], negateds: List[List[bool]]) -> float:
    """
    Expected value(num of satisifed clauses) = summation of Pr(clause is satisifed)

    Pr(clause is satisifed) = 1 - (The product of Pr(val = false) for each non-negated literal * The product of Pr(val = true) for each negated literal)

    Args:
        vals (List[Optional[bool]]): The assignment of each value, None represents it is undetermined.
        vars (List[List[int]]): A 2D list storing the index of each literal. Each row is a clause.
        negateds (List[List[bool]]): A 2D list storing whether each literal is negated. Each row is a clause.

    Returns:
        float: The expected value.
    """
    ret = 0
    for i in range(len(negateds)):
        ret += _pr_clause_satisfied(vals, vars[i], negateds[i])
    return ret