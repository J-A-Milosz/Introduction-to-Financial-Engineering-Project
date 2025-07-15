import timeit
from numpy import round
from funkcje_do_zadan_1_2_3 import european_option_evaluation, american_option_evaluation, draw_option_binary_tree
from funkcje_do_zadan_4_5 import european_option_evaluation_for_drawing, \
    option_evaluation_relative_to_arg_and_option_type, draw_plot_option_evaluation_relative_to_arg
from funkcje_do_map_ciepla_zadanie_4 import option_evaluation_relative_to_arg1_and_arg2_and_option_type, \
    draw_plot_option_evaluation_relative_to_arg1_and_arg2
from funkcje_do_zadania_6 import delta_alpha_hedging_portfolio, draw_hedging_portfolio

fuctions_and_tiems = {}

fuctions_and_tiems[european_option_evaluation.__name__] = timeit.timeit(european_option_evaluation, number=1)

fuctions_and_tiems[american_option_evaluation.__name__] = timeit.timeit(american_option_evaluation, number=1)

v, V_matrix, S_matrix, strike_map = european_option_evaluation(o_type='c')
f_partial = lambda: draw_option_binary_tree(S_matrix, V_matrix, strike_map)
fuctions_and_tiems[draw_option_binary_tree.__name__] = timeit.timeit(f_partial, number=1)

fuctions_and_tiems[european_option_evaluation_for_drawing.__name__] = timeit.timeit(european_option_evaluation_for_drawing, number=1)

lst_K = [i / 20 for i in range(2001)]
f_partial = lambda: option_evaluation_relative_to_arg_and_option_type(european_option_evaluation_for_drawing, 'c', 'K', lst_K)
fuctions_and_tiems[option_evaluation_relative_to_arg_and_option_type.__name__] = timeit.timeit(f_partial, number=1)

lst_K = [i / 20 for i in range(2001)]
f_partial = lambda: draw_plot_option_evaluation_relative_to_arg('K', lst_K)
fuctions_and_tiems[draw_plot_option_evaluation_relative_to_arg.__name__] = timeit.timeit(f_partial, number=1)

lst_T = [i / 4 for i in range(41)]
lst_S_0 = [i / 2 for i in range(201)]
f_partial = lambda: option_evaluation_relative_to_arg1_and_arg2_and_option_type(european_option_evaluation_for_drawing, 'c',
                                                            'T', lst_T, 'S_0', lst_S_0)
fuctions_and_tiems[option_evaluation_relative_to_arg1_and_arg2_and_option_type.__name__] = timeit.timeit(f_partial, number=1)

f_partial = lambda: draw_plot_option_evaluation_relative_to_arg1_and_arg2('T', lst_T, 'S_0', lst_S_0, 'europejskiej')
fuctions_and_tiems[draw_plot_option_evaluation_relative_to_arg1_and_arg2.__name__] = timeit.timeit(f_partial, number=1)

f_partial = lambda: delta_alpha_hedging_portfolio('c', 'europejskiej')
fuctions_and_tiems[delta_alpha_hedging_portfolio.__name__] = timeit.timeit(f_partial, number=1)

f_partial = lambda: draw_hedging_portfolio('c', 'europejskiej')
fuctions_and_tiems[draw_hedging_portfolio.__name__] = timeit.timeit(f_partial, number=1)

for key in fuctions_and_tiems.keys():
    print(f'\\verb|{key}| & {round(fuctions_and_tiems[key], 6)} \\\\')




