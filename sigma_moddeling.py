from matplotlib import pyplot as plt
import numpy as np


def add_grid(axes):
    """Functions to modify grid"""
    axes.grid(color='grey', linestyle='-', linewidth=0.5, which='major', axis='both')
    axes.grid(color='lightblue', linestyle='-', linewidth=0.5, which='minor', axis='both')
    axes.minorticks_on()


def get_stat(arr):
    return np.percentile(arr, 5), np.percentile(arr, 50), np.percentile(arr, 95)


def plot_hist(rnd_set, sigma_mc_modeled):
    fig, axes = plt.subplots(2, 3, figsize=(8, 5), dpi=85,
                             facecolor='white', frameon=True, edgecolor='grey', linewidth=1)
    fig.subplots_adjust(wspace=0.4, hspace=0.5, left=0.12, right=0.95, top=0.9, bottom=0.18)

    t_ax = axes[0, 0]
    t_ax.hist(rnd_set.params_prop['porosity']['param_rand'], bins=50)
    t_ax.set_title('Porosity', fontsize=10)
    t_ax.set_xlabel('Porosity, v/v', fontsize=8)
    t_ax.set_ylabel('Frequency', fontsize=8)
    add_grid(t_ax)

    t_ax = axes[0, 1]
    t_ax.hist(rnd_set.params_prop['water_saturation']['param_rand'], bins=50)
    t_ax.set_title('Sw', fontsize=10)
    t_ax.set_xlabel('Saturation water, v/v', fontsize=8)
    t_ax.set_ylabel('Frequency', fontsize=8)
    add_grid(t_ax)

    t_ax = axes[0, 2]
    t_ax.hist(rnd_set.params_prop['sigma_water']['param_rand'], bins=50)
    t_ax.set_title('Sigma water', fontsize=10)
    t_ax.set_xlabel('Sigma water, c.u.', fontsize=8)
    t_ax.set_ylabel('Frequency', fontsize=8)
    add_grid(t_ax)

    t_ax = axes[1, 0]
    t_ax.hist(rnd_set.params_prop['sigma_oil']['param_rand'], bins=50)
    t_ax.set_title('Sigma oil', fontsize=10)
    t_ax.set_xlabel('Sigma oil, c.u.', fontsize=8)
    t_ax.set_ylabel('Frequency', fontsize=8)
    add_grid(t_ax)

    t_ax = axes[1, 1]
    t_ax.hist(rnd_set.params_prop['sigma_matrix']['param_rand'], bins=50)
    t_ax.set_title('Sigma matrix', fontsize=10)
    t_ax.set_xlabel('Sigma matrix, c.u.', fontsize=8)
    t_ax.set_ylabel('Frequency', fontsize=8)
    add_grid(t_ax)

    t_ax = axes[1, 2]
    t_ax.hist(sigma_mc_modeled, color='red', bins=50)
    t_ax.set_title('Sigma modelled', fontsize=10)
    t_ax.set_xlabel('Sigma modelled, c.u.', fontsize=8)
    t_ax.set_ylabel('Frequency', fontsize=8)
    add_grid(t_ax)

    plt.show()


class RandomSet:
    def __init__(self, params_prop, params_val, scale):
        self.params_prop = params_prop.copy()
        self.params_val = params_val.copy()
        for param in self.params_prop.keys():
            self.params_prop[param]['param_rand'] = np.random.default_rng().normal(self.params_val[param],
                                                                                   self.params_prop[param]['std'],
                                                                                   scale)

    def print_values(self, param):
        print(self.params_prop[param]['param_rand'])


def calculate_model_sigma(rnd_set):
    por = rnd_set.params_prop['porosity']['param_rand']
    sw = rnd_set.params_prop['water_saturation']['param_rand']
    sigma_oil = rnd_set.params_prop['sigma_oil']['param_rand']
    sigma_water = rnd_set.params_prop['sigma_water']['param_rand']
    sigma_matrix = rnd_set.params_prop['sigma_matrix']['param_rand']
    sigma_modeled = sigma_matrix*(1-por)+por*sw*sigma_water+por*(1-sw)*sigma_oil
    return sigma_modeled


params_prop_dict = {
    'porosity': {
        'std': 0.01,
        'units': 'v/v',
    },
    'water_saturation': {
        'std': 0.03,
        'units': 'v/v',
    },
    'sigma_water': {
        'std': 2,
        'units': 'cu',
    },
    'sigma_oil': {
        'std': 0.5,
        'units': 'cu',
    },
    'sigma_matrix': {
        'std': 0.5,
        'units': 'cu',
    },
}

params_val_dict = {
    'porosity': 0.15,
    'water_saturation': 0.35,
    'sigma_water': 110,
    'sigma_oil': 21,
    'sigma_matrix': 8,
}


def main():
    rnd_set = RandomSet(params_prop_dict, params_val_dict, 1000)
    sigma_mc_modeled = calculate_model_sigma(rnd_set)
    print(get_stat(sigma_mc_modeled))
    plot_hist(rnd_set, sigma_mc_modeled)


if __name__ == '__main__':
    main()
