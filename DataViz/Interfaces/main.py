import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

class dataviz:

    def __init__(self, background  = '#1B1B2F', auxiliary_background ='#22223D', colors = ['#F54291','#2AD5F5','#F5E55B','#F5E55B','#2594A8'], color_labels = '#FFFFFF'):
        self.background = background
        self.auxiliary_background = auxiliary_background
        self.colors = colors
        self.color_labels = color_labels
    
    def plot_lines(self, x, y, background = '#1b1b2f', colors = ['#f54291','#4cd3c2'], legend= [], axes = True, grid = True, color_labels = '#FFFFFF'):
        """Plot line graph with n lines.
        
        Parameters
        ----------
        x : list
            List with x values
        y : list
            List with y values
        background : str
            Background color
        colors : list
            Color palette
        legend : list
            List with the legends 
        axes : boolean
            Axes flag
        grid : boolean
            Grid flag
        color_labels : str
            Color of labels
        """

        # generates the figure and axes
        fig, ax = plt.subplots(facecolor = background)
        # set background color
        ax = plt.gca()
        ax.set_facecolor(background)

        # axes configuration
        if axes:
            # removes the bottom and left axes
            for param in ['top', 'right']:
                ax.spines[param].set_visible(False)
            # changes the color of the active axes
            for param in ['top','right']:
                ax.spines[param].set_color(color_labels)
            # changes the color of the labels 
            for i in ['x','y']:
                ax.tick_params(axis = i, colors = color_labels)
        else:
            # removes the axes
            for param in ['bottom','top','left','right']:
                ax.spines[param].set_visible(False)
            # changes the color of the labels
            for i in ['x','y']:
                ax.tick_params(axis = i, colors = background)
        
        # grid configuration
        if grid:
            # add the grids
            plt.grid(color = color_labels, linestyle = ':', linewidth = 2, alpha = 0.1)
        
        # plots the lines
        for i in range(0, len(x)):
            plt.plot(x[i],y[i], color = colors[i])
        
        # definition of shadow resources
        n_shades = 10
        diff_linewidth = 1.0
        alpha_value = 0.4 / n_shades

        # generates the neon effect
        for i in range(0, len(x)):
            for n in range(1, n_shades+1):
                plt.plot(x[i],y[i], linewidth = 2+(diff_linewidth*n), alpha = alpha_value, color = colors[i])

        # generates the shadow below the lines
        for i in range(0, len(x)):
            ax.fill_between(x = x[i], y1 = y[i],y2 = y[i].min(), color = colors[i], alpha = 0.08)

        # generates the legend
        if legend == []:
            aux_legend = []
            for i in range(0, len(x)):
                aux_legend.append(f'line {i+1}')
            leg = ax.legend(aux_legend, frameon = False)
        else:
            leg = ax.legend(legend, frameon = False)

        # change de color legend   
        for text in leg.get_texts():
            plt.setp(text, color = color_labels)



    

