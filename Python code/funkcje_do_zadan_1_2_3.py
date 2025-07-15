from numpy import e, sqrt, zeros, round
from matplotlib.pyplot import plot, text, show, tight_layout, yscale, xlabel, ylabel, title, close
from fukcje_pomocnicze import create_share_price_matrix, create_intrinsic_value_matrix




def european_option_evaluation(o_type='c', K=48, T=2, dt=1/12, S_0=50, sigma=0.3, r=0.02):
    # if T//dt != T/dt:
    #    raise ValueError('dt musi byc dzielnikiem T')

    n = int(T / dt)
    u = e**(sigma * sqrt(dt))
    d = e**(-sigma * sqrt(dt))
    p = (e**(r*dt) - d) / (u - d)

    # Uwaga: w opcj europejskiej nie trzeba liczyć całych macierzy wystarczy ostatni rząd
    # Ale taka implementacja pomoże nam w rozwiązaniu podpunktu 6.
    S_matrix = create_share_price_matrix(S_0, n, u, d)
    V_matrix = create_intrinsic_value_matrix(o_type, K, n, S_matrix)

    # Zwracanie strike_map umożliwia
    strike_map = zeros((n + 1, n + 1))
    strike_map[n][:] = [1 if el > 0 else el for el in V_matrix[n][:]]

    for i_row in range(n-1, -1, -1):
        for i_col in range(0, i_row + 1):
            value = e**(-r * dt) * (V_matrix[i_row+1][i_col] * p
                                    + V_matrix[i_row+1][i_col+1] * (1-p))
            V_matrix[i_row][i_col] = value

    return V_matrix[0][0], V_matrix, S_matrix, strike_map



def american_option_evaluation(o_type='c', K=48, T=2, dt=1/12, S_0=50, sigma=0.3, r=0.02):
    # if T//dt != T/dt:
    #     raise ValueError('dt musi byc dzielnikiem T')

    n = int(T / dt)
    u = e**(sigma * sqrt(dt))
    d = e**(-sigma * sqrt(dt))
    p = (e**(r*dt) - d) / (u - d)

    S_matrix = create_share_price_matrix(S_0, n, u, d)
    V_matrix = create_intrinsic_value_matrix(o_type, K, n, S_matrix)

    strike_map = zeros((n+1, n+1))
    strike_map[n][:] = [1 if el > 0 else el for el in V_matrix[n][:]]

    for i_row in range(n-1, -1, -1):
        for i_col in range(0, i_row + 1):
            continuation_value = e**(-r * dt) * (V_matrix[i_row+1][i_col] * p
                                                 + V_matrix[i_row+1][i_col+1] * (1-p))
            if continuation_value >= V_matrix[i_row][i_col]:
                V_matrix[i_row][i_col] = continuation_value
            else:
                strike_map[i_row][i_col] = 1

    return V_matrix[0][0], V_matrix, S_matrix, strike_map



def draw_option_binary_tree(S_matrix, V_matrix, strike_map, dt=1/12):
    n = len(V_matrix[0]) - 1
    V_matrix = round(V_matrix, 2)

    for i_row in range(n + 1):
        for i_col in range(0, i_row + 1):
            t, S_t = i_row*dt, S_matrix[i_row][i_col]
            # rysowanie krawedzi
            if i_row != n:
                t_next = t + dt
                plot([t, t_next], [S_t, S_matrix[i_row+1][i_col]], linestyle='-', color='silver')
                plot([t, t_next], [S_t, S_matrix[i_row+1][i_col+1]], linestyle='-', color='silver')

            # rysowanie wierzchołków
            if strike_map[i_row][i_col] == 1:
                plot(t, S_t, 'o', markersize=12, color='lightcoral')
            else:
                plot(t, S_t, 'o', markersize=12, color='white')

            # rysowanie wartosci
            text(t, S_t,
                 str(V_matrix[i_row][i_col]),
                 ha='center',
                 va='center',
                 fontsize=6,
                 fontweight='bold')
    yscale('log')
    xlabel(r'$t$')
    ylabel(r'$\ln(S_t)$')
    title(r'Wartość opcji ($V_t$) w modelu dwumianowym przy danym $t$ oraz $S_t$')
    tight_layout()
    show()
    # close()



if __name__ == '__main__':
    pass
