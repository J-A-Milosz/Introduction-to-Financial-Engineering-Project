from matplotlib.pyplot import show, subplots, close
from numpy import zeros
from funkcje_do_zadan_4_5 import european_option_evaluation_for_drawing
from funkcje_do_zadan_1_2_3 import american_option_evaluation




def option_evaluation_relative_to_arg1_and_arg2_and_option_type(option_evaluation_function,
                                                                o_type,
                                                                arg1, arg1_lst,
                                                                arg2, arg2_lst):
    args = {'K': 48, 'T': 2, 'dt': 1 / 12, 'S_0': 50, 'sigma': 0.3, 'r': 0.02}
    values_matrix = zeros((len(arg2_lst), len(arg1_lst)))
    for i_row in range(len(arg2_lst)):
        args[arg2] = arg2_lst[i_row]
        for i_col in range(len(arg1_lst)):
            args[arg1] = arg1_lst[i_col]
            value = option_evaluation_function(o_type, **args)[0]
            values_matrix[len(arg2_lst) - 1 - i_row][i_col] = value

    return values_matrix


def draw_plot_option_evaluation_relative_to_arg1_and_arg2(arg1, arg1_lst, arg2, arg2_lst, option_type_a_e):
    types = {'europejskiej': european_option_evaluation_for_drawing, 'amerykańskiej': american_option_evaluation}
    values_call_matrix \
        = option_evaluation_relative_to_arg1_and_arg2_and_option_type(types[option_type_a_e],
                                                                      o_type='c',
                                                                      arg1=arg1,
                                                                      arg1_lst=arg1_lst,
                                                                      arg2=arg2,
                                                                      arg2_lst=arg2_lst)
    values_put_matrix \
        = option_evaluation_relative_to_arg1_and_arg2_and_option_type(types[option_type_a_e],
                                                                      o_type='p',
                                                                      arg1=arg1,
                                                                      arg1_lst=arg1_lst,
                                                                      arg2=arg2,
                                                                      arg2_lst=arg2_lst)

    # Tworzymy wykres:
    fig, plots = subplots(1, 2)

    # Zmiana arg, zeby LaTeX zadzialal na sigme:
    if arg1 == 'sigma':
        arg1 = '\sigma'

    if arg2 == 'sigma':
        arg2 = '\sigma'

    boundaries = [min(arg1_lst), max(arg1_lst), min(arg2_lst), max(arg2_lst)]

    call_plot = plots[0].imshow(values_call_matrix, cmap='hot', extent=boundaries, aspect='auto')
    plots[0].set_title('Call')
    plots[0].set_xlabel(rf'${arg1}$')
    plots[0].set_ylabel(rf'${arg2}$')

    put_plot = plots[1].imshow(values_put_matrix, cmap='hot', extent=boundaries, aspect='auto')
    plots[1].set_title('Put')
    plots[1].set_xlabel(rf'${arg1}$')
    plots[1].set_ylabel(rf'${arg2}$')

    fig.suptitle(fr'Cena {option_type_a_e} opcji ($V_0$) w zależności od ${arg1}$ i ${arg2}$')

    cbar = fig.colorbar(call_plot, ax=plots.ravel().tolist(), shrink=0.6)
    cbar.set_label(r'Wartości $V_0$')

    show()
    # close()


if __name__ == '__main__':
    lst_T = [i / 4 for i in range(40)]
    lst_S_0 = [i / 2 for i in range(201)]
    lst_K = [i / 2 for i in range(201)]
    lst_r = [0.01 * i for i in range(21)]
    lst_sigma = [0.01 * i for i in range(1, 201)]

    # T kontra S_0
    draw_plot_option_evaluation_relative_to_arg1_and_arg2('T', lst_T, 'S_0', lst_S_0, 'europejskiej')
    draw_plot_option_evaluation_relative_to_arg1_and_arg2('T', lst_T, 'S_0', lst_S_0, 'amerykańskiej')

    # T kontra r
    draw_plot_option_evaluation_relative_to_arg1_and_arg2('T', lst_T, 'r', lst_r, 'europejskiej')
    draw_plot_option_evaluation_relative_to_arg1_and_arg2('T', lst_T, 'r', lst_r, 'amerykańskiej')

    # T kontra sigma
    draw_plot_option_evaluation_relative_to_arg1_and_arg2('T', lst_T, 'sigma', lst_sigma, 'europejskiej')
    draw_plot_option_evaluation_relative_to_arg1_and_arg2('T', lst_T, 'sigma', lst_sigma, 'amerykańskiej')

    # S_0 kontra K
    draw_plot_option_evaluation_relative_to_arg1_and_arg2('S_0', lst_S_0, 'K', lst_K, 'europejskiej')
    draw_plot_option_evaluation_relative_to_arg1_and_arg2('S_0', lst_S_0, 'K', lst_K, 'amerykańskiej')
