from numpy import zeros, e, round
from matplotlib.pyplot import plot, text, show, tight_layout, yscale, xlabel, ylabel, title, subplots_adjust, \
    xlim, ylim, subplots, close
from matplotlib.patches import Ellipse
from funkcje_do_zadan_1_2_3 import european_option_evaluation, american_option_evaluation




def delta_alpha_hedging_portfolio(o_type, option_type_a_e, dt=1/12, r=0.02):
    if option_type_a_e == 'europejskiej':
        val, V_matrix, S_matrix, strike_map = european_option_evaluation(o_type=o_type)
    else:
        val, V_matrix, S_matrix, strike_map = american_option_evaluation(o_type=o_type)
    n = len(V_matrix[0]) - 1

    delta_matrix = zeros((n+1, n+1))
    alpha_matrix = zeros((n+1, n+1))

    for i_row in range(n-1, -1, -1):
        for i_col in range(0, i_row + 1):
            delta = (V_matrix[i_row+1][i_col] - V_matrix[i_row+1][i_col+1]) / \
                                         (S_matrix[i_row+1][i_col] - S_matrix[i_row+1][i_col+1])
            delta_matrix[i_row][i_col] = delta
            alpha = (V_matrix[i_row+1][i_col] - S_matrix[i_row+1][i_col] * delta) * e**(-r* dt)
            alpha_matrix[i_row][i_col] = alpha

    for i_col in range(n+1):
        alpha_matrix[n][i_col] = V_matrix[n][i_col]

    return delta_matrix, alpha_matrix



def draw_hedging_portfolio(o_type, option_type_a_e, dt=1/12, r=0.02, steps_no=6):
    if option_type_a_e == 'europejskiej':
        val, V_matrix, S_matrix, strike_map = european_option_evaluation(o_type=o_type)
    else:
        val, V_matrix, S_matrix, strike_map = american_option_evaluation(o_type=o_type)
    delta_matrix, alpha_matrix = delta_alpha_hedging_portfolio(o_type,
                                                               option_type_a_e,
                                                               dt=dt,
                                                               r=r)
    delta_matrix = round(delta_matrix, 3)
    alpha_matrix = round(alpha_matrix, 3)

    n = steps_no

    fig, ax = subplots()

    for i_row in range(n + 1):
        for i_col in range(0, i_row + 1):
            t, S_t = i_row*dt, S_matrix[i_row][i_col]
            # rysowanie krawedzi
            if i_row != n:
                t_next = t + dt
                plot([t, t_next], [S_t, S_matrix[i_row+1][i_col]], linestyle='-', color='silver', zorder=-1)
                plot([t, t_next], [S_t, S_matrix[i_row+1][i_col+1]], linestyle='-', color='silver', zorder=-1)

    for i_row in range(n + 1):
        for i_col in range(0, i_row + 1):
            t, S_t = i_row * dt, S_matrix[i_row][i_col]
            plot(t, S_t, 'o', markersize=25, color='white', zorder=0)
            dot = Ellipse((t, S_t), 4*dt/5, S_t/6.3, edgecolor='black', facecolor='white', linewidth=0.5)
            ax.add_patch(dot)

            text(t, S_t,
                 rf'$\Delta_{{{round(t, 2)}}}$ = {delta_matrix[i_row][i_col]}' + '\n' +
                 rf'$\alpha_{{{round(t, 2)}}}$ = {alpha_matrix[i_row][i_col]}',
                 ha='center',
                 va='center',
                 fontsize=8,
                 fontweight='bold',
                 zorder=4)

    yscale('log')
    xlabel(r'$t$')
    ylabel(r'$\ln(S_t)$')
    title(r'Portfel replikujący ($\Delta_t, \alpha_t$) w modelu dwumianowym przy danym $t$ oraz $S_t$')
    tight_layout()
    # subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.1)
    # xlim([-0.04, dt*n+0.04])
    # ylim([S_matrix[n][n]*e**(-0.08), S_matrix[n][0]*e**(0.08)])
    show()
    # close()



if __name__ == '__main__':
    pass

