import numpy
import pylab
import scipy
from matplotlib.widgets import Slider, RadioButtons, CheckButtons

def gauss(x):
    #Отображаемая фукнция
    return (numpy.sin(x) * numpy.cos(x**2+5))

def tangent(x0, x):
    f = scipy.misc.derivative(gauss, x0, dx = 1e-6)
    f_0 = gauss(x0)
    tangent_result = f_0 + f * (x-x0)
    return tangent_result


if __name__ == '__main__':

    def updateGraph():
        global graph_axes
        x = numpy.arange(0, 5.0000001, 0.01)
        y = gauss(x)
        colors = {'Пурпурный': 'm', 'Синий': 'b', 'Зеленый': 'g'}
        styles = {'Сплошная линия': '-', 'Штриховая линия': '--', 'Штрих-пунктирная линия': '-.', 'Штриховая линия': ':'}
        graph_axes.clear()
        graph_axes.plot(x, y, color = colors[radiobuttons_color.value_selected], linestyle = styles[radiobuttons_style.value_selected])

        global slider_sigma
        sigma = slider_sigma.val
        y = gauss(sigma)
        graph_axes.plot(sigma, y, 'o', color = 'red')
        x_0 = sigma
        y = tangent(x_0, x)
        graph_axes.set_ylim(-1.2, 1.2)
        global tangent_flag 
        if tangent_flag:
            graph_axes.plot(x, y, color = 'red')

        pylab.draw()


    def onChangeGraph(value):
        updateGraph()
    
    def onCheckClicked(label):
        global tangent_flag
        # Обработчик события при клике по CheckButtons
        if label == 'Касательная':
            tangent_flag = not tangent_flag
        updateGraph()

    def ButtonsClicked(label):
        # Обработчик события при клике по Button
        slider_sigma.set_val(0)
        updateGraph()

    def onRadioButtonsClicked_color(label):
        # Обработчик события при клике по RadioButtons_color
        updateGraph()

    def onRadioButtonsClicked_style(label):
        #Обработчик события при клике по RadioButtons_style
        updateGraph()


    fig, graph_axes = pylab.subplots(figsize = (10, 5))
    graph_axes.grid()
    tangent_flag = False
    graph_axes.set_title('Грфик')     
    # Основной график
    fig.subplots_adjust(left=0.17, right=0.85, top=0.95, bottom=0.55)

    # Создание слайдера
    axes_slider_sigma = pylab.axes([0.20, 0.35, 0.62, 0.04])
    slider_sigma = Slider(axes_slider_sigma, label='Движение точки', valmin=0, valmax=5.0, valinit=0, valfmt='%1.2f')
    slider_sigma.on_changed(onChangeGraph)

    axes_checkbuttons = pylab.axes([0.10, 0.15, 0.2, 0.1])

    # Создание флажка
    checkbutton_grid = CheckButtons(axes_checkbuttons, ['Касательная'], [False])
    checkbutton_grid.on_clicked(onCheckClicked)

    # Создание осей для переключателей
    axes_button = pylab.axes([0.35, 0.10, 0.2, 0.2])

    # Создание переключателя

    check_button = pylab.Button(axes_button, "Сброс")
    check_button.on_clicked(ButtonsClicked)

    #Создание осей для переключателей
    axes_radiobuttons_color = pylab.axes([0.58, 0.10, 0.12, 0.2])

    # Создание переключателя на цвет
    radiobuttons_color = RadioButtons(axes_radiobuttons_color, ['Синий', 'Пурпурный', 'Зеленый',])
    radiobuttons_color.on_clicked(onRadioButtonsClicked_color)

    # Создание переключателя на стиль
    axes_radiobuttons_style = pylab.axes([0.72, 0.10, 0.259, 0.2])
    radiobuttons_style = RadioButtons(axes_radiobuttons_style, ['Сплошная линия', 'Штриховая линия', 'Штрих-пунктирная линия', 'Штриховая линия'])
    radiobuttons_style.on_clicked(onRadioButtonsClicked_style)

    updateGraph()
    pylab.show()
