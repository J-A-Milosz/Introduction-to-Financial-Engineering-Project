from funkcje_do_zadan_1_2_3 import european_option_evaluation, american_option_evaluation, draw_option_binary_tree
from funkcje_do_zadan_4_5 import draw_plot_option_evaluation_relative_to_arg
from funkcje_do_map_ciepla_zadanie_4 import draw_plot_option_evaluation_relative_to_arg1_and_arg2
from funkcje_do_zadania_6 import draw_hedging_portfolio


if __name__ =='__main__':
    v, V_matrix, S_matrix, strike_map = european_option_evaluation(o_type='c')
    print(f'Cena opcji europejskiej call to: {v}')
    draw_option_binary_tree(S_matrix, V_matrix, strike_map)
    print('-------------------------------------')
    v, V_matrix, S_matrix, strike_map = european_option_evaluation(o_type='p')
    print(f'Cena opcji europejskiej put to: {v}')
    draw_option_binary_tree(S_matrix, V_matrix, strike_map)
    print('-------------------------------------')
    v, V_matrix, S_matrix, strike_map = american_option_evaluation(o_type='c')
    print(f'Cena opcji amerykańskiej call to: {v}')
    draw_option_binary_tree(S_matrix, V_matrix, strike_map)
    print('-------------------------------------')
    v, V_matrix, S_matrix, strike_map = american_option_evaluation(o_type='p')
    print(f'Cena opcji amerykańskiej put to: {v}')
    draw_option_binary_tree(S_matrix, V_matrix, strike_map)
    print('-------------------------------------')

    # od 0 do 100
    lst_K = [i / 20 for i in range(2001)]
    draw_plot_option_evaluation_relative_to_arg('K', lst_K)

    # od 0 do 30
    lst_T = [i / 4 for i in range(121)]
    draw_plot_option_evaluation_relative_to_arg('T', lst_T)

    # od 0 do 100
    lst_S_0 = [i / 20 for i in range(2001)]
    draw_plot_option_evaluation_relative_to_arg('S_0', lst_S_0)

    # od 0.01 do 2
    lst_sigma = [0.01 * i for i in range(1, 201)]
    draw_plot_option_evaluation_relative_to_arg('sigma', lst_sigma)

    # od 0 do 0.2
    lst_r = [0.0001 * i for i in range(2001)]
    draw_plot_option_evaluation_relative_to_arg('r', lst_r)

    lst_dt = [1 / 432, 1 / 288, 1 / 144, 1 / 96, 1 / 72, 1 / 48, 1 / 36, 1 / 24, 1 / 12, 1 / 6, 1 / 4, 1 / 3, 1 / 2, 1]
    draw_plot_option_evaluation_relative_to_arg('dt', lst_dt)

    # Mapy ciepła: zakresy te same z wyjątkiem T!!! T od 0 do 10
    lst_T = [i / 4 for i in range(41)]
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

    # Portfele replikujący europejskiego calla:
    draw_hedging_portfolio('c', 'europejskiej')

    # Portfele replikujący europejskiego puta:
    draw_hedging_portfolio('p', 'europejskiej')

    # Portfele replikujący amerykańskiego calla:
    draw_hedging_portfolio('c', 'amerykańskiej')

    # Portfele replikujący amerykańskiego put:
    draw_hedging_portfolio('p', 'amerykańskiej')
