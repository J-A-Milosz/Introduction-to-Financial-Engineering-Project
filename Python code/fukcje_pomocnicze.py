from numpy import zeros



def call_payoff(K, S):
    # payoff opcji call
    return max(S - K, 0)


def put_payoff(K, S):
    # payoff opcji put
    return max(K - S, 0)


def create_share_price_matrix(S_0, n, u, d):
    # tworzenie macierzy cen akcji zgodnie z modelem
    # wiersze to możliwie ceny w czasie: numer_wiersza * dt
    S_matrix = zeros((n + 1, n + 1))
    for i_row in range(n + 1):
        for i_col in range(0, i_row + 1):
            S_matrix[i_row][i_col] = S_0 * u ** (i_row - i_col) * d ** i_col
    return S_matrix


def create_intrinsic_value_matrix(o_type, K, n, S_matrix):
    # bez n (ewentualnie)

    # tworzenie macierzy wartości wewnętrznych opcji na podstawie macierzy cen akcji
    # wiersze to możliwie wartości wewnętrzne w czasie: numer_wiersza * dt
    V_matrix = zeros((n+1, n+1))
    if o_type == 'c':
        for i_row in range(n + 1):
            for i_col in range(0, i_row + 1):
                V_matrix[i_row][i_col] = call_payoff(K, S_matrix[i_row][i_col])
    if o_type == 'p':
        for i_row in range(n + 1):
            for i_col in range(0, i_row + 1):
                V_matrix[i_row][i_col] = put_payoff(K, S_matrix[i_row][i_col])
    return V_matrix



def create_share_price_at_T_lst(S_0, n, u, d):
    # tworzenie liste cen akcji w chwili T
    S_T_lst = zeros(n + 1)
    for i in range(n + 1):
        S_T_lst[i] = S_0 * u ** (n - i) * d ** i
    return S_T_lst



def create_intrinsic_value_at_T_lst(o_type, K, n, S_T_lst):
    # tworzenie macierzy wartości wewnętrznych opcji w chwilil T
    V_T_lst = zeros(n + 1)
    if o_type == 'c':
        for i in range(n + 1):
            V_T_lst[i] = call_payoff(K, S_T_lst[i])
    if o_type == 'p':
        for i in range(n + 1):
            V_T_lst[i] = put_payoff(K, S_T_lst[i])
    return V_T_lst
