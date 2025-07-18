def find_pivot_bland(tableau):
    """
    Using Bland's rule and the minimum ratio test, find the pivot entry in the tableau.
    
    Parameters
    ----------
    tableau : array
        The simplex method tableau in basic form
    
    Returns
    -------
    r, s : integer
        Row and column indexes of the pivot

    Notes
    -----
    Assumes that there is a negative reduced cost that we can pivot on.
    """
    M, N = tableau.shape
    m = M-1  # Number of constraints
    n = N-1  # Number of variables
    # Bland's rule: find first negative reduced cost
    s = 1
    while tableau[0, s] >= 0:
        s = s + 1
    # Minimum ratio test plus Bland's rule:
    # find the (first) row i minimizing b_i / a_{is}, a_{is} > 0
    r = 0
    theta_star = np.inf
    for i in range(1, m+1):
        if tableau[i, s] > 0:
            if tableau[i, 0] / tableau[i, s] < theta_star:
                r = i
                theta_star = tableau[i, 0] / tableau[i, s]
    return r, s
