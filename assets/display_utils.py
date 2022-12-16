import pygame

from assets.globals import *

def draw_histogram(surface, histogram_data, histogram_location, histogram_end, hfont, spacing = 0.05, text_space = 0.05, box = True):
    hist_width = histogram_end[0] - histogram_location[0]
    chart_height = histogram_end[1] - histogram_location[1]
    hist_height = chart_height * (1 - text_space)
    dlen = len(histogram_data)
    dmax = max(histogram_data.values())

    if box:
        pygame.draw.rect(surface, BLACK, (histogram_location[0], histogram_location[1], hist_width, hist_height), 1, 1)
        pygame.draw.rect(surface, BLACK, (histogram_location[0], histogram_location[1], hist_width, chart_height), 1, 1)
    if dlen == 0 or dmax == 0:
        return

    bar_interval = (hist_width / dlen)
    bar_width = (1 - spacing) * bar_interval
    unit_height = hist_height / dmax

    x = histogram_location[0] + (bar_interval - bar_width) / 2
    y = histogram_end[1]

    

    for key in histogram_data.keys():
        value = histogram_data[key]
        pygame.draw.rect(surface, GRAY, (x, y-unit_height*value, bar_width, unit_height*value))
        x += bar_interval/2
        surface.blit(hfont.render(key, False, BLACK), (x, y + text_space * chart_height / 2))
        x += bar_interval/2



    


