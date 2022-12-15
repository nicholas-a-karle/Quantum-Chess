import pygame

def draw_histogram(surface, histogram_data, histogram_location, histogram_end, spacing = 0.05):
    #histogram data should be dictionary with numeric values
    #histogram location should be (x, y)
    #histogram end should be (x, y)
    #spacing is % of bar which is displayed empty
    max = 0
    num = 0

    x0 = histogram_location[0]
    y0 = histogram_location[1]
    x1 = histogram_end[0]
    y1 = histogram_end[1]
    hist_width = x1 - x0
    hist_height = y1 - y0

    x = x0
    y = y0

    for key in histogram_data:
        num += 1
        if histogram_data[key] > max:
            max = histogram_data[key]
    
    bar_width = (1-spacing) * hist_width
    unit_height = hist_height / num

    for key in histogram_data:
        value = histogram_data[key]

