import numpy
import pylab
import scipy

def gauss(x):
    #Отображаемая фукнция
    return (numpy.sin(x) * numpy.cos(x**2+5))

def tangent(x0, x):
    f = scipy.misc.derivative(gauss, x0, dx = 1e-6)
    f_0 = gauss(x0)
    tangent_result = f_0 + f * (x-x0)
    return tangent_result
def normal(x0, x):
    f = scipy.misc.derivative(gauss, x0, dx = 1e-6)
    f_0 = gauss(x0)
    normal_result = f_0 - 1/f * (x-x0)
    return normal_result
if __name__ == '__main__':
    fig, graph_axes = pylab.subplots(1, 4, figsize = (15, 4))
    graph_axes[0].grid()
    graph_axes[1].grid()
    graph_axes[2].grid()
    graph_axes[3].grid()

    graph_axes[0].set_title('Грфик')   
    graph_axes[1].set_title('1-я производная')   
    graph_axes[2].set_title('2-я производная')   
    graph_axes[3].set_title('Касательное расслоение')   
    x = numpy.arange(0, 5.0, 0.01)
    y = gauss(x)

    x_max = x[numpy.argmax(y)]
    y_max = numpy.max(y)
    x_min = x[numpy.argmin(y)]
    y_min = numpy.min(y)

    # Основной график
    graph_axes[0].plot(x, y, label = 'График')
    graph_axes[0].plot([x_max], [y_max], 'o', color = 'g', label = 'т.max')
    graph_axes[0].plot([x_min], [y_min], 'o', color = 'r', label = 'т.min')
    y = tangent(1.2, x)
    graph_axes[0].plot(1.2, tangent(1.2, 1.2), 'o', color = 'orange')
    graph_axes[0].plot(x, y, linestyle = '--', color = 'orange', label = 'Касательная')
    y = normal(1.2, x)
    graph_axes[0].plot(1.2, normal(1.2, 1.2), 'o', color = 'magenta')
    graph_axes[0].set_ylim(-2, 2)
    graph_axes[0].plot(x, y, linestyle = '--', color = 'magenta', label = 'Нормаль')
    graph_axes[0].legend()
    # График производных
    y = scipy.misc.derivative(gauss, x, dx = 1e-6)
    graph_axes[1].plot(x, y)
    y = scipy.misc.derivative(gauss, x, dx = 1e-6, n = 2)
    graph_axes[2].plot(x, y)
   
   #Касательное расслоение
    tanget_rasl = [tangent(x_0, x) for x_0 in x]
    graph_axes[3].plot(x, tanget_rasl)

    #Вычисление и вывод длины дуги
    l = lambda x: numpy.sqrt(1 + scipy.misc.derivative(gauss, x, dx = 1e-6)**2)
    print(f'Длина дуги: {(scipy.integrate.quad(l, 0, 5))[0]}')
    pylab.show()