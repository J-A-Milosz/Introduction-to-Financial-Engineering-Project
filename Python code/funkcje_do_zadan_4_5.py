from matplotlib.pyplot import show, subplots, tight_layout, close
from numpy import e, sqrt, round
from math import comb
from fukcje_pomocnicze import create_share_price_at_T_lst, create_intrinsic_value_at_T_lst
from funkcje_do_zadan_1_2_3 import american_option_evaluation




def european_option_evaluation_for_drawing(o_type='c', K=48, T=2, dt=1 / 12, S_0=50, sigma=0.3, r=0.02):
    # if T//dt != T/dt:
    #     raise ValueError('dt musi byc dzielnikiem T')

    n = int(T / dt)
    u = e ** (sigma * sqrt(dt))
    d = e ** (-sigma * sqrt(dt))
    p = (e ** (r * dt) - d) / (u - d)

    S_T_lst = create_share_price_at_T_lst(S_0, n, u, d)
    V_T_lst = create_intrinsic_value_at_T_lst(o_type, K, n, S_T_lst)

    v = sum([V_T_lst[i] * comb(n, i) * p ** (n - i) * (1 - p) ** i for i in range(n + 1)]) * e ** (-r * T)

    # 3x0 jest dodane, bo american_option_evaluation zwraca 4 elementy,
    # a chce, zeby option_evaluation_relative_to_arg_and_option_type bylo takie same dla obu funkcji
    # bez nadpisywania kodu
    return v, 0, 0, 0


def option_evaluation_relative_to_arg_and_option_type(option_evaluation_function, o_type, arg, arg_lst):
    values_lst = []
    args = {'K': 48, 'T': 2, 'dt': 1 / 12, 'S_0': 50, 'sigma': 0.3, 'r': 0.02}

    for el in arg_lst:
        args[arg] = el
        value = option_evaluation_function(o_type, **args)
        values_lst.append(value[0])

    return values_lst



def draw_plot_option_evaluation_relative_to_arg(arg, arg_lst):

    values_european_call_lst \
        = option_evaluation_relative_to_arg_and_option_type(european_option_evaluation_for_drawing,
                                                            o_type='c',
                                                            arg=arg,
                                                            arg_lst=arg_lst)
    values_european_put_lst \
        = option_evaluation_relative_to_arg_and_option_type(european_option_evaluation_for_drawing,
                                                            o_type='p',
                                                            arg=arg,
                                                            arg_lst=arg_lst)
    values_american_call_lst = \
        option_evaluation_relative_to_arg_and_option_type(american_option_evaluation,
                                                          o_type='c',
                                                          arg=arg,
                                                          arg_lst=arg_lst)
    values_american_put_lst = \
        option_evaluation_relative_to_arg_and_option_type(american_option_evaluation,
                                                          o_type='p',
                                                          arg=arg,
                                                          arg_lst=arg_lst)

    # Tworzymy wykres:
    fig, (call_plot, put_plot) = subplots(ncols=2)

    # Zmodyfikowany slownik z poprzedniej funkcji, aby LaTeX zadzialal na sigme:
    args = {'K': 48, 'T': 2, 'dt': round(1 / 12, 3), 'S_0': 50, '\sigma': 0.3, 'r': 0.02}

    # Zmiana arg, zeby LaTeX zadzialal na sigme:
    if arg == 'sigma':
        arg = '\sigma'

    # Zeby skale na obu wykresach byly rowne
    # ustalamy minimalne i maksymalne wartosci:
    val_min = 0
    val_max = max(max(values_european_call_lst), max(values_european_put_lst),
                  max(values_american_call_lst), max(values_american_put_lst)) + 0.5

    arg_min = 0
    arg_max = max(arg_lst)

    # Rysujemy poczatkowa wartosc parametru:
    call_plot.axvline(args[arg], linestyle=':', linewidth=1, color='dimgrey')
    call_plot.text(args[arg], val_min, rf'${arg}={args[arg]}$', verticalalignment='bottom',
                   horizontalalignment='left', color='dimgrey')
    put_plot.axvline(args[arg], linestyle=':', linewidth=1, color='dimgrey')
    put_plot.text(args[arg], val_min, rf'${arg}={args[arg]}$', verticalalignment='bottom',
                  horizontalalignment='left', color='dimgrey')

    # Plot dla opcji call:
    call_plot.plot(arg_lst, values_european_call_lst, color='blue', linestyle='-',
                   linewidth=2, label='Europejska')
    call_plot.plot(arg_lst, values_american_call_lst, color='orangered', linestyle='--',
                   linewidth=2, label='Amerykańska')
    call_plot.set_title(rf'Cena opcji call ($V_0$) w zależności od ${arg}$')
    call_plot.set_xlabel(rf'${arg}$')
    call_plot.set_ylabel(rf'$V_0({arg})$')
    call_plot.legend(loc='best')
    call_plot.set_ylim(val_min, val_max)
    call_plot.set_xlim(arg_min, arg_max)
    call_plot.grid(True)

    # Plot dla opcji put:
    put_plot.plot(arg_lst, values_european_put_lst, color='blue', linestyle='-',
                  linewidth=2, label='Europejska')
    put_plot.plot(arg_lst, values_american_put_lst, color='orangered', linestyle='--',
                  linewidth=2, label='Amerykańska')
    put_plot.set_title(rf'Cena opcji put ($V_0$) w zależności od ${arg}$')
    put_plot.set_xlabel(rf'${arg}$')
    put_plot.set_ylabel(rf'$V_0({arg})$')
    put_plot.legend(loc='best')
    put_plot.set_ylim(val_min, val_max)
    put_plot.set_xlim(arg_min, arg_max)
    put_plot.grid(True)

    tight_layout()

    show()
    # close()


if __name__ == '__main__':
    lst_T = [i / 4 for i in range(40)]
    lst_S_0 = [i / 2 for i in range(201)]
    lst_K = [i / 2 for i in range(201)]
    lst_r = [0.01 * i for i in range(21)]
    lst_sigma = [0.01 * i for i in range(1, 201)]

    draw_plot_option_evaluation_relative_to_arg('T', lst_T)
    draw_plot_option_evaluation_relative_to_arg('S_0', lst_S_0)
    draw_plot_option_evaluation_relative_to_arg('r', lst_r)
    draw_plot_option_evaluation_relative_to_arg('sigma', lst_sigma)
