def find_pivot_largest_subscript(tableau):
    """
    Uses largest subscript case and the minimum ratio test to find the pivot entry in the tableau.

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
    m = M - 1
    n = N - 1
    # Largest subscript rule: find the first negative reduced cost from the right of the tableau
    s = n
    while tableau[0, s] >= 0:
        s -= 1
    # Minimum ratio test and largest subscript rule put together:
    r = 0
    theta_star = np.inf
    for i in range(m, 0, -1):
        if tableau[i, s] > 0:
            if tableau[i, 0] / tableau[i, s] < theta_star:
                r = i
                theta_star = tableau[i, 0] / tableau[i, s]
    final_r = r
    final_s = s
    return final_r, final_s
